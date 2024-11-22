# Pracuj.pl Job Scraper - AWS Lambda Edition

Automated job scraper that monitors Pracuj.pl for new job offers, stores them in DynamoDB, and sends notifications via Telegram.

## Architecture

- **AWS Lambda Function**: Runs hourly to fetch and process job listings
- **DynamoDB**: Stores job offers and tracks new listings
- **Telegram Bot**: Delivers notifications about new job opportunities
- **AWS EventBridge**: Triggers the Lambda function on schedule

## Prerequisites

1. AWS Account and CLI
```bash
aws configure
```

2. AWS SAM CLI ([installation guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html))

3. Python 3.12+

4. Telegram Bot ([creation guide](https://core.telegram.org/bots#how-do-i-create-a-bot))

## Configuration

1. Environment Variables (stored in AWS Lambda):
```
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_CHAT_ID=your-chat-id
```

2. AWS SAM Parameters (in template.yaml):
```yaml
Parameters:
  TelegramBotToken:
    Type: String
  TelegramChatId:
    Type: String
```

3. DynamoDB Configuration (in src/db.py):
```python
table_name = 'job_offers'  # Customize table name if needed
```

4. Job Search Configuration (in src/scrapper.py):
```python
url = 'https://it.pracuj.pl/praca/devops%20engineer;kw'  # Modify search criteria
```

## Deployment

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Deploy using SAM:
```bash
python deploy.py
```

Follow the prompts to configure:
- Stack name (e.g., `job-scraper`)
- AWS Region
- Telegram credentials
- Scheduling preferences

## Customization

### Notification Format
Edit 

notify.py

 to modify message format:
```python
def format_offer(offer):
    # Customize message template
```

### Schedule
Modify in 

template.yaml

:
```yaml
Events:
  HourlyTrigger:
    Type: Schedule
    Properties:
      Schedule: rate(1 hour)  # Customize interval
```

### Search Criteria
Update in 

scrapper.py

:
```python
def requ_pracuj():
    url = 'https://it.pracuj.pl/praca/your-search-term;kw'
```

### DynamoDB Capacity
Adjust in 

db.py

:
```python
ProvisionedThroughput={
    'ReadCapacityUnits': 5,  # Customize based on load
    'WriteCapacityUnits': 5
}
```

## Monitoring

- CloudWatch Logs: `/aws/lambda/job-scraper-JobScraperFunction-*`
- DynamoDB Metrics: Monitor table throughput and capacity
- Lambda Metrics: Duration, invocations, errors

## Troubleshooting

1. **Lambda Timeout**: Increase timeout in 

template.yaml

 (default: 30s)
2. **DynamoDB Capacity**: Adjust provisioned throughput if hitting limits
3. **Telegram Errors**: Verify bot token and chat ID in environment variables
4. **Scraping Issues**: Check URL format and website changes

## Security

- AWS IAM: Function uses minimal required permissions via DynamoDBCrudPolicy
- Environment Variables: Sensitive data stored in Lambda environment
- Telegram: Bot token restricted to single chat ID

## Cost Considerations

- Lambda: Free tier includes 1M requests/month
- DynamoDB: Free tier includes 25 WCU/RCU
- CloudWatch: Basic monitoring included

## Contributing

1. Fork the repository
2. Create feature branch
3. Update relevant files
4. Add tests if applicable
5. Submit pull request
