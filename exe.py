import os
import subprocess

# Install dependencies
print("Installing dependencies...")
subprocess.run(["pip", "install", "-r", "packages.txt"])

# Build and run Docker containers
print("Building and running Docker containers...")
subprocess.run(["docker-compose", "up"])
