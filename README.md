# Automated Game Server

I built this project to solve a problem: I wanted to host a Terraria server for my friends, but I did not want to pay for a server that sits idle 90% of the time.

This architecture allows the server to run only when needed. It boots up instantly when we want to play and shuts itself down automatically when we are done, which reduces hosting costs by around 90%.

## How It Works

The system relies on three main parts to automate the server:

1. The Trigger (AWS Lambda):
I wrote a Python script using the Boto3 library that acts as like a start button. This script is hosted on AWS Lambda and exposed by a secure Function URL. When accessed, it checks the status of the EC2 instance and starts it if it is currently stopped.

2. The Server (EC2 & Docker):
The game runs on a t3.micro instance. I used Docker Compose to containerize the game server. This means that every time the server boots, the environment is identical, and I do not have to manually work with dependencies or updates. I also configured Linux swap memory to make sure that the game runs smoothly on the limited RAM of the free-tier instance.

3. The Safety (CloudWatch):
To keep from having to worry about accidental billing, I set up an AWS CloudWatch alarm. It monitors CPU usage in 15-minute intervals. If the CPU usage goes below 5% (meaning that no players are connected), the alarm triggers a "Stop Instance" action, putting the server to sleep.

## Skills Learned

- Cloud Provider: Amazon Web Services (AWS)
- Compute: EC2
- Containerization: Docker and Docker Compose
- Automation: AWS Lambda
- Monitoring: AWS CloudWatch Alarms
