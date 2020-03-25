
# About 

Tutorial project to manage AWS envoirenment using boto3


## Configuration

### Set up profile -->

#### create a user named 'piti' in AWS and give necessary permissions for used services

#### Then run

`aws configure --profile piti`



# Installation

run `pip3 install https://piti.s3.amazonaws.com/piti-0.0.1-py3-none-any.whl`


# Usage:

*commands*  `buckets create/list, instances start/stop/list, vpc list`

`piti --help`

`piti COMMAND [OPTIONS] [ARGS]`

`piti buckets create --name=bucket_name`


### To uninstall the tool run 

`pip3 uninstall piti`



##### Resources used

Boto3 documentation

https://boto3.amazonaws.com/v1/documentation/api/1.9.42/index.html

click_ documentation

https://click.palletsprojects.com/en/7.x/#documentation