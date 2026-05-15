import boto3
import json
import datetime

# Create AWS service clients
ssm = boto3.client('ssm')
sns = boto3.client('sns')

# Replace with your actual SNS topic ARN from the SNS console
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:799990344483:SelfHealingAlerts'
def lambda_handler(event, context):
    # Extract alarm name from the EventBridge event
    alarm_name = event['detail']['alarmName']

    # Extract instance ID from the alarm's metric dimensions
    instance_id = event['detail']['configuration']['metrics'][0]['metricStat']['metric']['dimensions']['InstanceId']

    # Send SSM Run Command to restart nginx on the affected instance
    ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': ['sudo systemctl restart nginx']}
    )

    # Build a remediation summary with timestamp
    timestamp = datetime.datetime.now().isoformat()
    message = (
        f"Self-Healing Remediation Executed\n"
        f"Alarm: {alarm_name}\n"
        f"Instance: {instance_id}\n"
        f"Action: Restarted nginx via SSM Run Command\n"
        f"Timestamp: {timestamp}"
    )

    # Publish the summary to SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f'Self-Healing Alert: {alarm_name}',
        Message=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Remediation complete')
    }