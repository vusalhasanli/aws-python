import boto3
import click



session = boto3.Session(profile_name='architect')
s3 = boto3.resource('s3')

@click.command()
@click.option( '--list', default=None, help='list s3 buckets')

def list_buckets(list):
    if list:
        print('---- filtered ----')
        buckets = s3.buckets.filter(Prefix='my-')
    else:
        buckets = s3.buckets.all()
        # print("unfiltered")
    
    for bucket in buckets:
        print(bucket.name)




if __name__ == "__main__":
    list_buckets()
    

    