import boto3
from enum import Enum

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


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='List contents of S3 bucket')
    parser.add_argument('--bucket', help='Name of bucket to list')
    parser.add_argument('-v', action='store_true', default=False, help='Verbose output (list all objects)')

    args = parser.parse_args()
    bucketname = args.bucket
    lister = BucketLister(bucketname)
    values = lister.ListObjects()
    bucketObjects = [BucketObject(o) for o in values]

    '''for obj in values:
        print(obj.key)
        parts = obj.key.split('/')
        print(parts)'''

    total_size = 0
    total_billable_size = 0
    for o in bucketObjects:
        total_size += o.Size
        total_billable_size += o.BillableSize
        if args.v:
            print(o.Name)

    print(f'Total # objects = {len(bucketObjects):,}')
    print(f'Total size = {total_size:,}')
    print(f'Billable size = {total_billable_size:,}')
