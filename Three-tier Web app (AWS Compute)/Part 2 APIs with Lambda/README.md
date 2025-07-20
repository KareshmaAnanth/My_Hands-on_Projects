<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# APIs with Lambda + API Gateway

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-compute-api)

**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)

**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

**Logic tier Documentation:** [Detailed](https://github.com/KareshmaAnanth/My_Hands-on_Projects/blob/01690a63bbc2c686176f1f728f609a2b647ee1bf/Three-tier%20Web%20app%20(AWS%20Compute)/Part%202%20APIs%20with%20Lambda/Three%20-%20tier%20Part%202%20Logic%20tier.pdf)

⚠️*GitHub sometimes just fails to preview certain PDFs, but the file is still downloadable and safe*

---

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-api_c9d0e1f2)

---

## Introducing Today's Project!

In this project, I will demonstrate how to build a serverless API using AWS Lambda and API Gateway. I'm doing this project to learn how backend logic is implemented in a cloud-native way, without managing servers, and to understand how APIs are securely configured and integrated in a three-tier architecture.

### Tools and concepts

Services I used were AWS Lambda and Amazon API Gateway. Key concepts I learnt include Lambda functions, API creation and deployment, RESTful resource handling, HTTP methods like GET, and how Lambda and API Gateway work together to create serverless APIs. I also explored API stages, invoke URLs, and writing API documentation using OpenAPI/Swagger standards.

### Project reflection

This project took me approximately 1 hour to complete. The most challenging part was understanding how API Gateway integrates with Lambda and configuring the GET method correctly. It was most rewarding to see my serverless API work and to write and publish proper API documentation an essential skill for real-world backend and cloud development.

I did this project today to deepen my understanding of serverless architecture and learn how to build and expose backend logic using AWS Lambda and API Gateway. This project met my goals by helping me set up a working API, connect it to a Lambda function, and document it properly valuable skills for backend and cloud roles.

---

## Lambda functions

AWS Lambda is a serverless compute service that runs my code in response to events, without the need to manage servers. I'm using Lambda in this project to handle backend logic that responds to API requests specifically, to simulate fetching user data as part of the logic tier in a three-tier web architecture.

The code I added to my function will connect to a DynamoDB table named UserData and retrieve user information based on a userId passed through an API query string. It returns the user’s data if found, or an appropriate error message otherwise simulating a typical backend lookup in a serverless setup.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-api_a1b2c3d5)

---

## API Gateway

APIs are interfaces that allow different software systems to communicate and exchange data. There are different types of APIs, like REST for standard web operations, WebSocket for real-time communication, and HTTP for simplified routing. My API is a REST API, ideal for linking user requests to my Lambda function in a scalable, language-agnostic way.

Amazon API Gateway is a fully managed service that helps me create and manage APIs at scale. I'm using API Gateway in this project to securely expose my Lambda function to users, handle incoming requests, and manage traffic, security, and routing between clients and backend logic.

When a user makes a request, API Gateway receives it and forwards it to the Lambda function. Lambda then processes the request such as retrieving data and sends the response back to API Gateway, which returns it to the user. This setup creates a secure and serverless way to run backend logic for web or mobile applications.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-api_m3n4o5p6)

---

## API Resources and Methods

An API is made up of resources, which represent specific endpoints that handle different functions of your application. Each resource maps to a part of the data or service, like /users or /messages, helping to organize and route incoming requests effectively.

Each resource consists of methods, which are actions that define how clients can interact with that resource using standard HTTP commands. For example, GET retrieves data, POST adds new data, PUT updates existing data, and DELETE removes data. These methods control how your API behaves and responds.

I created a GET method for the /users resource and connected it to my RetrieveUserData Lambda function. This allows API Gateway to forward user requests directly to the Lambda function, which then retrieves and returns user data from DynamoDB.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-api_c9d0e1f2)

---

## API Deployment

When you deploy an API, you deploy it to a specific stage. A stage is like a versioned environment (e.g., dev, test, or prod) that holds your deployed API configuration. I deployed to the prod stage, which is the live environment where real users can access and interact with the API.

To visit my API, I copied the Invoke URL from the prod stage page and opened it in a new browser tab. The API displayed an error because I haven’t set up the DynamoDB table yet—so there’s no data for the Lambda function to retrieve.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-api_3ethryj2)

---

## API Documentation

For my project's extension, I am writing API documentation because it helps other developers understand how to use my API, what endpoints and parameters to use, and what responses to expect. You can do this in API Gateway’s Documentation section, where each method and resource can be clearly described in JSON format.

Once I prepared my documentation, I could publish it to the prod stage by selecting Publish documentation, choosing the correct stage, and entering a version number. You have to publish your API to a specific stage because each stage represents a version of the API, ensuring the right documentation matches the deployed API.

My published and downloaded documentation showed me a detailed JSON file containing both the high-level description I manually wrote and the automatically generated sections from API Gateway. It included my API's title, version, base URL, resource paths like /users, supported methods like GET, and a x-amazon-apigateway-documentation section capturing descriptions, parameters, and responses.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-api_z9a0b1c2)

---

---
