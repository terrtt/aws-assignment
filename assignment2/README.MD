### Task Requirements:
CloudFormation Template:
Create a YAML file containing a CloudFormation template.

The template should get all readonly access for the resources such as EC2, S3 Bucket, etc.
Generate a CloudFormation Stack Launch URL that can be used to create the stack on AWS.

Python Script:

Create a Python script that does not use access key, secret key, or role ARN explicitly.
The script should dynamically use the CloudFormation Stack ARN URL as an input to connect with the AWS account.

After the stack is created, your script should connect AWS cloud and fetch all inventory details from the created resources (e.g., EC2 instances, S3 buckets) using the Stack ARN or Stack Name.
You can assume that the script is running within an environment that has sufficient IAM permissions via instance profile or assumed role, so you must not hardcode or manually pass any credentials.

 ### solution:

# step1 : i created a yaml file containig the cloud formation template that created a iam role ReadOnlyAccessrole-wibix ,this iam role can be assumed by ec2 instance,it attaches the manage aws polivies to the role and the output section gives you the role name and arn 

then i upload this file to a public s3 bucket and apply the bucket policy to make the object publicaly accesible 

# step2: i created a stcak using this the arn of my s3 bucket using aws console

# step3: i launch a ec2 instance with suitable permissions and install all the dependencies to run the python script 

```bash
python3 fetc.py --stack-name ReadOnlyStack
```
this gives the output of the resources (ec2,s3,etc...). 

I have attached screenshots of my work also please have a look on them also...