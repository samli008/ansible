import boto3
import os

AK='L9JGMYNWV474ON35T8N7'
SK='al73vUQ1dVSCJ8A8beusVlMQMjZC4oEri6yQkQsN'
url='http://192.168.20.182:8084'

s3=boto3.resource('s3',aws_access_key_id=AK,
                   aws_secret_access_key=SK,
                   endpoint_url=url)

def s3_to_local(bucket_name, local):
  try:
    files = set(os.listdir(local))
    bucket = s3.Bucket(bucket_name)
    i=0
    for obj in bucket.objects.all():
      file = obj.key
      if file not in files:
        s3.Object(bucket_name,file).download_file(file)
        print("download file: %s" % file)
        i+=1
    if i == 0:
      print("no sync.")
  except:
    print("shit bucket not exist or directory not exist!")

bk=input("pls input bucket name: ")
local=input("pls local directory: ")

s3_to_local(bk,local)
