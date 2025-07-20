<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Fetch Data with AWS Lambda

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-compute-lambda)

**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)

**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

**Data tier Documentation:** [Detailed](https://github.com/KareshmaAnanth/My_Hands-on_Projects/blob/7c13632cfe4c1a3c8926f5a1bcfac8b294cf3334/Three-tier%20Web%20app%20(AWS%20Compute)/Part%203%20Fetch%20data%20with%20AWS%20Lambda/Three%20-%20tier%20Part%203%20Data%20tier.pdf) 

⚠️*GitHub sometimes just fails to preview certain PDFs, but the file is still downloadable and safe*

---

## Fetch Data with AWS Lambda

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_p9thryj2)

---

## Introducing Today's Project!

In this project, I will demonstrate how to retrieve data from a DynamoDB table using a serverless AWS Lambda function. I'm doing this project to learn how serverless architectures manage and fetch backend data efficiently, forming the data tier of a scalable three-tier application.

### Tools and concepts

Services I used were AWS Lambda and DynamoDB. Key concepts I learnt include Lambda functions as serverless compute, how to securely interact with DynamoDB using IAM roles and fine-grained permissions, how to write and test Lambda functions, and the importance of using inline policies for tighter security.

### Project reflection

This project took me approximately 1 hour and 15 minutes to complete. The most challenging part was resolving the AccessDenied error by updating and refining IAM permissions. It was most rewarding to see my Lambda function successfully retrieve data from DynamoDB after securing it with a tightly scoped inline policy.

I did this project today to deepen my hands-on understanding of using AWS Lambda with DynamoDB in a real-world, serverless context. This project met my goals by helping me practice secure permission setup, API integration, and efficient data retrieval all essential for building scalable cloud-native applications.

---

## Project Setup

To set up my project, I created a database using DynamoDB called UserData. The partition key is userId, which means each item in the table is uniquely identified by a user ID. This key helps DynamoDB efficiently organize, store, and retrieve user-specific data across distributed servers.

In my DynamoDB table, I added a sample item with userId as "1", along with the user's name and email. DynamoDB is schemaless, which means I didn’t need to define name or email attributes in advance each item can have different attributes, giving me flexibility to store varied data.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_a112c3d5)

### AWS Lambda

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. I'm using Lambda in this project to retrieve user data from a DynamoDB table efficiently, without needing to handle backend infrastructure manually.

---

## AWS Lambda Function

My Lambda function has an execution role, which is an IAM role that defines what the function is allowed to do within AWS. By default, the role grants permissions to write logs to CloudWatch, helping me monitor and debug my function's execution securely.

My Lambda function will retrieve user data from a DynamoDB table based on a provided userId. It uses the AWS SDK for JavaScript to connect to DynamoDB, send a GetCommand to fetch the matching item, and return it. If the item isn’t found or an error occurs, it logs the result and returns a null value or error accordingly.

The code uses AWS SDK, which is a collection of libraries that make it easier for developers to interact with AWS services using their preferred programming language. My code uses SDK to connect to DynamoDB, send a request to fetch a user's data using their userId, and handle the response without writing low-level API calls.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_a1b2c3d5)

---

## Function Testing

To test whether my Lambda function works, I used the Test tab in the Lambda console and entered a JSON event with a userId of "1". The test is written in JSON because it's the standard format Lambda understands for input events. If the test is successful, I'd see the user's data returned from the DynamoDB table.

The test displayed a "success" because the Lambda function ran without syntax or runtime errors, but the function's response was actually an access denied error because it didn’t have permission to read from the DynamoDB table. We need to explicitly grant access in the Lambda execution role.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_u1v2w3x4)

---

## Function Permissions

To resolve the AccessDenied error, I reviewed the error message and found that the denied action was dynamodb:GetItem. This means my Lambda function lacks read access to DynamoDB. I’m attaching the AmazonDynamoDBReadOnlyAccess policy because it grants permission to perform read operations like GetItem, resolving the error securely.

There were four DynamoDB permission policies I could choose from, but I didn't pick AWSLambdaDynamoDBExecutionRole or AWSLambdaInvocation-DynamoDB because they are meant for working with DynamoDB Streams, not for reading items from a table. My Lambda function needs GetItem access, which only the AmazonDynamoDBReadOnlyAccess policy provides.

I also didn't pick AmazonDynamoDBFullAccess because it grants unnecessary permissions, including write and delete access, which could pose a security risk. AmazonDynamoDBReadOnlyAccess was the right choice because it provides just enough access like GetItem for my Lambda function to securely read data without overexposing the database.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_3ethryj2)

---

## Final Testing and Reflection

To validate my new permission settings, I re-ran the Lambda function test using a sample event with userId: "1". The results were successful and returned the correct user data from DynamoDB because the function now has AmazonDynamoDBReadOnlyAccess, which includes permission to perform the GetItem operation.

Web apps are a popular use case of using Lambda and DynamoDB. For example, I could build a user profile system that fetches data when someone logs in, create a product catalog that updates dynamically, or design a blog that retrieves posts based on search queries all without managing any servers.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_p9thryj2)

---

## Enahancing Security

For my project extension, I challenged myself to replace the broad AmazonDynamoDBReadOnlyAccess policy with a custom inline policy that only allows access to the specific UserData table. This will tighten security by limiting the Lambda function to exactly what it needs no more, no less.

To create the permission policy, I used the JSON method because it gave me more control and was quicker to implement. I'm comfortable writing IAM policies in JSON, and it allowed me to directly specify only the exact GetItem action for my UserData table, minimizing excess permissions.

When updating a Lambda function's permission policies, you could risk accidentally removing access it needs to function properly. I validated that my Lambda function still works by re-running the test in the Test tab and confirming that it successfully retrieved the item from my DynamoDB table.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-lambda_1qthryj2)

---

---
