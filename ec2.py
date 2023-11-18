from tokenize import Name
import boto3

def ec2_demo ():
    ec2 = boto3.resource('ec2',region_name='eu-north-1')
    demo_instance = ec2.create_instances(
        ImageId='ami-0416c18e75bd69567',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro',
        KeyName='PK_CLI_Demo_1'
    )

    s3_client = boto3.client('s3', region_name='eu-north-1')
    location = {'LocationConstraint': 'eu-north-1'}
    s3_client.create_bucket(Bucket='pkatu-py-bucket2', CreateBucketConfiguration=location)   
    try:
        s3_client.upload_file('c:\\new.txt', 'pkatu-py-bucket2', 'new.txt')
        print("File uploaded successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")   
    print (demo_instance)
    response = s3_client.list_buckets()
    print("Existing buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

if __name__ == '__main__':
    ec2_demo()