import datetime
import os
from os.path import exists
import base64
import yaml
import datetime
import azure.functions as func
from urllib3.exceptions import HTTPError
from sendgrid import SendGridAPIClient, To
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition)
from azure.storage.blob import BlobServiceClient, __version__

config = yaml.safe_load(open("config.yml"))

# Assuming the api response looks like this
text = [{
"id": 1,
"name": "basant1",
"roll":1
},
{
"id": 2,
"name": "basant2",
"roll":2
}
,{
"id": 3,
"name": "basant3",
"roll":3
},{
"id": 1,
"name": "basant1",
"roll":1
},
{
"id": 2,
"name": "basant2",
"roll":2
}
,{
"id": 3,
"name": "basant3",
"roll":3
},{
"id": 1,
"name": "basant1",
"roll":1
},
{
"id": 2,
"name": "basant2",
"roll":2
}
,{
"id": 3,
"name": "basant3",
"roll":3
}
]


connect_str = 'DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;'


container_name = 'icontainer'
blob_name = 'user_events.txt'
local_path = "./Downoaded"
local_file_name = "idownload.txt"




def send_emails(data):
    """_summary_
    function to send email to the configured recipient

    Args:
        data (ray text): data downloaded from azure blob container
    """    
    message = Mail(
    from_email= config['Email_distribution_list']['from_email'],
    to_emails= [To(config['Email_distribution_list']['to_emails_recipient1']), To(config['Email_distribution_list']['to_emails_recipient2']), To(config['Email_distribution_list']['to_emails_recipient3']), To(config['Email_distribution_list']['to_emails_recipient4'])],
    subject= config['Email_distribution_list']['email_subject'],
    html_content= config['Email_distribution_list']['email_html_content'],
    is_multiple=True)

    # # Where it was uploaded Path.
    file_path = '../Downoaded'
    # # filenames = [os.path.join(file_path, f) for f in os.listdir(file_path)]
    filenames = 'idownload.txt'
    print(file_path)
    print(filenames)

    encoded_file = base64.b64encode(data).decode('utf-8')
    attachedFile = Attachment(
    FileContent(encoded_file),
    FileName("fileName"),
    FileType('text/csv'),
    Disposition('attachment')
    )
    message.attachment = attachedFile


    sg = SendGridAPIClient(os.environ.get('Sendgrid.apikey'))
    try:
        response = sg.send(message)
    except HTTPError as e:
        print(e.to_dict)


def loop_endpoints(start_date, end_date):
    """_summary_

    Args:
        start_date (date): starting date
        end_date (date): ending date
    """    # hit the endpoints for each date range
    for end_point_key in config['api']['endpoints']:
        base_url = config['api']['base_url'] + '/' + config['api']['endpoints'][end_point_key]
        export_to_csv(end_point_key, base_url, start_date, end_date)



def export_to_csv(end_point_key, report_parsed, start_date, end_date):
    # from datetime import datetime
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    if (report_parsed != []):
        tdelta = end_date - start_date
        if tdelta.days == 0:
            period_type = 'Daily'
        elif tdelta.days == 6:
            period_type = 'Weekly'
        else:
            period_type = '28 day'

        
        file_name = 'user_events.csv'
        cwd = os.getcwd() 
        print(cwd)
        file_name = cwd+'/'+file_name
        print(file_name)

        if not exists(file_name):
            # only write header row if file does not yet exist
            write_csv_row(file_name,build_rows(report_parsed,'data'), 'w')
        print("My name"+build_rows(report_parsed,'data'))
        write_csv_row(file_name,build_rows(report_parsed,'data'), 'a')


def build_rows(report_parsed, mode, period_type = "user_events"):
    this_row = ''
    if type(report_parsed) == list:
        # TODO: Needs work to parse out properly in CSV file
        if (mode == "header"):
            this_row += "\"PeriodType\","
            j = 0;
            for row in report_parsed:
                for key in row:
                    if (j == 0):
                        this_row += "\"" + key + "\","
                j += 1
        elif (mode == "data"):
            i = 0
            for row in report_parsed:
                this_row += period_type + ","
                for key in row:
                    print(key)
                    this_row += "\"" + str(row[key]) + "\","
                i += 1
                if i < len(report_parsed):
                    this_row += "\n"
    else:
        if mode == 'header':
            this_row = "\"PeriodType\","
        else:
            this_row = period_type + ","
        for key in report_parsed:
            if mode == 'header':
                this_row += "\"" + key + "\","
            else:
                this_row += "\"" + str(report_parsed[key]) + "\","
    print(this_row)
    return this_row


def write_csv_row(file_name, row, mode='a'):
    csv_file = open(file_name, mode, encoding="utf8")
    csv_file.write(row + "\n")  # manually modify this CSV file header
    csv_file.close()









def uploadDataToTheBlobContainer(data):
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)

        print("\nUploading to Azure Storage as blob")
        blob_client.upload_blob(data,overwrite=True)
    

    except Exception as ex:
        print('Exception:')
        print(ex)





def downloadDataToTheBlobContainer():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Download the blob to a local file
        # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
        download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
        blob_client = blob_service_client.get_container_client(container_name) 
        print("\nDownloading blob to \n\t" + download_file_path)

        with open(download_file_path, "wb") as download_file:
            downloadedData = blob_client.download_blob(blob_name).readall()
            download_file.write(downloadedData)
            return downloadedData



    except Exception as ex:
        print('Exception:')
        print(ex)






print("run completed")


def Main():
    filteredDataFromAllTheProcessWeHaveDoneSoFar = build_rows(text,'data',',')
    uploadDataToTheBlobContainer(filteredDataFromAllTheProcessWeHaveDoneSoFar)
    downloadedData = downloadDataToTheBlobContainer()
    send_emails(downloadedData)

