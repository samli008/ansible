from minio import Minio

cq = Minio('samli008.f3322.net:9009',
                    access_key='admin',
                    secret_key='12345678',
                    secure=False)

print("{a:10}{b:15}".format(a='bucket',b='createTime'))

buckets = cq.list_buckets()
for bucket in buckets:
  date=str(bucket.creation_date)
  print(f"{bucket.name:10}{date:15}")

mybucket=input('pls input new bucket name: ')

try:
  cq.bucket_exists("mybucket")
  cq.make_bucket(mybucket, location="us-east-1")

  print("{a:10}{b:15}".format(a='bucket',b='createTime'))

  buckets = cq.list_buckets()
  for bucket in buckets:
    date=str(bucket.creation_date)
    print(f"{bucket.name:10}{date:15}")

except:
  print("Sorry bucket already exist!!!")
