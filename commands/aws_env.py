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
        try:
            bucket = s3.Bucket(name)
            bucket.create()
        except: print("Bucket name already exists.. Please choose a different name..")
    else: print('Please insert a bucket name like so --name=bucket_name')



#----------------- ec2 section -------------------------#
    
def filter_instances(tag):
    instances = []
    if tag:
        filters = [{ 'Name': 'tag:Project', 'Values': [tag]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances


@aws_env.command('list-instances')
@click.option('--tag', default=None, help='Filter instances by tags')
def list_instances(tag):
    "List ec2 instances"
    instances = filter_instances(tag)
    for instance in instances:
        print(', '.join((
            instance.id,
            instance.instance_type,
            instance.placement['AvailabilityZone'],
            instance.state['Name'],
            instance.public_dns_name
        )))

@aws_env.command('stop-instances')
@click.option('--tag', default=None, help='Filter instances by tags')
def stop_instances(tag):
    "Stop instances"
    instances = filter_instances(tag)
    for i in instances:
        i.stop()
        print(i.id, i.state)

@aws_env.command('start-instances')
@click.option('--tag', default=None, help='Filter instances by tags')
def start_instances(tag):
    "Start instances"
    instances = filter_instances(tag)
    for i in instances:
        i.start()
        print(i.id, i.state)




#----------------- VPC section -------------------------#

@aws_env.command('list-vpc')
def list_custom_vpcs():
    "List custom vpcs"
    # filters = [{'Name': 'tag:Name', 'Values': ['Custom']}]
    # for vpc in ec2.vpcs.filter(Filters=filters):
    #     print(vpc.id)
    for vpc in ec2.vpcs.all():
        if not vpc.is_default:
            print(
                vpc.vpc_id,
                vpc.state,
                vpc.cidr_block,
                vpc.tags,
                vpc.is_default
                )







if __name__ == "__main__":
    aws_env()
    

    