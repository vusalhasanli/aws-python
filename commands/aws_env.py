import boto3
import click


session = boto3.Session(profile_name='architect')
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')


@click.group()
def aws_env():
    """Commands for aws resources"""



#----------------- S3 section -------------------------#

@aws_env.group('buckets')
def buckets():
    "Commands for s3"

@buckets.command('list')
def list_buckets():
    "List s3 buckets"
    buckets = s3.buckets.all()

    for bucket in buckets:
        print(bucket.name)

@aws_env.command('create')
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

@aws_env.group('instances')
def instances():
    "Commands for ec2"


@instances.command('list')
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

@instances.command('stop')
@click.option('--tag', default=None, help='Filter instances by tags')
def stop_instances(tag):
    "Stop instances"
    instances = filter_instances(tag)
    for i in instances:
        i.stop()
        print(i.id, i.state)

@instances.command('start')
@click.option('--tag', default=None, help='Filter instances by tags')
def start_instances(tag):
    "Start instances"
    instances = filter_instances(tag)
    for i in instances:
        i.start()
        print(i.id, i.state)




#----------------- VPC section -------------------------# 

@aws_env.group('vpc')
def v_p_c():
    "Commands for vpc"

@v_p_c.command('list')
@click.option('--tag', default=None, help='To see some info about specifice vpc, give --tag=name, it is case sensitive')
def list_custom_vpcs(tag):
    "List custom vpcs"
    if tag:
        filters = [{'Name': 'tag:Name', 'Values': [tag]}]
        vpc_s = ec2.vpcs.filter(Filters=filters)
    else: vpc_s = ec2.vpcs.all()
    for v in vpc_s:
        print(
            v.id,
            v.state
            )
    # for vpc in ec2.vpcs.all():
    #     if not vpc.is_default:
    #         print(
    #             vpc.vpc_id,
    #             vpc.state,
    #             vpc.cidr_block,
    #             vpc.tags,
    #             vpc.is_default
    #             )





if __name__ == "__main__":
    aws_env()
    

    