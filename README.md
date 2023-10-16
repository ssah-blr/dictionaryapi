PipeLine to build docker Image for Python Webapp, which call https://dictionaryapi.com/products/api-collegiate-dictionary

Components -
1) Jenkins Pipepine to build Docker Image
2) Python Script which Works as a WebApp and utilises https://dictionaryapi.com/ API
3) Docker build to use Python Script


Example -
Example Docker Image - https://hub.docker.com/r/ssahblr/app2
How to use -
```
> docker pull ssahblr/app2
> docker run -p 5500:5500 ssahblr/app2:latest <dictionaryapi.com-API-KEY>
 * Serving Flask app 'dictionary'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5500
 * Running on http://172.17.0.2:5500
Press CTRL+C to quit
172.17.0.1 - - [16/Oct/2023 06:46:42] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [16/Oct/2023 06:46:48] "POST /home HTTP/1.1" 200 -
172.17.0.1 - - [16/Oct/2023 06:46:49] "POST /reset?type=resetme HTTP/1.1" 200 -
172.17.0.1 - - [16/Oct/2023 06:46:52] "POST /home HTTP/1.1" 200 -
```

Background

To build an automation pipeline for a web-based API that queries another API, runs a Python and Flask script in a Docker container, and pushes the resultant Docker image to Docker Hub as an artifact using Jenkins, you can follow these steps. This requires a basic understanding of Jenkins and Docker:

1. Set Up Your Environment:
    Ensure you have the necessary tools and services in place:

    Jenkins server installed and running.
    Docker installed on the Jenkins server.
    A code repository (e.g., Git) where your Python and Flask script and Jenkinsfile are stored.

2. Create a Dockerfile:
    In your code repository, create a Dockerfile to define how your Python and Flask application should run in a Docker container. Here's a basic example of a Dockerfile for a Python/Flask application:
    [Dockerfile](scripts/Dockerfile)

3. Create a Jenkinsfile:
    Create a Jenkinsfile in your code repository. This file defines your CI/CD pipeline. Here's an example pipeline script:
    [Jenkinsfile](Jenkinsfile)

    Note: Please update - Jenkins credentials, Docker image Name and Tag.

4. Configure Jenkins:

    Install the Docker plugin for Jenkins.
    Configure Jenkins to use the credentials for Docker Hub (you need to create these credentials in Jenkins).
    Create a Jenkins pipeline job and configure it to use the Jenkinsfile from your code repository.

5. Set Up Webhook or Polling:
    Configure the Jenkins job to be triggered either through a webhook (if your SCM supports it) or by polling your code repository for changes.

6. Run the Pipeline:
    Make a change in your code repository to trigger the Jenkins job, which will then:

    Build the Docker image using the Dockerfile.
    Push the Docker image to Docker Hub using the specified credentials.

7. Test and Deploy:
    After pushing the Docker image to Docker Hub, you can deploy the containerized application to your target environment, such as a Kubernetes cluster or a Docker Swarm.


This pipeline automates the process of building the Docker image, pushing it to Docker Hub, and can be extended to include further stages like automated testing and deployment.

Make sure to replace 'your-image-name:tag' with your actual image name and tag in the Jenkinsfile. Also, ensure you have the necessary permissions and settings in Docker Hub and Jenkins for this pipeline to work seamlessly.