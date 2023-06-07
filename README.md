# Research Insights Extractor

This repository contains code for an automated feature extraction system from medical literature. The program parses PDF files, specifically medical research papers, and utilizes the OpenAI GPT model to extract key features. These key features include, but are not limited to, conclusion, number of subjects, relative risk, length of follow-up etc. The output is generated in a structured JSON format.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or later.
* You have a Windows/Linux/Mac machine.
* You have API access to OpenAI's GPT-3 or GPT-3.5 Turbo model.

## Installation
1. Clone the repository

2. Navigate to the project directory

3. Set Up a Virtual Environment

    - Before installing the project dependencies, it's recommended to set up a virtual environment. This helps to keep the dependencies required by different projects separate from each other, and also aligns with best practices for Python development.

    - Here's how you can set up a virtual environment for this project:

    - Using venv (included in standard Python 3)

    - If you're using a standard installation of Python 3, you already have the `venv` module for creating virtual environments. Here's how you use it:

        1. Navigate to the project directory in your terminal.
        2. Create a new virtual environment named 'env' (or another name of your choosing) using the following command:
        
        ```bash
        python3 -m venv env

4. Install the required packages
    pip install -r requirements.txt


## Usage
1. Place your PDF files in the `datasources/raw-data` directory.
2. Run the `parser.py` script to parse the PDF and break it down into manageable chunks. This will also save the parsed text into a local text file.

    python parser.py

3. This script makes API calls to OpenAI's GPT model for each chunk of text and writes the result in the `output` directory.

