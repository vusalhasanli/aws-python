import boto3
import click


session = boto3.Session(profile_name='architect')
s3 = boto3.resource('s3')
buckets = s3.buckets.all()

@click.group()
def buckets():
    """Commands for buckets"""

@buckets.command()
@click.option( '--name', default=None, help='list s3 buckets')
def list_buckets(name):
    buckets = s3.buckets.all()

    for bucket in buckets:
        print(bucket.name)


# @buckets.command()
# @click.option('--create', default=None, help='create a bucket')
# def create_bucket():
#     






# ---------->> Continue later
# def list_objects(bucket, buckets):
#     if bucet:
#         bucket.name = bucet
#         for obj in bucket.objects.filter(Prefix='photos/'):
#                 print('{0}:{1}'.format(bucke.name, obj.key))
#         # print(bucket.name)
#     else: print("something went wrong")




if __name__ == "__main__":
    buckets()
    

    