import boto3
from datetime import datetime
import os

if __name__ == "__main__":
    '''Usage:
    PutObject.py --bucket <bucketname> --key <keyname> -f <filename>'''
    import argparse

    parser = argparse.ArgumentParser(description='Put a single file into an S3 bucket')
    parser.add_argument('--bucket', help='Name of S3 bucket to store file')
    parser.add_argument('--key', help='Key name to store in bucket')
    parser.add_argument('--file', help='Pathname of file to store')

    args = parser.parse_args()

    s3 = boto3.resource('s3')
    s3_object = s3.Object(args.bucket, args.key)
    f = open(args.file, 'rb')
    date_str = datetime.fromtimestamp(os.path.getmtime(args.file)).strftime('%Y-%m-%d %H:%M:%S')
    s3_object.put(Body=f, Metadata={'date': date_str})
