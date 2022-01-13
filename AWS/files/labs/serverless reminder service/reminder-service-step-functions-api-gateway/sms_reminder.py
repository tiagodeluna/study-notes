import boto3

sns = boto3.client('sns', 'us-east-1')

def lambda_handler(event, context):
    sns.publish(PhoneNumber=event['phone'], Message=event['message'])
    return 'Success!'