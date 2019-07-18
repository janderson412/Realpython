import boto3

class BucketLister():
    def __init__(self, bucketname):
        #self._bucketName = bucketname
        #self._client = boto3.client('s3')
        s3 = boto3.resource('s3')
        self._bucket = s3.Bucket(bucketname)

    def ListObjects(self):
        #fields = self._client.list_objects_v2(Bucket=self._bucketName)
        #return fields['Contents']
        return self._bucket.objects.all()


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='List contents of S3 bucket')
    parser.add_argument('--bucket', help='Name of bucket to list')

    args = parser.parse_args()
    bucketname = args.bucket
    lister = BucketLister(bucketname)
    values = lister.ListObjects()

    for obj in values:
        print(obj.key)

    print('')
