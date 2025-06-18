## Project Title
  Implement a web server using python


## OBJECTIVE
  Web Server: Create a simple web application using Python (Flask/Django) or Node.js (Express or Nest.Js).

  Dockerization: Dockerize the web application to ensure consistency across different environments.

  Deployment on any cloud platform : AWS, Azure and Google Cloud Platform.

  CI/CD Implementation: Implement a Continuous Integration/Continuous Deployment (CI/CD) pipeline for the project. Use a CI/CD tool of your choice to automate the deployment process.



## Overview
  1. Web Server
    created a Flask-based to-do application, which is a lightweight Python web server that handles routes like adding, viewing, and deleting tasks.


  2. Dockerization
    wrote a Dockerfile that packages the Flask app and its dependencies into a Docker container. This ensures the app runs consistently across all environments.


  3. Deployment on Cloud Platform (AWS EC2)
    used an AWS EC2 instance to:
    Install Docker
    Pull your app’s image from Docker Hub
    Run the container and expose it to the internet via EC2’s public IP


  4. CI/CD Pipeline
    configured a GitHub Actions workflow that:
    Builds your app into a Docker image on every push to the main branch
    Pushes the image to Docker Hub
    This automates the integration and delivery of updated code.