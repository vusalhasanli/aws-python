
#About 

Tutorial project to manage AWS envoirenment using boto3


#Configuration

Set up profile -->
        `aws configure --profile {user}` #assuming user has full access for used services


Usage:


`python aws_env.py --help`

`python commands/aws_env.py COMMAND [OPTIONS] [ARGS]`

`python commands/aws_env.py buckets create --name=bucket_name`



*commands*  `buckets create/list, instances start/stop/list, vpc list`



#Resources used

Boto3 documentation

https://boto3.amazonaws.com/v1/documentation/api/1.9.42/index.html

click_ documentation

https://click.palletsprojects.com/en/7.x/#documentation