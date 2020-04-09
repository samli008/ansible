import boto3
from botocore.exceptions import ClientError
import os
import sys
import logging
import threading

s3=boto3.client('s3',aws_access_key_id='C5PR8CK8FB16NGAR125W',
                      aws_secret_access_key='12345678',
                      endpoint_url='http://192.168.20.143:7480')

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

print("{a:15}{b:15}".format(a='bucket',b='createTime'))

buckets=s3.list_buckets()
for bucket in buckets['Buckets']:
  name=bucket['Name']
  date=str(bucket['CreationDate'])
  print(f"{name:15}{date:15}")

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    try:
        response = s3.upload_file(file_name, bucket, object_name,Callback=ProgressPercentage(file_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True

file=input("pls input file name: ")
bucket=input("pls input bucket name: ")
upload_file(file,bucket)
