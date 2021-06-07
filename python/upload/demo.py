import os
from pprint import pprint
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'green-cell-312416-fcbc59926fd3.json'

storage_client = storage.Client()
bucket_name = 'cmask'

# Get Bucket
# my_bucket = storage_client.get_bucket(bucket_name)
# pprint(vars(my_bucket))

# Upload File
def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob


blob = "uwu"
pathFile = "image/test.jpg"

response = upload_to_bucket(pathFile, pathFile, bucket_name)
# response = upload_to_bucket('/docs/requirementABC', 'requirements.txt', bucket_name)

print(response)




