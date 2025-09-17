import json
import ee
import os


def init_gee():
    service_account = os.getenv("EE_SERVICE_ACCOUNT")
    private_key = os.getenv("EE_PRIVATE_KEY")

    if service_account and private_key:
        credentials = ee.ServiceAccountCredentials(service_account, key_data=private_key)
        ee.Initialize(credentials)
    else:
        ee.Initialize()  # fallback (for local auth)

init_gee()

def fetch_spei():
    """Fetch SPEI data from GEE (simplified demo)."""
    dataset = ee.ImageCollection("CSIRO/SPEI/01/monthly")
    region = ee.Geometry.Rectangle([30, 5, 40, 15])
    
    values = dataset.select("spei").mean().reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=5000
    ).getInfo()

    return values

def save_latest_data():
    data = fetch_spei()
    with open("app/data/latest_spei.json", "w") as f:
        json.dump(data, f)

def get_latest_data():
    with open("app/data/latest_spei.json", "r") as f:
        return json.load(f)
