<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a Three-Tier Web App

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-compute-threetier)

**Author:** Kareshma Rajaananthapadmanaban  
**Email:** kareshma2909@gmail.com

---

## Build a Three-Tier Web App

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_2b3c4d5e)

---

## Introducing Today's Project!

In this project, I will demonstrate how to build a fully functional three-tier web application using AWS services. I'm doing this project to learn how to integrate the presentation, logic, and data tiers using S3, CloudFront, Lambda, API Gateway, and DynamoDB in a scalable, serverless architecture.

### Tools and concepts

Services I used were S3, CloudFront, Lambda, API Gateway, and DynamoDB. Key concepts I learnt
include Lambda functions for serverless compute, REST APIs with API Gateway, storing and retrieving data using DynamoDB, CORS handling, and how to connect the presentation, logic, and data tiers to build a fully functional web app on AWS.

### Project reflection

This project took me approximately 1 hour to complete, plus a few extra minutes to write the documentation.The most challenging part was troubleshooting the API connection and resolving CORS-related errors. It was most rewarding to see the entire three-tier architecture working seamlessly and displaying live data on the website.

I did this project today to practice building a full-stack serverless web application using real AWS services. My goal was to understand how the presentation, logic, and data tiers work together in a cloud-native architecture. Yes, this project met my goals it helped me apply core AWS concepts hands-on and gave me confidence in deploying a complete three-tier solution.

---

## Presentation tier

For the presentation tier, I will set up an S3 bucket to host my static website files and use CloudFront to distribute the content globally, because this ensures fast, reliable, and secure delivery of the web interface to users across different regions.

I accessed my delivered website by copying the domain name from my CloudFront distribution and pasting it into my browser. CloudFront fetches the files stored in my S3 bucket and delivers them through its global edge locations. This ensures that my website loads faster for users around the world by serving cached content from the nearest server, making the experience smooth and reliable.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_3a4b5c6d)

---

## Logic tier

For the logic tier, I will set up an AWS Lambda function connected to an API Gateway because this layer handles the core application logic. It processes incoming user requests, fetches data from the DynamoDB table, and returns responses. This setup enables scalable, serverless interaction between the frontend and backend.

The Lambda function retrieves data by using the AWS SDK to connect to DynamoDB. It extracts the `userId` from the incoming HTTP request’s query string parameters. Then, it uses `GetCommand` to look up the item in the `UserData` table with that `userId`. If the item is found, it returns it in the response with a 200 status code. If not, it returns a 404. Errors during the process return a 500 status with an appropriate error message.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_6a7b8c9d)

---

## Data tier

For the data tier, I will set up a DynamoDB table to store and manage user data because it's a fast, serverless NoSQL database that integrates well with Lambda. This allows my web app to retrieve user-specific information dynamically through the API, making the application functional and data-driven.

The partiton key for my DynamoDB table is `userId`, which means each item in the table is uniquely identified by a user ID. This lets me efficiently retrieve individual user data. I'm using DynamoDB to store structured user records that my Lambda function can fetch when requested through the API.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_u1v2w3x4)

---

## Logic and Data tier

Once all three layers of my three-tier architecture are set up, the next step is to connect them by updating the frontend (presentation tier) to talk to the backend API (logic tier). This ensures that when a user visits the site, the browser can fetch and display data from DynamoDB through API Gateway and Lambda, completing the app flow.

To test my API, I copied the Invoke URL from the API Gateway's prod stage and appended `/users?userId=1` to it. I then opened the full URL in my browser. The results were successful I saw the expected user data returned from the DynamoDB table, which confirmed that the API Gateway and Lambda function integration is working correctly.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_a112c3d5)

---

## Console Errors

The error in my distributed site was because the `script.js` file still had a placeholder `[YOUR-PROD-API-URL]` instead of my actual API Gateway invoke URL. As a result, the site was trying to make a request to a non-existent endpoint, which caused a JavaScript error and prevented any data from being fetched or displayed.

To resolve the error, I updated script.js by replacing the `[YOUR-PROD-API-URL]` placeholder with my actual API Gateway invoke URL. I then reuploaded it into S3 because CloudFront serves files from the S3 bucket, so the updated JavaScript needed to be present there for the website to correctly fetch and display user data.

I ran into a second error after updating script.js. This was an error with CORS (Cross-Origin Resource Sharing) because my API Gateway wasn’t configured to accept requests from the CloudFront-distributed frontend. Without proper CORS settings, the browser blocks cross-origin requests between the frontend and backend.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_a1b2c3d5)

---

## Resolving CORS Errors

To resolve the CORS error, I first enabled CORS on my API Gateway's `/users` resource. I selected both GET and OPTIONS methods under Access-Control-Allow-Methods and added my CloudFront distribution domain under Access-Control-Allow-Origin. This allows my frontend to securely interact with the backend API.

I also updated my Lambda function because I'm using Lambda Proxy Integration, which requires the function itself to return CORS headers. The changes I made were adding `'Access-Control-Allow-Origin': '*'` in the response headers so that the frontend (hosted on CloudFront) can successfully make API requests without being blocked by the browser's CORS policy.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_1qthryj2)

---

## Fixed Solution

I verified the fixed connection between API Gateway and CloudFront by refreshing my CloudFront URL and testing the user data retrieval. This time, the data was successfully fetched from DynamoDB and displayed on the website, confirming that the CORS configuration and Lambda response headers were correctly updated.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-compute-threetier_2b3c4d5e)

---

---
