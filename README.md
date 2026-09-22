# Student Information Web Service

This project is a simple Client-Server web service built using Python. It consists of a REST API server built with Flask and a command-line client built with the `requests` library. The service allows users to retrieve information about students.

## Prerequisites

Before running the application, make sure you have Python installed and the required dependencies:

```bash
pip install flask requests
```

## Files

- `server.py`: A Flask web server that provides endpoints to access student data.
- `client.py`: A command-line client that connects to the server and retrieves information for a specific student.

## Running the Application

### 1. Start the Server
Open a terminal and run the Flask server:
```bash
python server.py
```
The server will start on `http://127.0.0.1:5000`.

### 2. Run the Client
Open a **new** terminal window and run the client script:
```bash
python client.py
```

### 3. Usage
The client will prompt you to enter a Student ID. 
- Enter a valid ID (e.g., `1`, `2`, `3`, `4`, `5`) to retrieve the corresponding student's details.
- Enter `q` to quit the client application.

## API Endpoints

The server provides the following endpoints:

- **`GET /students`**: Retrieve a list of all students.
- **`GET /students/<id>`**: Retrieve information for a specific student by their ID. Returns a `404` status code if the student is not found.

# Take Note
 **Only change the code logic look for "MODIFY HERE" and "DO NOT TOUCH BELOW"**
 **Just copy & paste the client side and server side code logic**
