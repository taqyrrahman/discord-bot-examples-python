# This file contains all functions with api calls
# some apis collected from https://apipheny.io/free-api/
# additional list open api https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
# feel free to add ur own api

import requests

cat_fact_url = "https://catfact.ninja/fact"

def get_cat_facts():
    result = requests.get(cat_fact_url).json()
    # structure of json result = {"fact":"fact","length":0}
    return result["fact"]

