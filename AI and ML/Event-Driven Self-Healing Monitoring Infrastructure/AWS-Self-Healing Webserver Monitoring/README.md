# 🚑 Event-Driven Self-Healing DevOps Monitoring System on AWS
**Project Link:** [View Project](https://learn.nextwork.org/projects/c2f11661-fe60-4106-8034-5f705896ba61)

**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)

**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

---
## 👋 Welcome

This project demonstrates how modern DevOps systems can automatically detect infrastructure failures and remediate them without human intervention.

Instead of waking up at 3 AM to restart a crashed service, this architecture uses event-driven automation to detect failures, trigger remediation logic, and restore services automatically.

The result is a **self-healing infrastructure pipeline** built using core AWS services.

This project simulates a real operational scenario where a production web server fails, and the system detects, fixes, and notifies the operator automatically.

---

## ⚠️ The Problem

In traditional infrastructure environments, when a web service crashes:

- Monitoring tools detect the issue  
- Engineers receive alerts  
- Someone logs into the server  
- The service is manually restarted  

This process introduces downtime and requires **human intervention**.

In high-availability environments, systems must recover automatically without waiting for manual response.

---

## 💡 The Solution

This project builds an **event-driven remediation pipeline** that:

- Detects abnormal system behavior  
- Triggers automated remediation  
- Restarts failed services  
- Sends notification alerts  
- Recovers stopped instances automatically  

The architecture relies on cloud-native services such as:

- Amazon EC2  
- Amazon CloudWatch  
- Amazon EventBridge  
- AWS Lambda  
- AWS Systems Manager  
- Amazon SNS  

---

## ⚙️Tech Stack 

## AWS Services Used

| Service             | Purpose                      |
|---------------------|------------------------------|
| EC2                 | Hosts nginx web server       |
| CloudWatch          | Monitors system metrics      |
| EventBridge         | Routes infrastructure events |
| AWS Lambda          | Executes remediation logic   |
| AWS Systems Manager | Runs remote commands on EC2  |
| Amazon SNS          | Sends email notifications    |
| IAM                 | Manages permissions securely |

---

## 🏗 Architecture Diagram

Below is the high-level architecture of the self-healing pipeline.

![self-healing-architecture](https://github.com/KareshmaAnanth/My_Hands-on_Projects/blob/5fae23d8a460b0c537205f4522fd2b367e029e7c/AI%20and%20ML/Event-Driven%20Self-Healing%20Monitoring%20Infrastructure/AWS-Self-Healing%20Webserver%20Monitoring/architecture/self-healing-architecture.gif)

---

## 🔄 Architecture Flow

The self-healing pipeline works through an automated event chain:

1. A web server runs on an EC2 instance with **nginx** installed.  
2. CloudWatch continuously monitors CPU utilization and service health.  
3. When CPU usage exceeds the defined threshold, an alarm enters the **ALARM** state.  
4. EventBridge detects the alarm state change and routes the event.  
5. EventBridge triggers a Lambda remediation function.  
6. Lambda sends a restart command to the EC2 instance using Systems Manager.  
7. The nginx service is restarted automatically.  
8. An SNS notification is sent confirming the remediation.

## Workflow

The Lambda function performs the following tasks:  
  1. Receives CloudWatch alarm events  
  2. Extracts instance ID from event payload  
  3. Sends SSM Run Command to restart nginx  
  4. Publishes notification to SNS

Example command executed via SSM:
sudo systemctl restart nginx

---

## 🎯 Extra: Instance Auto-Restart

To extend the automation, a **second event-driven workflow** was added.

This pipeline detects when an EC2 instance enters the **stopped state** and restarts it automatically if the instance has opted in through a tag.

## Workflow

1. EC2 emits a state change event when an instance stops.  
2. EventBridge captures the stopped state event.  
3. A second Lambda function checks for the `AutoRestart=true` tag.  
4. If the tag exists, the instance is automatically restarted.  
5. An SNS notification confirms the recovery action.

This ensures that **critical infrastructure cannot remain offline accidentally.**

---

## 🚀 Key DevOps Concepts Demonstrated

- Event-driven automation  
- Infrastructure monitoring  
- Self-healing infrastructure design  
- Automated remediation workflows  
- Infrastructure resilience engineering  

---

## 📂 Project Structure

```
aws-self-healing-infrastructure
│
├── architecture
│   └── self-healing-architecture.png
│
├── demo walkthrough
│   └── self-healing-monitoring-demo.mp4
│
├── documentation
│   └── Self-Healing-Webserver-Full-Documentation.pdf
│
├── lambda
│   ├── remediation_function.py
│   └── auto_restart_instance.py
│
├── policies
│   ├── lambda_ssm_policy.json
│   └── auto_restart_policy.json
│
├── eventbridge
│   ├── high_cpu_event_pattern.json
│   └── ec2_stopped_event_pattern.json
│
├── test-events
|   ├── cloudwatch_alarm_test_event.json
│   └── simulate-web-crashes.sh
|   
└── README.md
|
└── Startup-script.sh
```
--- 

## 🎬 Demo: Self-Healing in Action

The demonstration shows the system recovering from a real failure.

### Steps shown in the video

1. nginx service is intentionally stopped.  
2. CPU load is generated using `stress-ng`.  
3. CloudWatch detects the anomaly.  
4. EventBridge triggers the remediation Lambda.  
5. Lambda executes a restart command through Systems Manager.  
6. nginx automatically comes back online.  
7. A notification email confirms the remediation event.

## Video demonstration

![demo-walkthrough](https://drive.google.com/drive/folders/1HrXkiEz73MP4eMfnRpCZRkT3U08dT50p?usp=sharing)

---

## 📘 Full Documentation

A detailed step-by-step project walkthrough with screenshots is available in the PDF documentation.

```
/documentation/Self-Healing-DevOps-Infrastructure.pdf
```

## The documentation includes

- Architecture explanation 
- Screenshots for every configuration step 
- IAM roles and policies  
- Lambda function implementation  
- EventBridge event patterns  
- End-to-end testing process  
- Troubleshooting steps  
- Cleanup instructions  

---

## 🧠 Key Concepts Learned

Modern cloud infrastructure should be able to detect failures and recover automatically without human intervention.

This project demonstrates several real-world DevOps and cloud engineering concepts:

- Event-driven automation  
- Infrastructure monitoring and observability  
- Automated incident remediation  
- Serverless operational workflows  
- Remote command execution using Systems Manager  
- Infrastructure security with IAM roles  
- Tag-based infrastructure automation  
- Self Healing Systems

Instead of engineers manually restarting services, the system detects issues and resolves them autonomously.

---

## 🧹 Cleanup Reminder

If you deploy this project in your own AWS environment, remember to stop or terminate the EC2 instance when testing is complete to avoid unnecessary charges.

Most services used in this project remain within the free tier, but compute hours for EC2 instances may incur costs outside the free usage limits.

---

## 🚀 Future Improvement (Part 2)

This project can be extended into an **AI-powered DevOps assistant**.

The next stage introduces an **AI DevOps Copilot built with Amazon Bedrock**.

### Planned capabilities

- Collect CloudWatch alarm history  
- Analyze remediation logs  
- Inspect EC2 health status  
- Generate automated incident analysis using AI  
- Provide operational insights through an API  

The Copilot will analyze infrastructure events and explain what happened, why it happened, and what actions were taken automatically.

---

## 💭 Final Thoughts

This project demonstrates how event-driven architectures can transform infrastructure operations by enabling systems to detect failures, respond automatically, and maintain service availability with minimal human intervention.

It reflects how modern DevOps teams build resilient cloud systems that can monitor themselves, fix themselves, and notify operators when necessary.

---

## 🎓 What This Project Demonstrates

By completing this project, you learn how to design infrastructure that can:

- Detect operational failures
- Trigger automated responses
- Remediate services automatically
- Notify operators
- Maintain high system availability

This approach reflects **real-world DevOps reliability engineering practices used in production cloud environments.**

---

## 🧠 Author
Built by **Kareshma**, aspiring Cloud DevOps Engineer (DevOps, AI, AWS).  
Exploring how **cloud + AI** can power the next generation of intelligent apps.


# 📜 License

This project is for educational and demonstration purposes.
