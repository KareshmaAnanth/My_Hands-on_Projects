<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Create an API for Your RAG Chatbot

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-rag-api)

**Author:** Kareshma Rajaananthapadmanaban  
**Email:** kareshma2909@gmail.com

---

## How I Built an API for My RAG Chatbot

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_r4s5t6u7)

---

## Introducing Today's Project!

In this project, I will demonstrate how to turn my RAG chatbot into an API that any application can access. I'm doing this project to learn how to connect Amazon Bedrock with FastAPI so my chatbot isn’t limited to the console or terminal. This way, I can make it production-ready and integrate it into websites, apps, or even other tools.

### Tools and concepts

Services I used were Amazon Bedrock for calling foundation models, FastAPI for building API endpoints, and dotenv for managing environment variables. Key concepts I learnt include the difference between MODEL_ID and MODEL_ARN, how to extend an API with new endpoints, handling environment variables, and the contrast between direct model invocation and Knowledge Base queries.

### Project reflection

This project took me approximately 2 hours to complete. The most challenging part was troubleshooting the missing MODEL\_ID environment variable for the new endpoint. It was most rewarding to see the chatbot handle both Knowledge Base queries and direct AI model questions, giving me flexibility to use specialized or general knowledge.

I did this project today to deepen my hands-on understanding of how Retrieval-Augmented Generation works in AWS Bedrock and to practice extending APIs for both document-based and general AI queries. This project met my goals because I now feel more confident in configuring endpoints, managing environment variables, and explaining the difference between Knowledge Base and direct model calls.

---

## Setting Up The Knowledge Base

To set up my Knowledge Base, I used S3 to store the reference documents my chatbot will learn from. The documents I uploaded contain information about the NextWork project documentation, including project steps, outcomes, and skills. S3 acts as the central storage location, making it easy for Bedrock to retrieve and process this data securely for my chatbot.

Amazon Bedrock is an AWS service for building generative AI applications. I created a Knowledge Base in Bedrock to store and organize my chatbot’s information, enabling it to quickly find and answer questions from my S3 documents. This setup gives my chatbot a structured “brain” that understands the meaning of the text, not just exact keywords.

My chatbot also needs access to two AI models to process text and generate human-like responses. I then synchronized my Knowledge Base with my S3 data because this ensures the chatbot can read, understand, and store the documents in the vector database, allowing it to answer questions accurately.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_1u2v3w4x)

---

## Running CLI Commands Locally

When I ran a Bedrock command in my terminal, I initially got an error because AWS CLI wasn’t installed. To resolve this, I downloaded and installed the AWS CLI for my operating system, then verified the installation with aws --version. Once I saw the version number, I knew the CLI was set up correctly and ready to connect with my Knowledge Base.

I set up AWS access keys to let my local terminal securely connect to AWS and run Bedrock CLI commands. Since the CLI doesn’t share authentication with the AWS Management Console, the keys act like a username and password pair. This way, I could test my Knowledge Base queries locally, validate responses faster, and prepare my environment before building the API.

To pass my access key credentials to the AWS CLI, I ran the command aws configure. I had to provide my Access Key ID, Secret Access Key, and set the region to us-east-2 where my Knowledge Base is hosted. For the default output format, I left it empty. This allowed my terminal to securely connect to AWS services like Bedrock.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_9w0x1y2z)

---

## Running Bedrock Commands

When I first ran a Bedrock command, I ran into an error because I needed to provide values for the Knowledge Base ID and the Model ARN. Without these identifiers, Bedrock didn’t know which Knowledge Base to query or which AI model to use, so the command couldn’t process my request and returned a validation error.

To find the required values, I had to first locate my Knowledge Base ID in the Bedrock console and then retrieve my model ARN using the CLI with the model identifier meta.llama3-3-70b-instruct-v1:0. The Bedrock command ran successfully and showed me a context-rich answer from my chatbot, confirming that my Knowledge Base was correctly linked to the AI model and ready to respond to queries from the terminal.

---

## Creating an API

An API is an Application Programming Interface that lets different software communicate with each other. The API I'm creating will let any application send questions to my RAG chatbot and receive responses, without needing to access the AWS Console or CLI. This will be helpful for integrating the chatbot into websites, mobile apps, or other tools, making it accessible and interactive for users everywhere.

The API code has three main sections that work together to make the chatbot accessible. First, Imports bring in necessary libraries like FastAPI for the API framework, boto3 for AWS interactions, and dotenv/os for environment variables. Second, Environment Variables load your AWS region, Knowledge Base ID, and model ARN to connect the API to Bedrock. Third, Functions and API Endpoints define routes like the root page and /bedrock/query to handle requests and send them to the chatbot.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_w7x8y9z0)

---

## Installing Packages

To run the API, I had to install requirements like fastapi, uvicorn, boto3, and python-dotenv. These packages are important because FastAPI provides the framework for building the API, Uvicorn runs the API server and handles requests, Boto3 connects the API to AWS Bedrock, and python-dotenv loads environment variables so the API can access the Knowledge Base ID, model ARN, and region.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_a8b9c0d1)

---

## Testing the API

When I visited the root endpoint, I saw {"message": "Welcome to your RAG chatbot API"}. This confirms that the API server is running correctly, the FastAPI framework is handling requests, and the root endpoint is working as expected, meaning my local setup is ready to process further chatbot queries through the API.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_i6j7k8l9)

---

## The Query Endpoint

The query endpoint connects an app with my Bedrock Knowledge Base and AI model. I tested the query endpoint by visiting http://127.0.0.1:8000/bedrock/query?text=What%20is%20NextWork in my browser. The response was a clear, human-like answer generated from my Knowledge Base documents, confirming that the API correctly processes queries and communicates with the chatbot.

Looking at the API code, I can see that the API calls for environment variables because it uses os to load KNOWLEDGE_BASE_ID and MODEL_ARN instead of hardcoding them. To resolve the error in my query endpoint, I need to set these values as environment variables on my computer or in a .env file so the API can read them securely when sending requests to Bedrock.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_r4s5t6u7)

---

## Extending the API

In a project extension, I decided to extend my API by adding a new endpoint that calls the AI model directly, bypassing the Knowledge Base. Changes to the API code include two new imports—logging and json for better error tracking and handling JSON data, an additional environment variable MODEL\_ID for direct model calls, and a new endpoint /bedrock/invoke that lets the API respond to general questions without document context.

I initially ran into an error with the new endpoint because the MODEL_ID environment variable wasn’t set. Once I fixed it, I validated the new endpoint by adding MODEL_ID to my .env file using the part after model/ from the ARN (for example, meta.llama3-3-70b-instruct-v1:0). After saving the file and restarting the API, I confirmed it worked by hitting /bedrock/invoke with a test query like “Why is the sky blue?”.

When I use /bedrock/query, the chatbot first searches my Knowledge Base for context and then generates an answer, which makes it accurate for questions about my documents or projects. But when I use /bedrock/invoke, the chatbot skips the search and answers directly from its general knowledge, which works for broad questions but lacks my specific context.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-api_u8d9e0f1)

---

---
