from datetime import datetime
from pytz import timezone
import requests
import json

# Amazon Endpoint
url = r"https://flex-capacity-na.amazon.com/scheduledAssignments"

# User Access Token (Este puede ser un access que se pida siempre con la cuenta de Gustavo FLEX)
token = "Atna|EwICIOIc0qIG2foDskb8f5Zqan4frZnX13DgAU3zB5tbunnyqicz_vYd77xUpbvYtLEWZnxBMIJPIzEUlj6QEN1-GqyQAnmMXgY_k4Cs6OpR_xBdIpDrSPtgUbmbpKPfEV4r4z45SUvghNNtIzPfm2MpaGqkHaj-RwmaWWNk-TMBowU9gFLqC29DyjyCTYjmcz-oan-LMDq0BQ5VLFaWBePvti4T0lcZgBoWZ1wK7N160SUbPCEgNN0PwAQoy6VEyInb2p4e1YJr5ZdxuNVxweP-uGXP1K9d-R5TfnMB89NZCd4TIg"
header = {"x-amz-access-token": token}

##############################################################################################
# Query
query = requests.get(url=url, headers=header, timeout=10).json()
# block = query["scheduledAssignments"][0]

# start = block["startTime"]
# end = block["endTime"]


dtime = datetime.fromtimestamp(1615673700)
print(dtime.astimezone(timezone('US/Eastern')))

dtime = datetime.fromtimestamp(1615684500)
print(dtime.astimezone(timezone('US/Eastern')))

##############################################################################################
