import boto3
import botocore
from botocore.exceptions import ClientError
import logging

AK='C5PR8CK8FB16NGAR125W'
SK='12345678'
url='http://192.168.20.143:7480'

s3=boto3.resource('s3',aws_access_key_id=AK,
                   aws_secret_access_key=SK,
                   endpoint_url=url)

def obj_exist(bucket,obj_name):
  for obj in bucket.objects.filter(Prefix=obj_name):
    if obj.key == obj_name:
      return True
  return False

choose=input("pls input your choose[bk,obj]: ")
bucket=input("pls intput bucket name: ")

if choose == 'bk':
  try:
    s3.meta.client.head_bucket(Bucket=bucket)
    print("bucket %s exist!" % bucket)
  except botocore.exceptions.ClientError as e:
    error_code = int(e.response['Error']['Code'])
    if error_code == 404:
      print("bucket not exist") 

elif choose == 'obj':
  bucket = s3.Bucket(bucket)
  obj_name=input("pls input object name: ")
  if obj_exist(bucket,obj_name):
    print("object %s exist!" % obj_name)
  else:
    print("object not exist!")

else:
  print("choose error!")
