# FastAPi app with nginx proxy configuration 
This project is a simple example of a Dockerized Python application with an Nginx reverse proxy.

# Getting Started
This project uses Docker and Docker Compose to manage and run the services. Make sure you have Docker and Docker Compose installed on your machine and SSH connection before proceeding.

# Building and Running the Project
The project can be built and run using the GitHub Actions workflow defined in .github/workflows/build-and-deploy.yml. This workflow builds the Docker images for the Python application and the Nginx server, pushes them to Docker Hub, and then deploys them to a remote server using SSH and Docker Compose.

# Services
The project consists of two main services:

api_app_1: This is a Python application built using the FastAPI framework. The Dockerfile for this service is located at api_app_1/Dockerfile.

nginx: This is an Nginx server that acts as a reverse proxy for the Python application. The Dockerfile for this service is located at nginx/Dockerfile.

# Environment Variables
The project uses several environment variables, which are defined in the GitHub Actions workflow file. These include 
- the Docker Hub username and password and the IP address and port of the application server
- SSH username and private key for the application server

# Example application
You can find the example application deployed with github action on: http://130.61.126.80/app1/api/#

# License
This project is licensed under the MIT License. See the LICENSE file for more details.