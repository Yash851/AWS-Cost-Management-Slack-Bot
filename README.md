# AWS-Cost-Management-Slack-Bot
This project is an AWS Cost Management bot that integrates with Slack to provide regular updates and insights about AWS costs. It leverages AWS services like Lambda, EventBridge, and Cost Explorer, and uses the Slack API to send automated notifications.

# Features
- Automated cost reporting for AWS services
- Real-time Slack notifications with detailed cost insights
- Scheduled cost checks using AWS EventBridge

# Technologies Used
- Backend: AWS Lambda, Amazon EventBridge, AWS Cloud Explorer
- Integration: Slack API
- Programming Language: Python (boto3, requests libraries)

# Setup Instructions
## Prerequisites
- AWS account
- Slack workspace with admin permissions
- Python environment

# Step-by-Step Guide
1. ## Clone the repository
2. ## Set Up AWS Lambda Function:
   - Create a new Lambda function in AWS.
   - Use the provided lambda_function.py file.
   - Ensure you have the necessary IAM roles with AWSBillingReadOnlyAccess.
3. ## Install Dependencies
   ### Set Up Your Local Environment
   1. #### Create a new directory:
      Create a directory to hold your lambda function code and dependencies.
      ```bash
      mkdir lambda_package
      cd lambda_package
    2. #### Install 'requests' and All Dependencies Locally:
       Use pip to install the requests library and its dependencies directly into your lambda_package root directory.
       ```bash
       pip install requests -t .
    3. #### Add the Lambda Function Code:
       Save your Lambda function code in a file named lambda_function.py inside the lambda_package directory.
  4. ## Zip the Lambda Function and Dependencies
     1. ### Navigate to the lambda_package directory
        ```bash
        cd lambda_package
      2. ### Zip the contents of the Directory:
         Zip the contents of the lambda_package directory, ensuring the dependecies and lambda_function.py are included in the root of the zip file.
         ```bash
         zip -r ../lambda_function.zip .
         cd ..
  5. ## Upload the Deployment Package to AWS Lambda:
     1. Open the AWS Lambda Console: Go to the AWS Management Console and navigate to the Lambda service.
     2. Select Your Lambda Function: Choose the Lambda function you want to update.
     3. Upload the Deployment Package:
        - Go to the "Code" tab.
        - Click "Upload from" and select ".zip file".
        - Click "Upload" and choose the lambda_function.zip file you created.
        - Save the changes.
  6. ## Ensure Correct Handler Configuration
     1. Open the AWS Lambda Console: Go to the Lambda function you want to update.
     2. Handler Configuration:
        - Ensure the handler is specified as lambda_function.lambda_handler in the "Configuration" tab under "Function code".
  7. ## Create and Invoke a Test Event
     1. Create a Test event
        - In the Lambda function console, go to the "Test" tab.
        - Create a new test event with the following JSON:
          ```JSON
          {
            "key1": "value1"
          }
      2. ## Invoke the lambda function:
         - With your test event selected, click the "Test" button to invoke the function.
         - Check the "Execution result" section for the status code and logs.
      3. ## Verify the message in Slack
         1. Open Slack: Go to your Slack workspace.
         2. Check the Channel: Look at the channel where the webhook is configured to post messages.
  # Creating a new workspace on Slack and creating WebHook URL
  1. ## Sign Up for Slack:
     - Go to Slack's Website.
     - Click on "Get Started" and then "Create a Workspace".
     - Follow the prompts to create an account and set up your new workspace.
  2. ## Set Up Your Workspace:
     - Enter your team name and customize your workspace URL.
     - Invite team members if necessary (you can skip this step if you prefer).
  3. # Create a Slack App and Add Incoming Webhooks:
     1. ## Create a Slack App:
        - Go to the Slack API.
        - Click on "Create an App".
        - Choose "From scratch" and give your app a name.
        - Select the workspace where you want to install your app.
     2. ## Enable Incoming Webhooks:
        - Once the app is created, go to the "Features" section and click on "Incoming Webhooks".
        - Turn on the "Activate Incoming Webhooks" toggle.
     3. ## Create a Webhook URL:
        - Scroll down to the "Webhook URLs for Your Workspace" section and click on "Add New Webhook to Workspace".
        - Select the channel where you want to post messages and click "Allow".
        - A new webhook URL will be generated. Copy this URL, as you will need it for your Lambda function.
  # Configure Environment Variables in Your Lambda Function
  1. ## Set Environment Variables:
     - In the AWS Lambda console, go to your function and click on "Configuration".
     - In the "Environment variables" section, add a new variable:
       - Key: SLACK_WEBHOOK_URL
       - Value: (Paste your Slack webhook URL here)
