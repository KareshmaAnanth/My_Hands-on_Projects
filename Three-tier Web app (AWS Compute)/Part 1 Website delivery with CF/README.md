<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Website Delivery with CloudFront

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-networks-cloudfront)

**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)

**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

**Presentation tier Documentation:** [Detailed](https://github.com/KareshmaAnanth/My_Hands-on_Projects/blob/9233cc7b4c0887f21a017758c9cc13d5b76735b4/Three-tier%20Web%20app%20(AWS%20Compute)/Part%201%20Website%20delivery%20with%20CF/Three-tier%20part%201%20Presentation%20tier.pdf)  


---

## Website Delivery with CloudFront

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-networks-cloudfront_1dddddwe)

---

## Introducing Today's Project!

In this project, I will demonstrate how to deploy a static website using Amazon S3 and distribute it globally with Amazon CloudFront. I'm doing this project to learn how to deliver web content efficiently, manage permissions securely, and gain practical experience in building the presentation layer of a three-tier web architecture.

### Tools and concepts

Services I used were Amazon S3 and Amazon CloudFront. Key concepts I learnt include content delivery network (CDN), origin access control (OAC), S3 static website hosting, bucket policies, and caching behavior. I also practiced performance comparison, secure access management, and developer tools for analyzing website load times.

### Project reflection

This project took me approximately less than an hour to complete. The most challenging part was troubleshooting the access denied errors while configuring S3 static website hosting and understanding how Origin Access Control works with bucket policies. t was most rewarding to see my website successfully delivered through CloudFront and optimized for global performance.

I did this project to deepen my understanding of how static websites are delivered securely and efficiently using AWS services. It helped me connect S3 storage with CloudFront delivery and reinforced my knowledge of permissions, caching, and performance optimization. Yes, this project met my goals by enhancing both my practical skills and cloud architecture confidence.

---

## Set Up S3 and Website Files

I started the project by creating an S3 bucket to store and serve my static website files like HTML, CSS, and JavaScript. I can't use CloudFront for this task because CloudFront is a content delivery network, not a storage service. It needs an origin source, and S3 acts as that reliable and scalable origin for website content.

The three files that make up my website are `index.html`, which defines the structure and content of the webpage; `style.css`, which adds styling and visual formatting to the page; and `script.js`, which handles the client-side logic and interactivity of the website when opened in a browser.

I validated that my website files work by opening the `index.html` file directly in my browser. I checked that the layout rendered correctly, the styles from `style.css` were applied, and the interactive elements controlled by `script.js` responded as expected. This confirmed the files were functional before uploading to S3.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-networks-cloudfront_qgo7wcd3)

---

## Exploring Amazon CloudFront

Amazon CloudFront is a content delivery network, which means it delivers web content like HTML, CSS, JS, and images faster to users by caching it at global edge locations. Businesses and developers use CloudFront because it reduces latency, improves website load times, enhances security with HTTPS, and scales automatically to handle traffic spikes.

To use Amazon CloudFront, you set up distributions, which are configuration sets that define how CloudFront delivers your content. I set up a distribution for my static website to ensure fast, global delivery. The origin is my S3 bucket, which stores the website files CloudFront will cache and serve through edge locations.

My CloudFront distribution’s default root object is index.html. This means when users visit the root URL of the site without specifying a file CloudFront will automatically serve index.html from the S3 bucket. I kept the origin public, left cache behavior and other advanced settings as default for a simple, fast, and secure setup.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-networks-cloudfront_qgo7wcdt)

---

## Handling Access Issues

When I tried visiting my distributed website, I ran into an access denied error because my S3 bucket, which is the origin for CloudFront, is private by default. Although the bucket exists and contains the files, CloudFront doesn't have permission yet to access or serve them publicly through its distribution.

My distribution's origin access settings were set to Public. This caused the access denied error because, although CloudFront was allowed to access the origin, the objects inside my S3 bucket were still private. Without explicitly setting those files to public, CloudFront couldn’t retrieve or serve them to users.

To resolve the error, I set up origin access control (OAC). OAC is a secure method that allows CloudFront to access content in a private S3 bucket without making the files publicly accessible. It improves security by creating a special identity for CloudFront, giving it controlled access to the bucket while keeping the objects private from the public.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-networks-cloudfront_egrhntyu)

---

## Updating S3 Permissions

Once I set up my OAC, I still needed to update my bucket policy because the OAC only defines how CloudFront will authenticate requests to the S3 bucket. For CloudFront to actually retrieve content, the S3 bucket must explicitly grant permission to the OAC identity through its policy. Without this, access remains denied.

Creating an OAC automatically gives me a policy I could copy, which grants CloudFront permission to access the objects in my S3 bucket. This policy ensures only the CloudFront distribution associated with the OAC can read the content, keeping the bucket private while still allowing secure content delivery through CloudFront.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-networks-cloudfront_eg98ntyu)

---

## S3 vs CloudFront for Hosting

For my project extension, I'm comparing CloudFront and S3 static website hosting. I initially had an error with static website hosting because, even though hosting was enabled, the objects in my bucket were still private. S3 static websites require public access to serve files directly, so I need to update object permissions or the bucket policy.

I tried resolving this by disabling "Block all public access" in the S3 settings. I still ran into an error because I hadn't added a bucket policy to explicitly grant public read access to the objects. Without that policy, the files remain inaccessible, and S3 returns a 403 error even though public access is no longer blocked globally.

I could finally see my S3 hosted website when I added a bucket policy that allowed public read access to all objects using the correct bucket ARN. This worked because it explicitly granted everyone permission to retrieve files from the bucket, enabling S3 to serve the website content through its static hosting endpoint.

Compared to the permission settings for my CloudFront distribution, using S3 meant making the bucket and its objects publicly accessible through a bucket policy, which poses a higher security risk. I preferred CloudFront’s setup with Origin Access Control, as it allowed me to keep the bucket private while still serving content securely.

---

## S3 vs CloudFront Load Times

Load time means how quickly a website’s content is delivered to and rendered by the user’s browser. The load times for the CloudFront site were faster than the S3 site because CloudFront caches content at edge locations around the world, reducing latency. In contrast, S3 serves files from a single region, leading to longer data travel times.

A business would prefer CloudFront when performance, global reach, and security are priorities such as for production websites, e-commerce platforms, or apps with international users. S3 static website hosting might be sufficient when serving simple sites with low traffic or internal tools where speed and security are less critical.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-networks-cloudfront_12verpuh)

---

---
