from minio import Minio
from minio.error import S3Error
import os

client = Minio("minio.pish.pstu.ru:80",
    access_key="SUS2BB4MvMlGIrCz2Ufa",
    secret_key="jxmdtycNJHMv2WEW0XKZeynfwwiVaKLgZ3QXpfO0",
    secure=False
)


# The destination bucket and filename on the MinIO server
bucket_name = "ai-data"
destination_folder = os.path.join("re-id", "train")

# Получение списка объектов в папке
print(f"\nСписок файлов в папке '{destination_folder}':")
objects = client.list_objects(bucket_name, prefix=destination_folder, recursive=True)
for obj in objects:
    print(f"- {obj.object_name} (Размер: {obj.size} байт)")