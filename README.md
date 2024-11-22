# Pracuj.pl Job Scraper

This project scrapes job offers from a website, stores them in a database, and sends notifications for new job offers to a Telegram channel. It is designed to run on AWS Lambda.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Configure the database and Telegram bot by editing `config.json`.

3. Deploy the project to AWS Lambda.

## Folder Structure

- `src/scrapper.py`: Contains functions to scrape job offers.
- `src/db.py`: Contains functions to interact with the database.
- `src/notify.py`: Contains functions to send notifications to Telegram.
- `src/lambda_function.py`: The entry point for the AWS Lambda function.
- `requirements.txt`: Lists the dependencies.
- `config.json`: Configuration file for database and Telegram bot.
- `README.md`: Project documentation.