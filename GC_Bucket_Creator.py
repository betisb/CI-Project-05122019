from google.cloud import storage


def Bucket_Creator(project=None,bucket_name=None):
    storage_clinet = storage.Client(project=project)
    bucket = storage_clinet.create_bucket(bucket_name)
    print('Bucket {} Created.'.format(bucket.name))
    return bucket
