<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Deploy an App Across Accounts

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-compute-ecr)
**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)

**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

---

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-ecr_3e91948719)

---

## Introducing Today's Project!

In this special multiplayer project, I’m working with a buddy to deploy an app across AWS accounts. Together, we’ll build Docker images, store them in Amazon ECR, share them securely, and launch each other's apps. This helps us learn cross-account deployments, a real-world AWS practice.

### What is Amazon ECR?

Amazon ECR (Elastic Container Registry) is a fully managed Docker container registry that makes it easy to store, manage, and deploy container images. In this project, I used Amazon ECR to push my Docker image, store it securely, and share it with Player B for cross-account deployment.

### One thing I didn't expect...

One thing I didn’t expect in this project was getting a JSON policy syntax error while editing the ECR repository policy, which reminded me how even a small comma or bracket mistake can break AWS permissions setup and block image pulling or deployment.

### This project took me...

This project took me around 2 hours and 15 minutes to complete, along with a few extra minutes to finish the secret mission involving Elastic Beanstalk deployment and permissions setup.

---

## Creating a Docker Image

I set up a Dockerfile and an index.html file. Both files are needed because the Dockerfile defines the container setup using Nginx, while the index.html file contains the custom web content that will be served when the container runs. Together, they build a functional Docker image for deployment.

My Dockerfile tells Docker to use the latest Nginx image as the base and copy my custom index.html file into the Nginx default directory, so that when the container runs, it serves my personalized web page.


### I also set up an ECR repository

ECR stands for Elastic Continer Registry. It is important because it provides a secure, scalable, and fully managed location to store Docker container images, enabling smooth sharing and deployment of containerized applications across different AWS environments.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-ecr_e7f8g9h0)

---

## Set Up AWS CLI Access

### AWS CLI can let me run ECR commands

AWS CLI is a command line tool that allows me to manage AWS services directly from my terminal without using the AWS Management Console. The CLI asked for my credentials because it needs an access key and secret key to authenticate my AWS identity. Unlike the console, the CLI requires explicit credentials to perform actions like pushing images to ECR.

To enable CLI access, I set up a new IAM user with the permission policy AmazonEC2ContainerRegistryFullAccess. I also set up an access key for this user, which means I can securely authenticate and perform ECR actions like pushing Docker images from my terminal. I downloaded the .csv file to safely store the access credentials.

To pass my credentials to the AWS CLI, I ran the command `aws configure`. I had to provide the Access Key ID, Secret Access Key from the downloaded .csv file, the AWS region code where my ECR repository is set up, and left the output format blank to use the default JSON format for terminal responses.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-ecr_4aa3e4fe6)

---

## Pushing My Image to ECR

Push commands are instructions used to authenticate Docker with Amazon ECR and upload container images from my local machine to an ECR repository. These commands connect my terminal to AWS, allowing Docker to push or pull images securely from the specified ECR repository.

### There are three main push commands

To authenticate Docker with my ECR repo, I used the command `aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 390403861404.dkr.ecr.ap-south-1.amazonaws.com`. This command logs Docker into my ECR registry, enabling me to push and pull images securely.

To push my Docker image to ECR, I ran the command:
`docker push 390403864104.dkr.ecr.ap-south-1.amazonaws.com/crossdeploy:latest`. 
This command uploaded my tagged Docker image to my ECR repository, making it available for pulling and deployment by other AWS accounts, like my project buddy's.

When I built my image, I tagged it with the label `latest`. This means the image represents the most recent version of my application. Using the `latest` tag helps me and others easily pull the newest build from ECR without specifying a version number, ensuring the most up-to-date container is deployed.

---

## Resolving Permission Issues

When I tried pulling my project buddy's container image for the first time, I saw the error "403 Forbidden." This was because Amazon ECR repositories are private by default, and my buddy hadn’t granted me pull permissions yet. Without the correct permissions, Docker cannot access or pull images from another account’s ECR repository.

To resolve each other's permission errors, my buddy and I updated our ECR repository policies by adding each other’s IAM user ARNs to the policy JSON. This granted the required permissions to pull container images from our private repositories, enabling successful cross-account image sharing and deployment.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-ecr_74b90da414)

---

## Deploying the App

I used Elastic Beanstalk to deploy Player B’s Docker container image in a managed AWS environment. When I set up an Elastic Beanstalk application, I configured settings like the platform (Docker), instance type, storage, public IP, IAM roles for ECR access, and deployment policies. This made it easy to run Player B's app without managing the underlying servers manually.

While setting up for deployment, I created a new role for EC2 instances named ecrInstanceRole. The role has the permission to pull container images from Amazon ECR using the AmazonEC2ContainerRegistryReadOnly policy. I gave Elastic Beanstalk access to ECR too by attaching the same policy to its service role for pulling the image during deployment.

The Dockerrun.aws.json file is a configuration file used by Elastic Beanstalk to know how to deploy a Docker container image from a registry like Amazon ECR. My file tells Elastic Beanstalk to pull Player B’s latest Docker image from ECR, update to the newest version on each deployment, and expose port 80 to allow web traffic into the running container.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-ecr_70ed85fa3)

---

## Resolving Deployment Issues

When I visited my environment's domain, I initially saw the error "This site can't be reached." This was because the Elastic Beanstalk environment and EC2 instance didn’t have permission to pull the Docker image from Player B’s ECR repository. Updating the ECR repository policy with both role ARNs fixed this access issue.

To fix the permissions error, my buddy and I updated our ECR repository policies by adding each other's ecrInstanceRole and aws-elasticbeanstalk-service-role ARNs to the policy JSON. My ECR repository's existing permission settings didn't work because they didn’t allow Elastic Beanstalk or EC2 instances to pull images during environment setup and scaling.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-ecr_74b90da411)

---

---
