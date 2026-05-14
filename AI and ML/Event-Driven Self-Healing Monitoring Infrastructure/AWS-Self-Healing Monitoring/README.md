##**Event-Driven Self-Healing DevOps Monitoring System on AWS**

###**Welcome**### 👋

This project demonstrates how modern DevOps systems can automatically detect infrastructure failures and remediate them without human intervention.

Instead of waking up at 3 AM to restart a crashed service, this architecture uses event-driven automation to detect failures, trigger remediation logic, and restore services automatically.

The result is a self-healing infrastructure pipeline built using core AWS services.

This project simulates a real operational scenario where a production web server fails, and the system detects, fixes, and notifies the operator automatically.

###**The Problem**###

In traditional infrastructure environments, when a web service crashes:

• Monitoring tools detect the issue  
• Engineers receive alerts       
• Someone logs into the server  
• The service is manually restarted

This process introduces downtime and requires human intervention.

In high-availability environments, systems must recover automatically without waiting for manual response.

###**The Solution**###

This project builds an event-driven remediation pipeline that:

• Detects abnormal system behavior  
• Triggers automated remediation  
• Restarts failed services  
• Sends notification alerts  
• Recovers stopped instances   automatically

*The architecture relies on cloud-native services such as*:

• Amazon EC2
• Amazon CloudWatch
• Amazon EventBridge
• AWS Lambda
• AWS Systems Manager
• Amazon SNS

###**Architecture Diagram**###

Below is the high-level architecture of the self-healing pipeline.

/architecture/self-healing-architecture.png

###**Architecture Flow**###

The self-healing pipeline works through an automated event chain:

1. A web server runs on an EC2 instance with nginx installed.
2. CloudWatch continuously monitors CPU utilization and service health.
3. When CPU usage exceeds the defined threshold, an alarm enters the ALARM state.
4. EventBridge detects the alarm state change and routes the event.
5. EventBridge triggers a Lambda remediation function.
6. Lambda sends a restart command to the EC2 instance using Systems Manager.
7. The nginx service is restarted automatically.
8. An SNS notification is sent confirming the remediation.

###**Extra: Instance Auto-Restart**###

To extend the automation, a second event-driven workflow was added.

This pipeline detects when an EC2 instance enters the stopped state and restarts it automatically if the instance has opted in through a tag.

###**Workflow**###:

1. EC2 emits a state change event when an instance stops.
2. EventBridge captures the stopped state event.
3. A second Lambda function checks for the AutoRestart=true tag.
4. If the tag exists, the instance is automatically restarted.
5. An SNS notification confirms the recovery action.

This ensures that critical infrastructure cannot remain offline accidentally.