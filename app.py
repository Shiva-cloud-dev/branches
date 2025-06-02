s3 = boto3.client('s3')

# 1. List all S3 buckets
response = s3.list_buckets()
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")

# Replace with your bucket and file info
bucket_name = 'your-bucket-name'
upload_file_path = 'path/to/local/file.txt'
download_file_path = 'path/to/save/file.txt'
s3_key = 'uploaded-file.txt'
