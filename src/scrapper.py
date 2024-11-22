import requests
import json

def requ_pracuj():
    url = 'https://it.pracuj.pl/praca/aws%20administrator;kw'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    return response.text

def extract_job_offers(json_text):
    # Find the script tag with __NEXT_DATA__
    start = json_text.find('<script id="__NEXT_DATA__" type="application/json">')
    end = json_text.find('</script>', start)
    
    # Extract and parse JSON
    json_data = json_text[start:end].split('>', 1)[1]
    data = json.loads(json_data)
    
    # Get the job offers
    offers = data['props']['pageProps']['data']['jobOffers']['groupedOffers']
    
    return [
        {
            'id': offer['id'],
            'title': offer['jobTitle'],
            'company': offer['companyName'],
            'technologies': offer['technologies'],
            'salary': offer['salaryDisplayText'],
            'work_modes': offer['workModes'],
            'contract_types': offer['typesOfContract'],
            'workplace': [o['displayWorkplace'] for o in offer['offers']]
        }
        for offer in offers
    ]

def analyze_offers(offers):
    # Technology analysis
    all_techs = []
    for offer in offers:
        all_techs.extend(offer['technologies'])
    
    tech_count = {}
    for tech in all_techs:
        tech_count[tech] = tech_count.get(tech, 0) + 1
        
    print("\nMost common technologies:")
    for tech, count in sorted(tech_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{tech}: {count}")

    # Work mode analysis
    work_modes = []
    for offer in offers:
        work_modes.extend(offer['work_modes'])
    
    mode_count = {}
    for mode in work_modes:
        mode_count[mode] = mode_count.get(mode, 0) + 1
        
    print("\nWork modes distribution:")
    for mode, count in mode_count.items():
        print(f"{mode}: {count}")

# To use:
content = requ_pracuj()
offers = extract_job_offers(content)
analyze_offers(offers)