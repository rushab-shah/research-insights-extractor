# Use a base image with Python and Node.js installed
FROM python:3.10.7-alpine AS python_builder

# Install build tools and dependencies for compiling native extensions
RUN apk add --no-cache build-base libffi-dev

WORKDIR /project/datasources
COPY datasources .

WORKDIR /project/output
COPY output .

WORKDIR /project/prompts
COPY prompts .

# Set the working directory in the container
WORKDIR /project/app

# Copy the entire project to the container
COPY app .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
RUN python parser.py


# Build the React app
FROM node:14.18.1-alpine AS react_builder

# Set the working directory to the React app
WORKDIR /project/UI

# Copy only the necessary files for installing Node.js dependencies
COPY UI/package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the React app
COPY UI .

# Build the React app
RUN npm run build


# Final image
FROM python:3.10.7-alpine

# Set the working directory in the container
WORKDIR /project

# Copy the Python app from the python_builder stage
COPY --from=python_builder /project /project

# Copy the built React app from the react_builder stage
COPY --from=react_builder /project/UI/build /project/UI/build

# Set the entrypoint command to start the React app
CMD ["npm", "start"]
