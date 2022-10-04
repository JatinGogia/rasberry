from ensurepip import bootstrap
import boto3

s3 = boto3.client('s3')

obj = s3.get_object(
    Bucket = "ioe-assignment1",
    Key = "Image.jpg",
)

s3.download_file(
    Bucket = "ioe-assignment1",
    Key = "Image.jpg",
    Filename = "BucketImage.jpg"
)