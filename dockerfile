# Use a base image with Python installed
FROM python:3.10.7-alpine AS python_builder

# Install build tools and dependencies for compiling native extensions
RUN apk add --no-cache build-base libffi-dev

# Set the working directory in the container
WORKDIR /project/app

# Copy the entire project to the container
COPY ./app .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y poppler-utils

# ---- #

# Use a base image with Node.js installed
FROM node:14.18.1-alpine AS react_builder

# Set the working directory to the React app
WORKDIR /project/UI

# Copy only the necessary files for installing Node.js dependencies
COPY ./UI/package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the React app
COPY ./UI .

# Build the React app
# RUN npm run build

# ---- #

# Final image
FROM python:3.10.7-alpine

# Install Node.js
RUN apk add --update nodejs npm

# Set Python's site-packages folder from python_builder image as the one in the final image
COPY --from=python_builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the Python app from the python_builder stage
COPY --from=python_builder /project/app /project/app

# Copy the built React app from the react_builder stage
COPY --from=react_builder /project/UI/ /project/UI/

# Copy other necessary directories
COPY ./datasources /project/datasources
COPY ./output /project/output
COPY ./prompts /project/prompts

# Set the working directory in the container
WORKDIR /project

# Set the entrypoint command to start the Python script and then the React app
CMD ["sh", "-c", "cd app && python -u parser.py && cd /project/UI && npm start"]
