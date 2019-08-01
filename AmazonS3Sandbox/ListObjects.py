import boto3, os
from enum import Enum
import sqlite3

class StorageClass(Enum):
    STANDARD = 1
    REDUCED_REDUNDANCY = 2
    GLACIER = 3
    STANDARD_IA = 4
    ONEZONE_IA = 5
    INTELLIGENT_TIERING = 6
    DEEP_ARCHIVE = 7

class BucketObject():

    MinBillableSize = 128 * 1024

    def __init__(self, objectSummary):
        self._objectSummary = objectSummary

    @property
    def Name(self):
        return self._objectSummary._key

    @property
    def Size(self):
        return self._objectSummary.size

    @property
    def BillableSize(self):
        if self.Size < self.MinBillableSize and (self.StorageClass == StorageClass.ONEZONE_IA or self.StorageClass == StorageClass.STANDARD_IA):
            return self.MinBillableSize
        else:
            return self.Size


    @property
    def StorageClass(self):
        return StorageClass[self._objectSummary.storage_class]

class BucketLister():
    def __init__(self, bucketname):
        s3 = boto3.resource('s3')
        self._bucket = s3.Bucket(bucketname)

    def ListObjects(self):
        return self._bucket.objects.all()

def CaptureToDatabase(bucketObjects, pathname):
    if os.path.exists(pathname):
        os.remove(pathname)
    with sqlite3.connect(pathname) as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE "FileObjects" ( 
            "Name"	TEXT,
            "Size"	INTEGER,
            "BillableSize"	INTEGER,
            "StorageClass"  INTEGER,
	        PRIMARY KEY("Name")
            )''')
        for obj in bucketObjects:
            cursor.execute('''INSERT INTO FileObjects(Name,Size,BillableSize,StorageClass)
                              VALUES(?,?,?,?)''', (obj.Name, obj.Size, obj.BillableSize, obj.StorageClass.value))

def ListObjects(bucketObjects, verbose):
    total_size = 0
    total_billable_size = 0
    for o in bucketObjects:
        total_size += o.Size
        total_billable_size += o.BillableSize
        if verbose:
            print(o.Name)

    print(f'Total # objects = {len(bucketObjects):,}')
    print(f'Total size = {total_size:,}')
    print(f'Billable size = {total_billable_size:,}')

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='List contents of S3 bucket')
    parser.add_argument('--bucket', help='Name of bucket to list')
    parser.add_argument('-v', action='store_true', default=False, help='Verbose output (list all objects)')
    parser.add_argument('--capture', help='Pathname to database to capture file information')

    args = parser.parse_args()
    bucketname = args.bucket
    lister = BucketLister(bucketname)
    values = lister.ListObjects()

    bucketObjects = [BucketObject(o) for o in values]

    if args.capture != None:
        CaptureToDatabase(bucketObjects, args.capture)
    else:
        ListObjects(bucketObjects, args.v)

