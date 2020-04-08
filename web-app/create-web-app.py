import boto3
import json


session = boto3.Session(profile_name='architect')
s3 = boto3.client('s3')


# name = input("enter bucket name")
bucket_name = 'web-app'
def create_web_app(bucket_name):
    if bucket_name:
        try:
            bucket = s3.Bucket(bucket_name).create()
        except: print("{} bucket already exists..".format(bucket_name))
    else: print("something went wrong")

def set_policy(bucket_name):
    bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
            }]
        }
    bucket_policy = json.dumps(bucket_policy)
    # Set the new policy
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
    result = s3.get_bucket_policy(Bucket=bucket_name)
    print(result)
    
def enable_hosting(bucket_name):
    print("hello")





if __name__ == "__main__":
    create_web_app(bucket_name)
    set_policy(bucket_name)