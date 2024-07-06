# Save the following code in lambda_package/lambda_function.py

import json
import boto3
from datetime import datetime, timedelta
import requests
import os

def format_slack_message(total_cost, service_costs):
    message = {
        "text": "AWS Cost Report",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Total AWS cost for the last 30 days:* ${total_cost}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Cost by Service:*"
                }
            }
        ]
    }

    for service in service_costs:
        service_name = service['Keys'][0]
        service_cost = service['Metrics']['BlendedCost']['Amount']
        message['blocks'].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{service_name}: ${service_cost}"
                }
            }
        )

    return message

def lambda_handler(event, context):
    client = boto3.client('ce', region_name='us-east-1')

    end = datetime.today().strftime('%Y-%m-%d')
    start = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

    # Get total blended cost
    response = client.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='MONTHLY',
        Metrics=['BlendedCost']
    )

    total_cost = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']

    # Get cost by service
    response_by_service = client.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='MONTHLY',
        Metrics=['BlendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    service_costs = response_by_service['ResultsByTime'][0]['Groups']

    # Prepare the Slack message
    slack_message = format_slack_message(total_cost, service_costs)

    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']

    try:
        slack_response = requests.post(slack_webhook_url, data=json.dumps(slack_message), headers={'Content-Type': 'application/json'})
        slack_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request to Slack failed: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Failed to send message to Slack: {e}')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to Slack')
    }
