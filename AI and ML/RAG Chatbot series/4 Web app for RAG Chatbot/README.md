<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a Web App for your RAG Chatbot

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-rag-webapp)

**Author:** Kareshma Rajaananthapadmanaban  
**Email:** kareshma2909@gmail.com

---

## Building a RAG Chatbot with a Web Interface

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_oiuhgiuh)

---

## Introducing Today's Project!

In this project, I will demonstrate how to build a fully functional web app for my RAG chatbot. I’m doing this project to learn how to connect a frontend chat interface with an API-powered backend that uses Amazon Bedrock and a knowledge base in S3. This final step is about making the chatbot accessible, scalable, and user-friendly, while gaining hands-on skills in web development and AI integration.

### Tools and concepts

Services I used were Amazon Bedrock for model inference, AWS IAM for secure access, and FastAPI with Uvicorn to build and run the chatbot API. I also worked with dotenv to manage environment variables and integrated a web frontend to interact with the backend. Key concepts I learnt include Retrieval-Augmented Generation (RAG), separating frontend and backend layers, secure credential handling, and how enabling or disabling RAG changes chatbot behavior.

### Project reflection

This project took me approximately 2 hours and 30 minutes. The most challenging part was troubleshooting API integration and ensuring the chatbot responded correctly with and without RAG enabled. It was most rewarding to see the chatbot pull accurate answers from my knowledge base and experience the difference in responses when switching between general AI knowledge and RAG-based retrieval.

I did this project today to practice building with Amazon Bedrock and get hands-on with Retrieval-Augmented Generation concepts. My goal was to understand how different AWS services connect to create a working chatbot with a custom knowledge base. The project met my goals because I learned how to set up, test, and clean up the entire workflow while strengthening both my cloud and AI integration skills.

---

## Chatbot setup

I created a Knowledge Base to give my RAG chatbot a structured way to store, organize, and retrieve information from my documents in S3. This is important because without a Knowledge Base, the chatbot wouldn’t know how to process or search through the data. By using embeddings and a vector store in Bedrock, my chatbot can understand context, match questions to relevant content, and deliver accurate, meaningful answers.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_c1d2e3f4)

---

## Setting Up the API

To run the API, I had to install requirements like fastapi, uvicorn, boto3, and python-dotenv. These packages are important because FastAPI builds the API itself, Uvicorn runs the server so my API is accessible, Boto3 connects my app to AWS Bedrock, and python-dotenv loads environment variables securely. Together, they make my chatbot’s backend run smoothly and talk to AWS.

A virtual environment helps me by keeping all the Python dependencies for this project isolated from my global setup. This means any libraries I install for the web app won’t affect other projects on my computer. It also makes the project more portable and reproducible, since I can recreate the same environment anywhere. For this RAG chatbot web app, it ensures clean, conflict-free package management.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_a8b9c0d1)

---

## Breaking down the API

In our web app, we need an API because it acts as the bridge between the frontend chat interface and the backend logic that talks to Amazon Bedrock. The frontend alone can’t process or fetch answers it just displays them. The API handles requests from the user, connects to Bedrock, processes responses, and then sends them back to the frontend for display.

Digging deeper into the API code, the main tools we need to import are FastAPI, boto3, os, and load_dotenv. These tools help us by letting us build the API quickly (FastAPI), connect to AWS services like Bedrock (boto3), securely access environment variables (os), and load them from a file (load_dotenv) without hardcoding sensitive information.

The environment variables we need are AWS_REGION, KNOWLEDGE_BASE_ID, and MODEL_ARN. We store them separately because they contain sensitive information like credentials and IDs. Keeping them in a separate .env file protects this information from being exposed in our code or accidentally pushed to GitHub.

My API uses the Python AWS SDK to connect to Bedrock from within the code. The difference between the AWS CLI and an SDK is that the CLI is a command-line tool for manual tasks, while an SDK is a library for building applications that programmatically interact with AWS services. SDKs allow seamless integration into code, unlike the CLI.

Our API has two main routes: / is the root route that returns a welcome message, and /bedrock/query is where users send questions to the chatbot. In general, routes help us define paths in the API that perform specific functions, making it possible for different endpoints to handle different types of requests.

---

## Testing the API

When I visited the root endpoint, I saw `{"message": "Welcome to your RAG chatbot API"}`. This confirms that my API server is running correctly and responding to requests from the browser, which means the backend setup is working as expected.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_i6j7k8l9)

---

## Troubleshooting the API

### My second endpoint had errors!

To fix the Parameter Failed error, I had to create a .env file in my project directory and add the correct environment variables: AWS_REGION, KNOWLEDGE_BASE_ID, and MODEL_ARN. Doing this helps because it ensures the API knows which AWS region, Knowledge Base, and AI model to use, preventing invalid parameter errors when querying Bedrock.

To fix the credentials error, I ran aws configure in my terminal and entered my IAM user's Access Key ID, Secret Access Key, and the correct AWS region (us-east-2). This was necessary because the AWS CLI needs these credentials to authenticate my terminal commands and allow my API to communicate securely with Bedrock.

My chatbot initially failed to generate responses, so I made sure I had requested access to the Titan Text Embeddings V2 and Llama 3.3 70B Instruct models in Bedrock, then synced my Knowledge Base with the S3 bucket containing my documents. This should help the AI properly process my data and generate accurate, meaningful answers.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_s9t0u1v2)

---

## Running the Web App

The difference between the API and the web app for the user is how they interact with the chatbot. The API gives raw JSON responses when you hit endpoints like /bedrock/query, which is useful for testing and backend integration. The web app, on the other hand, provides a full chat interface in the browser where users can type questions and see responses in a conversational format.

The web app has the ability to switch between using RAG with my Knowledge Base and talking directly to the AI model. When I asked the same question, “Who is NextWork?”, with RAG enabled it gave me a grounded answer based on my documents. When I checked “Talk to AI directly,” the response came only from the model’s general knowledge, which was less accurate.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_v1w2x3y4)

---

## Breaking down the Web App

When a user sends a chat message, the frontend JavaScript captures the text and sends it as a GET request to the /bedrock/query endpoint. The backend (web_app.py) receives the request, queries the Knowledge Base via Bedrock, and generates a response. That response is sent back to the frontend, where the JavaScript displays both the user’s message and the chatbot’s reply in the chat window.

web_app.py extends the API by adding a full web interface on top of the core backend in main.py. It serves HTML pages, CSS, and JavaScript via FastAPI, uses Jinja2 templates to dynamically render pages, configures logging for debugging, and introduces a new endpoint (/bedrock/invoke) that lets the AI model respond directly, bypassing the Knowledge Base.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_i5j6k7l8)

---

## Customizing the Frontend

I want to experiment with customizing the frontend because it gives me the freedom to design a chatbot interface that feels more engaging and unique, instead of being stuck with a default look. This is possible because as long as the API endpoints stay the same, the backend doesn’t care how the frontend looks it just sends and receives data. That separation lets me play with design while keeping the functionality intact.


My customized interface now features a clean, modern dark theme with two distinct panels. On the left, there’s a profile-style card showing my name, a toggle to switch between /bedrock/invoke and /bedrock/query, quick prompt buttons, and a status section. On the right, the chat assistant panel feels more polished, with a neatly styled conversation area, an input box, and a bright send button. It looks like a professional dashboard rather than a plain chat box.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-webapp_cust24680)

---

---
