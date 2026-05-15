#Stop the nginx web server to simulate a crash by running:
sudo systemctl stop nginx

#Install stress-ng, a CPU load-testing tool, by running:
sudo dnf install -y stress-ng

#To avoid permission issues, change to the tmp directory:
cd /tmp

#Spike the CPU above 80% to trigger the CloudWatch alarm by running:
#creates two CPU-intensive worker processes that run for 5 minutes. 
stress-ng --cpu 2 --timeout 300

#stress-ng automatically stops after 5 minutes. You do not need to kill it manually.
