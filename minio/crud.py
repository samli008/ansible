import boto3
import botocore
from botocore.exceptions import ClientError
import logging

AK='L9JGMYNWV474ON35T8N7'
SK='al73vUQ1dVSCJ8A8beusVlMQMjZC4oEri6yQkQsN'
url='http://192.168.20.182:8084'

s3=boto3.resource('s3',aws_access_key_id=AK,
                   aws_secret_access_key=SK,
                   endpoint_url=url)
def list():
  for bucket in s3.buckets.all():
    print('bucket name: %s' % bucket.name)

def new():
  new=input("pls intput new bucket name: ")
  s3.create_bucket(Bucket=new)
  for bucket in s3.buckets.all():
    print('bucket name: %s' % bucket.name)

def del1(): 
  del1=input("pls input del bucket name: ")
  try:
    bucket= s3.Bucket(del1)
    bucket.delete()
    for bucket in s3.buckets.all():
      print('bucket name: %s' % bucket.name)
  except botocore.exceptions.ClientError as e:
    print('bucket is not empty or not exist')

def list_obj():
  bucket_name = input("bucket name: ")
  bucket = s3.Bucket(bucket_name)
  for obj in bucket.objects.all():
    print('obj name: %s' % obj.key)

def up():
  bucket_name = input("bucket name: ")
  file = input("file name: ")
  s3.Object(bucket_name,file).upload_file(file)

def down():
  bucket_name = input("bucket name: ")
  file = input("file name: ")
  s3.Object(bucket_name,file).download_file(file)

def delete():
  try:
    bucket_name = input("bucket name: ")
    bucket= s3.Bucket(bucket_name)
    bucket.objects.filter().delete()
  except botocore.exceptions.ClientError as e:
    print('bucket is not exist')

choose=input("pls input your choose[list,new,del,obj,up,down,delete]: ")

if choose == 'list':
  list()
elif choose == 'new':
  new()
elif choose == 'del':
  del1()
elif choose == 'obj':
  list_obj()
elif choose == 'up':
  up()
elif choose == 'down':
  down()
elif choose == 'delete':
  delete()
else:
  print("your choose error!")
