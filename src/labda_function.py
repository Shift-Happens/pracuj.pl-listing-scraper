from scrapper import requ_pracuj, extract_job_offers
from db import add_or_update_offers, create_table
from notify import notify_new_offers

def lambda_handler(event, context):
    create_table()
    content = requ_pracuj()
    offers = extract_job_offers(content)
    new_offers = add_or_update_offers(offers)
    notify_new_offers(new_offers)
    return {
        'statusCode': 200,
        'body': 'Job offers processed successfully'
    }