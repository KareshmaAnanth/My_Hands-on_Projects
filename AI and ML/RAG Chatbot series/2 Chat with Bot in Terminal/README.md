<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Chat With Your Bot in the Terminal

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-rag-cloudshell)

**Author:** Kareshma Rajaananthapadmanaban  
**Email:** kareshma2909@gmail.com

---

## Interacting With My RAG Chatbot in the Terminal

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-cloudshell_1i2j3k4l)

---

## Introducing Today's Project!

In this project, I will build a RAG chatbot that answers questions directly from the terminal using Amazon Bedrock. I'm doing this project to learn how to interact with my chatbot through the AWS CLI in CloudShell, manage a Knowledge Base without relying on the console, and practice command-line workflows. This helps me gain practical skills useful for DevOps and backend engineering, where speed, automation, and control matter.

### Tools and concepts

The services I used were Amazon Bedrock, S3, CloudShell, and the Bedrock Agent/Runtime. The key concepts I learnt included creating and uploading files to S3, syncing and updating a Knowledge Base through ingestion jobs, retrieving responses from a Knowledge Base, and invoking AI models directly from the CLI for both knowledge-specific and creative tasks.

### Project reflection

This project took me approximately 2 hours to complete. The most challenging part was figuring out the correct parameters and IDs while running commands in the CLI. It was most rewarding to see my Knowledge Base update successfully and to interact directly with an AI model through the terminal it felt like I had built my own mini AI lab.


I did this project today to push myself beyond just using the AWS console and get more comfortable with managing services directly from the CLI. Yes, it met my goals I wanted hands-on practice with Bedrock, S3, and Knowledge Bases, and I also learned how to interact with AI models in the terminal. It gave me both confidence and practical skills I can reuse in future projects.

---

## Setting Up The Knowledge Base

To set up my Knowledge Base, I used S3 to store all the documents my chatbot will learn from. The documents I uploaded contain information about my NextWork project documentation, which showcase the steps, skills, and experiences I’ve built. By keeping them in S3, I gave the chatbot a secure, centralized source of truth to reference when answering questions.


I also created a Knowledge Base in Bedrock to give my chatbot the ability to understand and retrieve information from the documents stored in S3. Instead of just holding raw files, the Knowledge Base organizes data using embeddings and a vector store, making it searchable by meaning. This way, my chatbot can answer questions accurately, even if the wording in the query is different from the documents.

My chatbot also requires access to two AI models: Titan Text Embeddings V2 for converting documents into embeddings and Llama 3.3 70B Instruct for generating human-like responses. I then synchronized the Knowledge Base so it could read the documents from S3, process their meaning, and store embeddings in OpenSearch making the chatbot ready to fetch and answer questions accurately.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-cloudshell_1u2v3w4x)

---

## Running CLI Commands in CloudShell

AWS CLI is a command line tool that lets me create, update, and manage AWS resources with text commands instead of clicking through the console. To start testing CLI commands, I first opened CloudShell, which is a built-in shell environment in the AWS Management Console that already has AWS CLI pre-installed, saving me from having to install or configure it on my own system.

When I first ran a Bedrock command, I ran into an error because I needed to provide values for the `knowledgeBaseId` and `modelArn`. These placeholders tell Bedrock which Knowledge Base to search and which AI model to use. Without replacing them with my actual Knowledge Base ID and the Llama 3.3 70B Instruct model’s ARN, the CLI command couldn’t execute.

While finding the parameters takes extra time, the advantage of using the CLI is flexibility and control. You can switch between different Knowledge Bases and models just by swapping values, automate repetitive tasks with scripts, and run commands directly in your workflow without clicking through the console. It’s faster, scalable, and perfect for frequent testing or debugging.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-cloudshell_sdrgsert)

---

## Running Bedrock Commands

To find the required values, I had to locate my Knowledge Base ID from the Bedrock console and retrieve the Model ARN using the `aws bedrock get-foundation-model` command with the model ID `meta.llama3-3-70b-instruct-v1:0`. Once I replaced both placeholders in the retrieve-and-generate command, the Bedrock command ran successfully and showed me a chatbot response to “What is NextWork?” right in the CloudShell terminal.


The retrieve-and-generate command typically also outputs the retrieved documents along with the chatbot’s response. To tidy up the terminal response, I added the `--query 'output.text' --output text` parameters, which filtered the output to show only the generated answer text. This made the terminal response cleaner and easier to read while still keeping the chatbot functional.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-cloudshell_1i2j3k4l)

---

## Extending Your Knowledge Base

In a project extension, I asked my Knowledge Base about why the coffee went to the police. I noticed it couldn’t answer the question because that information wasn’t part of the data stored in S3 or synced to the Knowledge Base. This showed me that the chatbot can only respond based on what it has been trained or updated with. It confirmed that before the new data is added and synced, the chatbot won’t recognize or respond to queries outside its existing knowledge.


To add new information to my Knowledge Base, I ran commands to create a text file in CloudShell, upload it to my S3 bucket, and then trigger an ingestion job to sync the Knowledge Base with the new data source. I also used commands to check the ingestion status and confirm the update. Compared to using the console, this process was faster, more precise, and gave me a better understanding of how to automate Knowledge Base updates directly from the terminal.

To validate the update worked, I ran the `retrieve-and-generate` command again with my new question. The Knowledge Base successfully retrieved the added document, processed the new content, and returned the updated answer. This confirmed that the ingestion job worked correctly and my chatbot could now respond to queries using the newly uploaded data.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-cloudshell_sm789ghi)

---

## Interacting with AI Models Directly

On top of chatting with my chatbot, I also interacted directly with an AI model via the terminal by running the `bedrock-runtime invoke-model` command. I specified the model ID `meta.llama3-3-70b-instruct-v1:0`, passed in my prompt, and received the response as plain text. This let me bypass the Knowledge Base and test the model’s creative capabilities directly.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-rag-cloudshell_gregerg)

---

---
