import boto3
import json

# Configuration
REGION = 'us-east-2'
INSTANCE_ID = 'YOUR_INSTANCE_ID_HERE' # Paste instance ID here

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    
    # This command turns the server on
    ec2.start_instances(InstanceIds=instances)
    
    print('Started your instance: ' + str(instances))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Server is starting up!')
    }