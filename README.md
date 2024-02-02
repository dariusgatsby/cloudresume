# cloudresume

Certainly! Here's the provided text converted into a step-by-step list in Markdown:

### CHUNK 1: Setting Up Resume Hosting

1. **Frontend Development:**
   - Created the resume's HTML and CSS components using tools to expedite the frontend development process.

2. **Connection Challenges:**
   - Faced difficulties connecting the hosted zone with the S3 bucket.
   - Ensured correct bucket names for seamless integration with Route53.
   - Configured both the main domain ([dariuscloudresume.com](http://dariuscloudresume.com)) and its subdomain (www.[dariuscloudresume.com](http://dariuscloudresume.com)).

3. **SSL Certificate Issuance:**
   - Waited for the Amazon-issued SSL certificate.
   - Realized the delay was due to DNS ownership validation via CNAME records.
   - Added the required CNAME records, and the certificate was swiftly validated.

4. **Hosted Zone Records:**
   - Changed records in the hosted zone to facilitate service interactions.
   - Initially puzzled by 403 errors when using CloudFront, corrected CNAME records.
   - Configured the viewer protocol setting to enable HTTPS, ensuring successful CloudFront integration.

5. **Origin Access Control (OAC):**
   - Implemented OAC on the S3 bucket for CloudFront.
   - Turned off the website endpoint as it does not allow OAC configuration.
   - Created a security control and configured bucket policies to allow specific CloudFront distributions while denying access to other principals.

## CHUNK 2: Building the Serverless Components

1. **Technologies Used:**
   - Leveraged AWS services including Lambda, API Gateway, and DynamoDB.
   - Utilized programming languages such as Python and JavaScript.
   - Employed the `boto3` library for AWS SDK in Python.

2. **Learning Python:**
   - This project prompted a focused effort to learn Python seriously, emphasizing reading documentation and understanding Object-Oriented Programming (OOP).

3. **DynamoDB Provisioning:**
   - Provisioned a DynamoDB table, opting for 'on-demand' mode to handle variable workflow and low traffic.

4. **Understanding NoSQL and Data Modeling:**
   - Explored NoSQL database concepts for effective data storage and retrieval.
   - Modeled the database to use a single unique key representing an all-time visitor count.

5. **Lambda Function Development:**
   - Faced challenges understanding the Lambda handler, testing, and working with JSON data.
   - Developed code to access the DynamoDB table and update the `visit_count` attribute on each Lambda function execution.

6. **API Gateway Integration:**
   - Connected the API Gateway to the Lambda function using the console's 'add trigger' feature.
   - Encountered challenges in understanding and creating APIs, delving into resource and method creation.

7. **Open API Configuration:**
   - Configured an open API without authentication, enabling easy access.
   - Implemented throttling as a security measure.

8. **API Gateway Staging:**
   - Staged the API for deployment, ensuring proper functionality.

9. **Connectivity with JavaScript:**
   - Integrated the serverless architecture with the resume site using JavaScript.
   - Ensured seamless interaction between the site and the serverless components.

### CHUNK 3: Automating Resume Updates with GitHub Actions

1. **GitHub Repository Setup:**
   - Created a GitHub repository to store HTML and CSS files of the resume.

2. **Continuous Deployment with GitHub Actions:**
   - Leveraged the S3 Sync GitHub Action to automate the deployment process.
   - Ensured that each push to the GitHub repository triggered the update of the website hosted on S3.

3. **Workflow Modification:**
   - Adjusted the workflow document to accommodate changes in GitHub Actions, considering deprecated features.

4. **Seamless Code Integration:**
   - Mastered the seamless integration of various components, tying together GitHub, S3, and CloudFront.

5. **Remote Changes with GitHub Actions:**
   - Learned to efficiently make remote changes to the resume by utilizing GitHub Actions.
   - Eliminated the need for manual cache invalidation in CloudFront after each resume update.