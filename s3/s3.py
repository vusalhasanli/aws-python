import boto3
import click


session = boto3.Session(profile_name='architect')
s3 = boto3.resource('s3')

@click.group()
def buckets():
    """Commands for buckets"""

@buckets.command()
@click.option( '--name', default=None, help='list s3 buckets')
def list_buckets(name):
    buckets = s3.buckets.all()

    for bucket in buckets:
        print(bucket.name)



if __name__ == "__main__":
    buckets()
    

    