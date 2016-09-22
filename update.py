#!/usr/bin/env python2.7

import requests
import json

s = requests.session()

# Update Headers
headers = {
    'Cache-Control': "no-cache",
    "Pragma": "no-cache",
    "Accept": "application/json",
    # "AuthToken": "",
    "User-Agent": "Mozilla/5.0 EA Download Manager Origin/9.12.1.43352",
    "X-Origin-UID": "17400363085085971258",
    "X-Origin-Platform": "PCWIN",
    "X-Origin-Client-Debug": "true",
    "localeInfo": "en_US",
    "Accept-Language": "en-US",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate"
}
s.headers.update(headers)

special_ids = [
    "OFB-EAST:109546867"  # BF4
]

how_many = 1500
offer_pat = "Origin.OFR.50.%s"
# offer_pat = "OFB-EAST:%s"
# offer_pat = "DR:%s"
url = "https://ecommerce2.dm.origin.com/ecommerce2/%s/%s/en_US?country=US&machine_hash=17400363085085971258"
url_new = "https://api2.origin.com/ecommerce2/%s/supercat/%s/en_US?country=US&lmd=1461618623000"
i = 1000

for i in range(i, i + how_many):
    try:
        offer_id = offer_pat % str(i).zfill(7)
        r = s.get(url % ("public", offer_id))
        # This version has no auth token so private offer requests are useless (unless you want to find out if something exists)
        # if r.status_code != 200:
        #     r = s.get(url % ("private", offer_id))
        if r.status_code != 200:
            continue
        else:
            r = r.json()
            print offer_id, r['localizableAttributes']['displayName'], r['localizableAttributes']['shortDescription']
            file_name = offer_id
            json.dump(r, open('offers/%s.json' % file_name, 'w'), sort_keys=True, indent=4)
    except Exception as e:
        print e.message
    # This is ugly as shit lol
    try:
        offer_id = offer_pat % str(i).zfill(7)
        r = s.get(url_new % ("public", offer_id))
        if r.status_code != 200:
            continue
        else:
            r = r.json()
            print offer_id, r['i18n']['displayName'], r['i18n']['shortDescription']
            file_name = offer_id
            json.dump(r, open('offers_new_api/%s.json' % file_name, 'w'), sort_keys=True, indent=4)
    except Exception as e:
        print e.message

for sid in special_ids:
    # print i
    try:
        r = s.get(url % ("public", sid))
        if r.status_code != 200:
            continue
        else:
            r = r.json()
            print sid, r['localizableAttributes']['displayName'], r['localizableAttributes']['shortDescription']
            file_name = sid
            json.dump(r, open('special_offers/%s.json' % file_name, 'w'), sort_keys=True, indent=4)
    except Exception as e:
        print e.message
