from ensurepip import bootstrap
import boto3

s3 = boto3.client('s3')

s3.upload_file(
    Bucket = "ioe-assignment1",
    Key = "Image.jpg",
    Filename = "Data\Image.jpg"
)