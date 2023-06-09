# Research Insights Extractor

This repository contains code for an automated feature extraction system from medical literature. The program parses PDF files, specifically medical research papers, and utilizes the OpenAI GPT model to extract key features. These key features include, but are not limited to, conclusion, number of subjects, relative risk, length of follow-up etc. The output is generated in a structured JSON format.

## Prerequisites

- Docker: The application is containerized using Docker, and requires Docker to be installed to run. You can download Docker [here](https://www.docker.com/products/docker-desktop).

## Installation & Usage

1) **Install Docker Desktop**: Docker is used to build and run the containerized application. You can download it [here](https://www.docker.com/products/docker-desktop) and install it.

2) **Check Docker Installation**: Make sure Docker is installed and running on your system. You can do this by running the command `docker -v` in the terminal/command prompt. If Docker is installed correctly, it should display the version.

3) **Build Docker Image**: Navigate to the project directory from the terminal and run the following command to build the Docker image:

```bash
docker build -t research-analysis:latest .

4) **Run Docker Container**: After the Docker image has been built, you can start the Docker container using the following command:

```bash
docker run -p <port>:3000 research-analysis:latest

Replace <port> with the port number where you want to host the application.

5) **Wait for Data Processing**: Please note that starting the Docker container can take up to 20-30 minutes, as when the application starts, it builds the database of features by analyzing the input files one by one. You will see a progress bar in the terminal window. Once the progress is complete, all features have been extracted and the UI will start.

6) **Access the Application**: Once the UI is up, you can access the application by opening a web browser and navigating to localhost:<port> where <port> is the port number you chose when starting the Docker container.

7) Exploring key features extracted from medical research papers!