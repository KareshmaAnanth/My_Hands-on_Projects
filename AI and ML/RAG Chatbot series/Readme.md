###### ***##*** ***Run AWS Commands*** 



To make sure CloudShell is working by running a simple command:

&nbsp;    

* aws -- version 



***#*** In CloudShell terminal. This command will ask your chatbot to answer the question "What is NextWork?"





aws bedrock-agent-runtime retrieve-and-generate \\

&nbsp;  --input '{"text": "What is NextWork?"}' \\

&nbsp;  --retrieve-and-generate-configuration '{

&nbsp;      "knowledgeBaseConfiguration": {

&nbsp;          "knowledgeBaseId": "your\_knowledge\_base\_id",

&nbsp;          "modelArn": "your\_model\_arn"

&nbsp; },

&nbsp; "type": "KNOWLEDGE\_BASE"

}'



Return error because need to replace your\_knowledge\_base\_id and your\_model\_arn, which are placeholders in the command, with your Knowledge Base ID and Model ARN.

###### 

###### \## ***Finding Your Knowledge Base and Model ARN \& IDs***



1\) Find the Knowledge Base ID from the overview panel.

2\) Find Your Model ARN



In the CloudShell terminal, run the following command to find the ARN of your model.



aws bedrock get-foundation-model --model-identifier <your-model-id>

&nbsp;

To find Model ID, Open Bedrock console again 

&nbsp;- Select Model catalog

&nbsp;- where you can find all the models available in Bedrock, and find metadata about each model - like the Model ID.

&nbsp;- Find the Llama 3.3 70B Instruct model.

&nbsp;- Copy the Model ID from the details panel



Now again run this in cloudshell to return the model ARN 



aws bedrock get-foundation-model --model-identifier meta.llama3-3-70b-instruct-v1:0





\# Tidy up the terminal response

Replace the KnowledgeBase ID and Model ARN with the command 



aws bedrock-agent-runtime retrieve-and-generate \\

&nbsp;   --input '{"text": "What is NextWork?"}' \\

&nbsp;   --retrieve-and-generate-configuration '{

&nbsp;       "knowledgeBaseConfiguration": {

&nbsp;           "knowledgeBaseId": "your\_knowledge\_base\_id",

&nbsp;           "modelArn": "your\_model\_arn"

&nbsp;       },

&nbsp;       "type": "KNOWLEDGE\_BASE"

&nbsp;   }' \\

&nbsp;   --query 'output.text' \\

&nbsp;   --output text



( output.text field in the response. This means the terminal response will only show the text of the response, not the raw information that's used to generate it)



###### ***## Boost Your Chatbot's Knowledge*** 



&nbsp;- Add new data to your S3 bucket.

&nbsp;- Sync your Knowledge Base with the new data.

&nbsp;- Test your RAG chatbot - can it answer questions about the new data?



1\) create a new file called secret-mission.txt



echo "Why did the coffee go to the police? Because it got mugged!" > secret-mission.txt



2\) Check the contents of the file by running the command: 



cat secret-mission.txt



3\) Upload your new file from the CloudShell terminal to your S3 bucket.



aws s3 cp secret-mission.txt s3://nextwork-rag-documentation-kareshma/secret-mission.txt



(aws s3 cp command copies files to S3)



4\) Check the contents of your S3 bucket



aws s3 ls s3://nextwork-rag-documentation-kareshma/



5\) Sync Your Knowledge Base



Run the command below to start a new ingestion job. An ingestion job syncs your Knowledge Base with your data source.( Replace both placeholders) 



aws bedrock-agent start-ingestion-job \\

&nbsp;   --knowledge-base-id "your\_knowledge\_base\_id" \\

&nbsp;   --data-source-id "your\_data\_source\_id"

\- How to find Data source ID 

Run this command in terminal and make sure to open cloudshell in Ohio region 



aws bedrock-agent list-data-sources \\

&nbsp;   --knowledge-base-id "your\_knowledge\_base\_id"



Now,after replacing the both placeholders run the ingestion job again 

Also can check the status of your sync by running the command



aws bedrock-agent get-ingestion-job \\

&nbsp;   --knowledge-base-id "your\_knowledge\_base\_id" \\

&nbsp;   --data-source-id "your\_data\_source\_id" \\

&nbsp;   --ingestion-job-id "your\_ingestion\_job\_id"



\# once sync is complete test if knowledge base learned about new information



aws bedrock-agent-runtime retrieve-and-generate \\

&nbsp;   --input '{"text": "Why did the coffee go to the police?"}' \\

&nbsp;   --retrieve-and-generate-configuration '{

&nbsp;       "knowledgeBaseConfiguration": {

&nbsp;           "knowledgeBaseId": "your\_knowledge\_base\_id",

&nbsp;           "modelArn": "your\_model\_arn"

&nbsp;       },

&nbsp;       "type": "KNOWLEDGE\_BASE"

&nbsp;   }' \\

&nbsp;   --query 'output.text' \\

&nbsp;   --output text

 

###### ***## Chat with AI Models Directly***



Learn how to talk with AI models directly using the AWS CLI.



To chat with an AI model directly, you can use the bedrock-runtime invoke-model command



aws bedrock-runtime invoke-model \\

&nbsp;   --model-id meta.llama3-3-70b-instruct-v1:0 \\

&nbsp;   --body '{"prompt": "Write a short poem about cats"}' \\

&nbsp;   --cli-binary-format raw-in-base64-out \\

&nbsp;   --region us-east-2 \\

&nbsp;   --output text \\

&nbsp;   /dev/stdout



###### ***## Delete the resources*** 



* Bedrock Knowledge Base
* OpenSearch vector store
* S3 bucket





