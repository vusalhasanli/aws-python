import boto3
import click


session = boto3.Session(profile_name='architect')
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

@click.group()
def aws_env():
    """Commands for aws resources"""



#----------------- S3 section -------------------------#
@aws_env.command('list-buckets')
def list_buckets():
    "List s3 buckets"
    buckets = s3.buckets.all()

    for bucket in buckets:
        print(bucket.name)

@aws_env.command('create-bucket')
@click.option('--name', default=None, help='Create a bucket')
def create_bucket(name):
    "Make a bucket"
    if name:
        bucket = s3.Bucket(name)
        bucket.create()
    #need to handle bucket_name_exists error
    else: print('Please insert a bucket name like so --name=bucket_name')



#----------------- ec2 section -------------------------#
@aws_env.command('list-instances')
def list_instances():
    "List ec2 instances"
    for instance in ec2.instances.all():
        print(instance)
    





if __name__ == "__main__":
    aws_env()
    

    