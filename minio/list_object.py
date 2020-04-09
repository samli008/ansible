# pip3 install minio -i https://mirrors.aliyun.com/pypi/simple
from minio import Minio

cq = Minio('samli008.f3322.net:9009',
                    access_key='admin',
                    secret_key='12345678',
                    secure=False)

print("{a:15}{b:25}{c:10}".format(a='bucket',b='object',c='size'))

buckets = cq.list_buckets()

for bucket in buckets:
    objects = cq.list_objects(bucket.name,recursive=True)
    for obj in objects:
      size=int(obj.size/1024**2)
      size=str(size)+'MB'
      bkname=str(obj.bucket_name)
      ojname=str(obj.object_name)
      print(f"{bkname:15}{ojname:25}{size:10}")
