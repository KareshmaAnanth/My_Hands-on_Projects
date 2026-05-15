#This script runs automatically when your EC2 instance boots for the first time.

##!/bin/bash tells the instance to run this as a shell script.
#!/bin/bash

#sudo dnf install -y nginx installs the nginx web server using the Amazon Linux 2023 package manager.

sudo dnf install -y nginx

#sudo systemctl start nginx starts the web server immediately.

sudo systemctl start nginx

#sudo systemctl enable nginx ensures nginx restarts automatically if the instance reboots.

sudo systemctl enable nginx