# Research Insights Extractor

This repository contains code for an automated feature extraction system from medical literature. The program parses PDF files, specifically medical research papers, and utilizes the OpenAI GPT model to extract key features. These key features include, but are not limited to, conclusion, number of subjects, relative risk, length of follow-up etc. The output is generated in a structured JSON format.


## Prerequisites

- Git: The application is maintained and developed using GitHub. A GitHub account & Git installation is required on your desktop. If you don't already have Git installed on your system, you can download it [here](https://git-scm.com/downloads) and install it.
- Docker: The application is containerized using Docker, and requires Docker to be installed to run. You can download Docker [here](https://www.docker.com/products/docker-desktop)

## Installation & Usage

1) **Check Git Installation:** Make sure Git is installed and running on your system. You can do this by running the command git --version in the terminal/command prompt. If Git is installed correctly, it should display the version.

2) **Clone Repository:** Once Git is installed, navigate to the directory where you want to clone the repository, then run the following command:
```bash
git clone https://github.com/rushab-shah/research-insights-extractor.git
```

3) **Navigate to Project Directory:** After cloning the repository, navigate into the project directory using the following command:
```bash
cd research-insights-extractor
```

1) **Install Docker Desktop**: Docker is used to build and run the containerized application. You can download it [here](https://www.docker.com/products/docker-desktop) and install it.

2) **Check Docker Installation**: Make sure Docker is installed and running on your system. You can do this by running the command `docker -v` in the terminal/command prompt. If Docker is installed correctly, it should display the version.

3) **Build Docker Image**: Navigate to the project directory from the terminal and run the following command to build the Docker image:

```bash
docker build -t research-analysis:latest .
```

4) **Run Docker Container**: After the Docker image has been built, you can start the Docker container using the following command:

```bash
docker run -p <port>:3000 research-analysis:latest
```
Replace <port> with the port number where you want to host the application

**Wait for Data Processing**: Please note that starting the Docker container can take up to 20-30 minutes, as when the application starts, it builds the database of features by analyzing the input files one by one. You will see a progress bar in the terminal window. Once the progress is complete, all features have been extracted and the UI will start.

**Access the Application**: Once the UI is up, you can access the application by opening a web browser and navigating to localhost:`<port>` where `<port>` is the port number you chose when starting the Docker container.

Explore key features extracted from medical research papers!

## Project Structure
The project has been organized into a number of directories and files. A brief description is as follows:

- `/app`: This is where the application backend code resides. It consists of Python code for reading, parsing, and analysing PDF files
- `/UI`: This directory contains the React frontend of the application. The UI is responsible for displaying the end result to the user.
- `/datasources`: This directory contains the input PDF files in raw-data. It also consists of parsed and preprocessed PDF text data in processed-data.
- `/output`: This directory stores the output.json generated by our backend code that consists of all the extracted features. It also consists of error logs. This data is purely for debugging purposes.
- `/prompts`: This directory contains the prompt needed to query GPT via REST APIs.
- `dockerfile`: This file is used to create a Docker image of the application.

## Interpreting the output
The output of the analysis will be a structured JSON file where each research paper corresponds to a JSON object with key features extracted. This is turned is presented in a user friendly manner on the UI.

## Approach
This system uses a combination of text extraction from PDF files, natural language processing & feature extraction with OpenAI's GPT to generate a structured output from medical research papers. The frontend is built with ReactJS and Material-UI, while the backend is Python based, all packaged within Docker for easy deployment. Let's talk about the approach in detail:

### Input
The input is a set of PDFs stored in the datasources/raw-data folder of our project.

### Steps
**Reading the Input & Preprocessing:**

- Read the PDF files
- Capture snapshots of each file and store them in the online image store, cloudinary for usage in UI via REST endpoints
- Parse each PDF file and divide the text data into chunks
- Store this data as a dictionary of pdf file and its list of chunks

**Extracting features & Caching:**

- For each PDF file we first identify if we've already stored its feature data in the online JSON database
- If yes, we don't process it further and simply reuse the existing feature data
- If no, then we proceed to make a REST API call to OpenAI GPT API, with help of a custom fine tuned prompt to extract features from the specific chunk of PDF text data.
- This prompt is designed to give output strictly in JSON format and only with feature data.
- We combine features observed in each chunk and assign all features to the respective PDF file
- Once this process is completed for all PDF files, we store the data in the JSON online store JSON Bin using REST endpoints.

**Presenting the data:**

- Once the backend tasks are done, the UI app is started
- The UI upon startup, loads the JSON feature data from JSON bin
- Then it displays each PDF file as a card in the UI
- Each card has the thumbnail of the PDF snapshot that we stored using the Python backend earlier which is loaded from cloudinary
- Each PDF card is clickable. Upon clicking a modal dialogue opens up showing a list of key features extracted from the PDF.


## Scope for Improvement
The system currently has a few limitations that can be improved upon in future iterations:

- Handling of complex PDF layouts: Some research papers may have complex layouts which could affect the feature extraction.
- Improve the speed of feature extraction: The extraction process can be made faster with optimized algorithms or parallel processing.
- Expanding the set of features: The set of key features extracted can be expanded based on requirements.
