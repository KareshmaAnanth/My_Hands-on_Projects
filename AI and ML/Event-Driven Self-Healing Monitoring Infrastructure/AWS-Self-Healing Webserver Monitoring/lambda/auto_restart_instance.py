import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    # Extract instance ID and state from the EC2 state change event
    instance_id = event['detail']['instance-id']
    state = event['detail']['state']

    print(f"Instance {instance_id} changed to state: {state}")

    # Check if the instance has the AutoRestart tag set to "true"
    ec2 = boto3.client('ec2')
    tags_response = ec2.describe_tags(
        Filters=[
            {'Name': 'resource-id', 'Values': [instance_id]},
            {'Name': 'key', 'Values': ['AutoRestart']}
        ]
    )

    # Only proceed if the tag exists and its value is "true"
    auto_restart = False
    for tag in tags_response['Tags']:
        if tag['Key'] == 'AutoRestart' and tag['Value'] == 'true':
            auto_restart = True

    if not auto_restart:
        print(f"Instance {instance_id} does not have AutoRestart=true. Skipping.")
        return {'statusCode': 200, 'body': 'Skipped - no AutoRestart tag'}

    # Restart the stopped instance
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Restart initiated for instance {instance_id}")

    # Send a notification to the SelfHealingAlerts SNS topic
    sns = boto3.client('sns')
    topic_arn = os.environ['SNS_TOPIC_ARN']
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    message = (
        f"Auto-Restart Triggered\n"
        f"Instance ID: {instance_id}\n"
        f"Previous State: {state}\n"
        f"Action: Instance restart initiated\n"
        f"Reason: Instance was stopped and has AutoRestart=true tag\n"
        f"Timestamp: {timestamp}"
    )

    sns.publish(
        TopicArn=topic_arn,
        Subject=f'Auto-Restart: {instance_id}',
        Message=message
    )

    return {'statusCode': 200, 'body': f'Restarted instance {instance_id}'}