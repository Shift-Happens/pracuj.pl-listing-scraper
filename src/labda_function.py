import json
import logging
from scrapper import requ_pracuj, extract_job_offers
from db import add_or_update_offers, create_table
from notify import notify_new_offers

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Ensure table exists
        create_table()
        
        # Fetch and process offers
        content = requ_pracuj()
        offers = extract_job_offers(content)
        logger.info(f"Found {len(offers)} total offers")
        
        # Store new offers
        new_offers = add_or_update_offers(offers)
        logger.info(f"Found {len(new_offers)} new offers")
        
        # Notify if new offers found
        if new_offers:
            notify_new_offers(new_offers)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Job offers processed successfully',
                'total_offers': len(offers),
                'new_offers': len(new_offers)
            })
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }