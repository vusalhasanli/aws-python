import boto3


if __name__ == "__main__":
    user_name = input("User name: ")
    session = boto3.Session(profile_name=user_name)
    s3 = boto3.resource('s3')


    for bucket in s3.buckets.all():
        print(bucket.name)