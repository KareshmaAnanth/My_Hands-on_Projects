# 🤖 RAG Chatbot Series with Amazon Bedrock

Welcome to the **RAG Chatbot Series**   a hands-on, 4-part journey where you’ll build a fully functional, AI-powered chatbot that can answer questions based on your own knowledge base using **Amazon Bedrock**, **FastAPI**, and **Python**.

By the end, you’ll understand how Retrieval-Augmented Generation (RAG) works end-to-end from data ingestion to web deployment.

---

## 🧠 Key Concepts

### 🔹 What is RAG (Retrieval-Augmented Generation)?
RAG combines **information retrieval** and **text generation**.  
It retrieves relevant data (from your knowledge base) and feeds it into a large language model (LLM) to generate accurate, context-aware answers.

### 🔹 What is Amazon Bedrock?
Amazon Bedrock is a **fully managed service** that lets you build and scale generative AI applications using foundation models (like Claude, Titan, and Llama) via a single API — without managing infrastructure.

### 🔹 What are Embedding Models?
Embedding models convert text into **numeric vector representations** — allowing semantic search and similarity matching between queries and documents.

### 🔹 What is a Vector Store?
A vector store (like **OpenSearch Serverless**) stores embeddings and lets the system **find meaning-related results**, not just keyword matches — enabling smarter retrieval for RAG.

---

## 📚 Project Overview

| Project | Title | Description |
|----------|--------|-------------|
| 🧩 **Project 1** | [Set Up a RAG Chatbot in Amazon Bedrock](https://github.com/KareshmaAnanth/My_Hands-on_Projects/tree/73d0af2471b14656881bc20c2d84ff5be167a5ea/AI%20and%20ML/RAG%20Chatbot%20series/1%20Set%20up%20a%20%20RAG%20Chatbot%20in%20Bedrock) | Configure Bedrock, create a Knowledge Base, and connect your data in S3. |
| 💬 **Project 2** | [Chat with Your Bot in the Terminal](https://github.com/KareshmaAnanth/My_Hands-on_Projects/tree/73d0af2471b14656881bc20c2d84ff5be167a5ea/AI%20and%20ML/RAG%20Chatbot%20series/2%20Chat%20with%20Bot%20in%20Terminal) | Interact directly with your RAG chatbot using Python CLI and Bedrock APIs. |
| ⚙️ **Project 3** | [Create an API for Your RAG Chatbot](https://github.com/KareshmaAnanth/My_Hands-on_Projects/tree/73d0af2471b14656881bc20c2d84ff5be167a5ea/AI%20and%20ML/RAG%20Chatbot%20series/3%20Create%20API%20for%20RAG%20Chatbot) | Build a FastAPI backend exposing endpoints to query your Bedrock chatbot. |
| 💻 **Project 4** (Final) | [Build a Web App for Your RAG Chatbot](https://github.com/KareshmaAnanth/My_Hands-on_Projects/tree/73d0af2471b14656881bc20c2d84ff5be167a5ea/AI%20and%20ML/RAG%20Chatbot%20series/4%20Web%20app%20for%20RAG%20Chatbot) | Create a frontend web app to chat through your browser using your API. |

---

## 🧭 How It All Connects

1. **Project 1:** Sets up your AWS foundation — Knowledge Base, S3, and Bedrock access.  
2. **Project 2:** Tests your chatbot locally through command line.  
3. **Project 3:** Exposes your chatbot as an API endpoint using FastAPI.  
4. **Project 4:** Adds a web interface, creating a complete, interactive chatbot app.

Together, these projects demonstrate a **full-stack RAG pipeline** — from data to interface.

---

## 🧩 Architecture Overview
```
User → Web App (Frontend)
↓
FastAPI Backend
↓
Amazon Bedrock (LLM)
↓
Knowledge Base (Vector Store in OpenSearch)
↓
S3 Documents
```


---

## 🛠️ Tech Stack
- **Amazon Bedrock** – foundation model access and orchestration  
- **Amazon S3** – document storage  
- **OpenSearch Serverless** – vector database for semantic retrieval  
- **FastAPI** – backend API service  
- **HTML, CSS, JavaScript** – web app interface  
- **Python** – main programming language  

---

## 🌟 What You’ll Learn
- How RAG systems retrieve and generate responses intelligently  
- How to integrate AWS Bedrock with FastAPI  
- How to design API and frontend layers for AI apps  
- How to customize chatbot UI/UX  
- How to clean up AWS resources safely  

---

## 🧹 Clean Up Reminder
After completing all four projects:
- Delete the **Bedrock Knowledge Base**, **S3 bucket**, and **OpenSearch collection**.  
- Revoke **IAM access keys** and remove your **virtual environment**.  

---

## 🧠 Author
Built by **Kareshma**, aspiring Cloud Engineer (DevOps, AI, AWS).  
Exploring how **cloud + AI** can power the next generation of intelligent apps.

---

