# from cgitb import text
# from unicodedata import name
import TACTelemetryReportingSchedule
# import yaml
# config = yaml.safe_load(open("././config.yml"))


# TACTelemetryReportingSchedule.main(10)
# TACTelemetryReportingSchedule.setup_for_files()


# work
# TACTelemetryReportingSchedule.loop_dates()
# 2022-07-24 2022-07-24
# 2022-07-23 2022-07-23
# 2022-07-22 2022-07-22
# 2022-07-21 2022-07-21
# 2022-07-20 2022-07-20
# 2022-07-19 2022-07-19
# 2022-07-18 2022-07-18
# 2022-07-18 2022-07-24
# 2022-06-27 2022-07-24




# TACTelemetryReportingSchedule.send_emails()

# work
# TACTelemetryReportingSchedule.loop_endpoints('2022-07-24','2022-07-24')


# work
# text =[
# ['id',"name","roll"],
# ['id',"name","roll"]
# ]
# TACTelemetryReportingSchedule.build_rows(text,'header',',')


# text = [{
# "id": 1,
# "name": "basant1",
# "roll":1
# },
# {
# "id": 2,
# "name": "basant2",
# "roll":2
# }
# ,{
# "id": 3,
# "name": "basant3",
# "roll":3
# }
# ]



# works
# TACTelemetryReportingSchedule.build_rows(text,'data',',')
# ,,"1","basant1","1",
# ,,"2","basant2","2",
# ,,"3","basant3","3",




# text = [{
# "id": 1,
# "name": "basant1",
# "roll":1
# },
# {
# "id": 2,
# "name": "basant2",
# "roll":2
# }
# ,{
# "id": 3,
# "name": "basant3",
# "roll":3
# }
# ]


# TACTelemetryReportingSchedule.export_to_csv("user_events",text,'2022-07-24','2022-07-24')


# works
# TACTelemetryReportingSchedule.write_csv_row("user_events.csv", "id, name, roll",'w')





# import os
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
# connect_str = 'DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;'


# container_name = 'icontainer'
# blob_name = 'user_events.txt'
# local_path = "./Downoaded"
# local_file_name = "idownload.txt"




# def uploadDataToTheBlobContainer(data):
#     try:
#         print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
#         blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#         blob_client = blob_service_client.get_blob_client(container_name, blob_name)

#         print("\nUploading to Azure Storage as blob")
#         blob_client.upload_blob(data,overwrite=True)
    

#     except Exception as ex:
#         print('Exception:')
#         print(ex)





# def downloadDataToTheBlobContainer():
#     try:
#         print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
#         # Create the BlobServiceClient object which will be used to create a container client
#         blob_service_client = BlobServiceClient.from_connection_string(connect_str)




#         # Download the blob to a local file
#         # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
#         download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
#         blob_client = blob_service_client.get_container_client(container_name) 
#         print("\nDownloading blob to \n\t" + download_file_path)

#         with open(download_file_path, "wb") as download_file:
#             download_file.write(blob_client.download_blob(blob_name).readall())



#     except Exception as ex:
#         print('Exception:')
#         print(ex)





# uploadDataToTheBlobContainer("hello tesk")
# downloadDataToTheBlobContainer()



TACTelemetryReportingSchedule.Main()
print("run completed")





