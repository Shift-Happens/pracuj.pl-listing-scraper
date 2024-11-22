import requests
import json
def requ_pracuj():
    cookies = {
        'gpc_v': '1',
        'gpc_analytic': '1',
        'gpc_func': '1',
        'gpc_ad': '1',
        'gpc_audience': '1',
        'gpc_social': '1',
        '_gcl_au': '1.1.1911144700.1729952332',
        '_hjSessionUser_432317': 'eyJpZCI6ImY4NjRhNGM0LWY5OTMtNTVkYi1iMGMzLWU4MDU2NWMxOThhYSIsImNyZWF0ZWQiOjE3Mjk5NTIzMzI5MDEsImV4aXN0aW5nIjp0cnVlfQ==',
        '_fbp': 'fb.1.1729952333053.84694295513475338',
        'gp__cfXfiDZP': '34',
        'gptrackCookie': '56261268-6a09-4349-y82f-441ddc46536a',
        '_ga_GD4CKCV28E': 'GS1.1.1730835364.1.1.1730835424.0.0.0',
        '_hjSessionUser_327300': 'eyJpZCI6IjY3ZmIzMjY0LTcxZTYtNWU1Ny04YmNjLWE5MTY0OGE1OGNlNSIsImNyZWF0ZWQiOjE3MzEzMjkwNTI2MTgsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_CJXS9Q5W6G': 'GS1.1.1731329052.1.1.1731329071.41.0.0',
        'gp_ab__testSearchAllKeyword__221': 'B',
        '__cf_bm': 's9QPXwParfYiJewcb6.kIjo8DJ1uiMhS1hGooEbH.t4-1732299475-1.0.1.1-WLz5m1cURJ4lu7BEOB3NDeznreqegvVpUF2LY1.n3vuSCRp_mIQSKXte34bP7GRu1_omniuoTzeuuMx_xpuQgA',
        '_cfuvid': 'u35n9f7bCv6e0IwO4BwlFLH3klQ0tQujA6CcbYUG.WQ-1732299475963-0.0.1.1-604800000',
        '__cfruid': '9f828c577f4bf69b649d3c5cb49e0e1123eb215d-1732299476',
        'gp_lang': 'pl',
        'cf_clearance': '1.I8Vj74EPTgWSU8J9EGAhT8U_IPkwbXUCAEf_fnLKQ-1732299477-1.2.1.1-FozVTEWA1I_xUhUJiFfJ3xkffoVnhyBFDxroRDQvjRLWM9XjCGLW5vV.zNaoRJ8TdeO_ZA.WrbtVYMJYMM_Kk_GPy5vVMMPonA7wP2i10FaPDmhjS.d3WDJfGFXSLC7cwefHT1683HHuLzYlslL2QcFLjPKBmG53GetzkWhkxITvi_nlEtmOletclzOnCIZO123ckWEpXYLsodUTH0tPdImay98b9UyBF28uWkxEkhhYX93zMfnPx9.Q2Vh1cIdOiBWN5sLwDbnQ8z2ZKFpCW1dtQG7n9bCTKvgf_VOZMywKidykuqVqLH.fddyE2R97JvRFCsKn8fms4pLoeH830lhXPyxRtnbCKOqVU6ZE8DEZNqWiFfyHPMORswy7sStR',
        '_gpantiforgery': 'CfDJ8BnsG4UujmlAhMc6W89smJaLpEUBoRwDk5FRxKIbenPiy9cZ2Df2Hq6GCyzaKRhMrtRsSgpj35JIYOFsXRN4jT_OxY2grIRaYO_QR2jCeJwh2ePi28xY9vPitzkMXUFjhMBgtwmDGXWmtvAprvfJuvI',
        '_ga': 'GA1.2.83705216.1730835350',
        '_gid': 'GA1.2.808708234.1732299480',
        '_uetsid': '1b493f90a8fe11efb283b780493639d9',
        '_uetvid': '94a4d290c92611ee97877dbfc5ecb9bb',
        '_clck': '6ki113%7C2%7Cfr3%7C0%7C1770',
        'cto_bundle': 'Muorrl9nSlZGSmhhVzAlMkY1amFSNDU2cjFKUWk5Q2pNNTQ1M3NSbWZwVjhPamM0c1ZxSGVsWmVxNyUyRklScE9FSHRicUxiM2YydU9zJTJGdWZHZmhtV0k0bHZvZG1CejFLeVZxc081OW5WUnlzU012d0hjWnVzVm1SNzg3b0NxMFpRMVg3TVBlbmc4N2psbmtCTkRxMEdQS1p5ejd6TUElM0QlM0Q',
        '__gfp_64b': 'aUHcyIJn3vCnQ9t522aYeCOSagI8ACVgaVcsdEJIkO3.U7|1729952331|2',
        '_clsk': 'ocura3%7C1732299481721%7C1%7C0%7Cw.clarity.ms%2Fcollect',
        '_ga_DD6PPTKNH1': 'GS1.1.1732299479.3.0.1732299485.54.0.0',
        '_ga_WDELMMFCBH': 'GS1.1.1732299479.3.0.1732299486.53.0.0',
        'XSRF-TOKEN': 'CfDJ8BnsG4UujmlAhMc6W89smJacX9FV7Rf3Lq5sY8Y-mfXXytCbuv11oqcRqSF34Ex7eotWcvrj4kdVdksv-SlseGb2_Uz4AmbsKS5r_g1XNX8vWbroUIqAANUxFpGF6gQvl76U8uVFfI9iOgf1HTkmrBM',
        'gptrackPVID': '3c6fae3d-8425-43e1-y6be-599ba0b9e4b6',
    }

    headers = {
        'authority': 'it.pracuj.pl',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'gpc_v=1; gpc_analytic=1; gpc_func=1; gpc_ad=1; gpc_audience=1; gpc_social=1; _gcl_au=1.1.1911144700.1729952332; _hjSessionUser_432317=eyJpZCI6ImY4NjRhNGM0LWY5OTMtNTVkYi1iMGMzLWU4MDU2NWMxOThhYSIsImNyZWF0ZWQiOjE3Mjk5NTIzMzI5MDEsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1729952333053.84694295513475338; gp__cfXfiDZP=34; gptrackCookie=56261268-6a09-4349-y82f-441ddc46536a; _ga_GD4CKCV28E=GS1.1.1730835364.1.1.1730835424.0.0.0; _hjSessionUser_327300=eyJpZCI6IjY3ZmIzMjY0LTcxZTYtNWU1Ny04YmNjLWE5MTY0OGE1OGNlNSIsImNyZWF0ZWQiOjE3MzEzMjkwNTI2MTgsImV4aXN0aW5nIjp0cnVlfQ==; _ga_CJXS9Q5W6G=GS1.1.1731329052.1.1.1731329071.41.0.0; gp_ab__testSearchAllKeyword__221=B; __cf_bm=s9QPXwParfYiJewcb6.kIjo8DJ1uiMhS1hGooEbH.t4-1732299475-1.0.1.1-WLz5m1cURJ4lu7BEOB3NDeznreqegvVpUF2LY1.n3vuSCRp_mIQSKXte34bP7GRu1_omniuoTzeuuMx_xpuQgA; _cfuvid=u35n9f7bCv6e0IwO4BwlFLH3klQ0tQujA6CcbYUG.WQ-1732299475963-0.0.1.1-604800000; __cfruid=9f828c577f4bf69b649d3c5cb49e0e1123eb215d-1732299476; gp_lang=pl; cf_clearance=1.I8Vj74EPTgWSU8J9EGAhT8U_IPkwbXUCAEf_fnLKQ-1732299477-1.2.1.1-FozVTEWA1I_xUhUJiFfJ3xkffoVnhyBFDxroRDQvjRLWM9XjCGLW5vV.zNaoRJ8TdeO_ZA.WrbtVYMJYMM_Kk_GPy5vVMMPonA7wP2i10FaPDmhjS.d3WDJfGFXSLC7cwefHT1683HHuLzYlslL2QcFLjPKBmG53GetzkWhkxITvi_nlEtmOletclzOnCIZO123ckWEpXYLsodUTH0tPdImay98b9UyBF28uWkxEkhhYX93zMfnPx9.Q2Vh1cIdOiBWN5sLwDbnQ8z2ZKFpCW1dtQG7n9bCTKvgf_VOZMywKidykuqVqLH.fddyE2R97JvRFCsKn8fms4pLoeH830lhXPyxRtnbCKOqVU6ZE8DEZNqWiFfyHPMORswy7sStR; _gpantiforgery=CfDJ8BnsG4UujmlAhMc6W89smJaLpEUBoRwDk5FRxKIbenPiy9cZ2Df2Hq6GCyzaKRhMrtRsSgpj35JIYOFsXRN4jT_OxY2grIRaYO_QR2jCeJwh2ePi28xY9vPitzkMXUFjhMBgtwmDGXWmtvAprvfJuvI; _ga=GA1.2.83705216.1730835350; _gid=GA1.2.808708234.1732299480; _uetsid=1b493f90a8fe11efb283b780493639d9; _uetvid=94a4d290c92611ee97877dbfc5ecb9bb; _clck=6ki113%7C2%7Cfr3%7C0%7C1770; cto_bundle=Muorrl9nSlZGSmhhVzAlMkY1amFSNDU2cjFKUWk5Q2pNNTQ1M3NSbWZwVjhPamM0c1ZxSGVsWmVxNyUyRklScE9FSHRicUxiM2YydU9zJTJGdWZHZmhtV0k0bHZvZG1CejFLeVZxc081OW5WUnlzU012d0hjWnVzVm1SNzg3b0NxMFpRMVg3TVBlbmc4N2psbmtCTkRxMEdQS1p5ejd6TUElM0QlM0Q; __gfp_64b=aUHcyIJn3vCnQ9t522aYeCOSagI8ACVgaVcsdEJIkO3.U7|1729952331|2; _clsk=ocura3%7C1732299481721%7C1%7C0%7Cw.clarity.ms%2Fcollect; _ga_DD6PPTKNH1=GS1.1.1732299479.3.0.1732299485.54.0.0; _ga_WDELMMFCBH=GS1.1.1732299479.3.0.1732299486.53.0.0; XSRF-TOKEN=CfDJ8BnsG4UujmlAhMc6W89smJacX9FV7Rf3Lq5sY8Y-mfXXytCbuv11oqcRqSF34Ex7eotWcvrj4kdVdksv-SlseGb2_Uz4AmbsKS5r_g1XNX8vWbroUIqAANUxFpGF6gQvl76U8uVFfI9iOgf1HTkmrBM; gptrackPVID=3c6fae3d-8425-43e1-y6be-599ba0b9e4b6',
        'referer': 'https://www.pracuj.pl/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }

    response = requests.get('https://it.pracuj.pl/praca/aws%20administrator;kw', cookies=cookies, headers=headers)
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