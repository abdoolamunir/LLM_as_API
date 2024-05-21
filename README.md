# LLM as API with FastAPI and Streamlit

This project demonstrates how to build a Language Model (LLM) as an API using FastAPI and Streamlit. The project uses LangChain to integrate with OpenAI's GPT-3.5-turbo and the Ollama model, providing endpoints for generating text descriptions and haikus.

## Features

- **OpenAI Integration**: Generate short descriptions using OpenAI's GPT-3.5-turbo.
- **Ollama Integration**: Generate haikus using the Ollama model.
- **API Endpoints**: Expose models as RESTful APIs.
- **Streamlit Interface**: Interactive web interface to interact with the models.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
```

### 2.Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```
### 4. Create a .env File
Create a .env file in the project directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Application
### Start the FastAPI Server
Run the FastAPI application:
```bash
uvicorn app:app --reload
```
The server wil be available at http://localhost:8000.

### Start the Streamlit Client
Run the Streamlit application:
```bash
streamlit run client.py
```

### Project Structure
- app.py: The main FastAPI application file that sets up the API endpoints and integrates with LangChain models.
- client.py: The Streamlit client application that interacts with the FastAPI endpoints.
- requirements.txt: A file containing all the dependencies required to run the application.
- .env: Environment file containing the OpenAI API key.

### Usage
1. Open the Streamlit Interface: Navigate to http://localhost:8501 in your browser.
2. Enter Text: Use the input fields to enter a topic for description or haiku.
3.  View Responses: Click "Enter" to generate and view the responses from the models.

### Endpoints
- OpenAI Description Endpoint: POST /prompt1
    - Request Body: { "input": { "topic": "your_topic_here" } }
    - Response: { "description": "Generated description" }
- Ollama Haiku Endpoint: POST /prompt2
    - Request Body: { "input": { "topic": "your_topic_here" } }
    - Response: { "description": "Generated haiku" }

### Notes
This is a basic example, for more advanced features and customizations, refer to the official documentation of LangChain, OpenAI and Ollama

### Contributing 
Contributions are welcome! Pleasee open an issue or submit a pull request for any improvements or bug fixes!
