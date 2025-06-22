<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Deploy an App with Docker

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-compute-eb)
**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)


**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

---

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-eb_c4df13c84)

---

## Introducing Today's Project!

### What is Docker?

Docker is a tool that lets you package applications and their dependencies into lightweight containers, ensuring they run consistently across environments. In this project, I used Docker to create a custom image with Nginx serving my HTML file. I built the image, ran it locally, and deployed it on AWS Elastic Beanstalk to make my web app publicly accessible.

### One thing I didn't expect...

One thing I didn’t expect was the error caused by my Dockerfile being saved as **Dockerfile.txt** by default. I fixed it by renaming it properly. Later during Elastic Beanstalk deployment, my default VPC’s Internet Gateway got detached, causing the launch to fail. After reattaching the IGW to the VPC, the deployment worked perfectly, and the app was successfully hosted!

### This project took me...

This project took me 2 hours to complete, plus an additional 30 minutes for writing and organizing the documentation to ensure everything was clear, well-documented, and reusable for future reference.


---

## Understanding Containers and Docker

### Containers

Containers are lightweight, standalone units that package an application with all its dependencies, libraries, and configuration files. They are useful because they allow the app to run consistently across different environments, from  local machines to cloud platforms like AWS reducing the issues caused by differences in environments.

A container image is a compact, self sufficient file that includes everything needed to run an application—code, libraries, dependencies, and configurations. It serves as a blueprint for creating containers, ensuring the app runs consistently across different environments.


### Docker

Docker is an open-source platform that enables me to build, run, and manage containers easily. Docker Desktop is its user-friendly application for Windows, Mac, and Linux that lets me create and handle containers locally through a graphical interface or command line.

The Docker daemon is a background process that manages Docker containers on my system. It listens to Docker commands from the client and handles tasks like building, running, and distributing containers. Without the daemon, Docker commands wouldn’t function.

---

## Running an Nginx Image

Nginx is a powerful, high-performance web server used to deliver web pages to users. It’s also commonly used as a reverse proxy to forward requests to other servers, helping to manage heavy web traffic efficiently. Its speed and scalability make it popular in modern web apps.

The command I ran to start a new container was `docker run -d -p 80:80 nginx`. This command runs the Nginx container in detached mode and maps port 80 of my local machine to port 80 inside the container, allowing me to access the Nginx welcome page via my browser.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-eb_6245f5bb10)

---

## Creating a Custom Image

The Dockerfile is a text file that contains a set of instructions Docker uses to build a custom image. In this case, it starts from the latest Nginx image, copies my local index.html file into the container’s web directory, and exposes port 80 for web traffic.

My Dockerfile tells Docker three things: first, to use the latest Nginx image as the base; second, to copy my local index.html file into the Nginx HTML directory; and third, to expose port 80 so the container can serve the webpage when accessed through the browser.

The command I used to build a custom image with my Dockerfile was "docker build -t my-web-app ." The `.` at the end of the command means Docker should look for the Dockerfile and other files needed to build the image in the current directory.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-eb_4c741d1913)

---

## Running My Custom Image

There was an error when I ran my custom image because port 80 was already in use by the Nginx container I started earlier. I resolved this by stopping the running Nginx container. Later, I also found my Dockerfile was mistakenly saved as a `.txt` file on Windows. I renamed it using `rename Dockerfile.txt Dockerfile`, rebuilt the image, and the error was gone.


In this example, the container image is my-web-app, which includes the Nginx base image and my custom index.html file. The container is the running instance of this image that serves the webpage when I visit http://localhost in my browser.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-eb_74b5c3d619)

---

## Elastic Beanstalk

Elastic Beanstalk is an AWS service that simplifies deploying and managing applications in the cloud. It handles server provisioning, load balancing, auto-scaling, and health monitoring automatically. I can deploy web apps or services without worrying about the underlying infrastructure, making it ideal for developers to focus purely on coding and app logic.

Deploying my custom image with Elastic Beanstalk took me around a few minutes. The environment creation and deployment process required some waiting time as AWS set up resources like EC2, storage, and networking. Once complete, I was able to access my updated webpage live through the provided domain link, confirming a successful deployment!

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-eb_26d5573b23)

---

## Deploying App Updates

To learn how to deploy app updates with Elastic Beanstalk, I updated my app by adding a new heading, a motivational quote, and an anime-style image below the main title in my index.html file. I verified those changes by opening the file in my browser to ensure the new text and image appeared correctly.


My app updates didn’t show up in my live environment immediately because Elastic Beanstalk needs the updated ZIP file to redeploy. To deploy my changes, I only had to delete the old ZIP, create a new one with my updated index.html and Dockerfile, upload it in Elastic Beanstalk as Version Two, and hit Deploy.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-eb_5b7034684)

---

---
