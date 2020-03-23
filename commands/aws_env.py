import boto3
import click


session = boto3.Session(profile_name='architect')
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

@click.group()
def aws_env():
    """Commands for buckets"""

@aws_env.command()
@click.option( '--name', default=None, help='list s3 buckets')
def list_buckets(name):
    buckets = s3.buckets.all()

    for bucket in buckets:
        print(bucket.name)


@aws_env.command()
def list_instances():
    for instance in ec2.instances.all():
        print(instance)
    





if __name__ == "__main__":
    aws_env()
    

    