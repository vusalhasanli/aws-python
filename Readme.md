
#About 

Tutorial project to manage AWS envoirenment using boto3


##Configuration

###Set up profile -->

####create a user {piti} for AWS and give necessary permissions for used services
        
`aws configure --profile {user}` #assuming you have a user 'piti' and has full access for used services



#Installation

run `pip3 install https://piti.s3.amazonaws.com/piti-0.0.1-py3-none-any.whl`


#Usage:


`piti --help`

`piti COMMAND [OPTIONS] [ARGS]`

`piti buckets create --name=bucket_name`


#To uninstall the tool run `pip3 uninstall piti`



*commands*  `buckets create/list, instances start/stop/list, vpc list`



#Resources used

Boto3 documentation

https://boto3.amazonaws.com/v1/documentation/api/1.9.42/index.html

click_ documentation

https://click.palletsprojects.com/en/7.x/#documentation