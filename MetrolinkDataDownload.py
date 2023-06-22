import requests
import json
import time
from requests.auth import HTTPBasicAuth
import random

url = 'https://metrolinktrains.com/rtt/TrainList.json'


while True:
    current_time = time.time()
    current_locations = requests.get(url,headers={'User-Agent':'curl/8.0.1'})
    time.sleep(60+random.randint(0,9))
    if len(current_locations.json()) < 1:
        continue
    with open(str(current_time)+"_metrolink_current_locations.json", "w") as outfile:
        outfile.write(json.dumps(current_locations.json(), indent=4))
