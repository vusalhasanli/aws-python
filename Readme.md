#Tutorial

Tutorial project to manage AWS envoirenment using boto3


#About 

Use boto3 to make python scripts for each AWS services


#Configuration 

Set up profile -->
        `aws configure --profile {user}` #assuming user has full access for used services

#Commands

For help run `python3 aws_env.py --help`

List S3 buckets, run `python3 aws_env.py list-buckets`

List ec2 instances, run `python3 aws_env.py list-instances` ----> `python3 aws_env.py list-instances --tag=tag_name`

Create a bucket, run `python3 aws_env.py create-bucket --name=bucket_name`

Start ec2 instances, run `python3 aws_env.py start-instances` ---> `python3 aws_env.py start-instances --tag=tag_name`



#Resources used

Boto3 documentation

https://boto3.amazonaws.com/v1/documentation/api/1.9.42/index.html

click_ documentation

https://click.palletsprojects.com/en/7.x/#documentation