import boto3
import argparse


# function to list all the aws resources created by cloudformation stack 
def get_stack_resources(stack_identifier):
    cf = boto3.client('cloudformation')
    try:
        if stack_identifier.startswith("arn:"):
            # If ARN is provided, use it directly
            stack_name = stack_identifier.split('/')[-1]
        else:
            # Otherwise, it's a stack name
            stack_name = stack_identifier
        
        resources = cf.describe_stack_resources(StackName=stack_name)
        print(f"\nResources in stack '{stack_name}':")
        for res in resources['StackResources']:
            print(f"- {res['LogicalResourceId']} ({res['ResourceType']}): {res['PhysicalResourceId']}")
    except Exception as e:
        print(f"Error fetching stack resources: {e}")

# function to list all ec2 instances

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    print("\nEC2 Instances:")
    for res in instances['Reservations']:
        for inst in res['Instances']:
            print(f"- Instance ID: {inst['InstanceId']}, State: {inst['State']['Name']}")

# function to list all the s3 buckets in your aws account

def list_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    print("\nS3 Buckets:")
    for bucket in buckets['Buckets']:
        print(f"- {bucket['Name']}")

# function to list all the rds instances in your aws account

def list_rds_instances():
    rds = boto3.client('rds')
    dbs = rds.describe_db_instances()
    print("\nRDS Instances:")
    for db in dbs['DBInstances']:
        print(f"- {db['DBInstanceIdentifier']} (Status: {db['DBInstanceStatus']})")

def main():
    parser = argparse.ArgumentParser(description='Fetch inventory from AWS using a CloudFormation stack name or ARN.')
    parser.add_argument('--stack-name', help='Name of the CloudFormation stack')
    parser.add_argument('--stack-arn', help='ARN of the CloudFormation stack')
    args = parser.parse_args()

    if args.stack_name:
        get_stack_resources(args.stack_name)
    elif args.stack_arn:
        get_stack_resources(args.stack_arn)
    else:
        print("Error: You must provide either --stack-name or --stack-arn")

    list_ec2_instances()
    list_s3_buckets()
    list_rds_instances()

if __name__ == "__main__":
    main()
