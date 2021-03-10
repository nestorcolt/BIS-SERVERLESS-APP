import requests
import json

# Amazon Endpoint
url = r"https://flex-capacity-na.amazon.com/regions"

# User Access Token (Este puede ser un access que se pida siempre con la cuenta de Gustavo FLEX)
token = "Atna|EwICIKIywTUWeRdx9WfrNRs5PqNsL7Y6_fASdjefoQsnmqBREuoH_qU1esF4jp7gbN-Q6VJap2vEqaWLSzCreIidmq4gj6ckb6f46CLcyFro9Z-wjzOcbpvkwpbb99ObNeEHx4h0yP3XIg21XHCHNBSObJvYAAi3gnh-9XvWIWwHZm6VvvRl7tVefEYaNpvFfGSPnIrKbKQt-Lw3BUJrHtD_9HefpAB0zP46Rcfsw4JcDFlgPtGPnX_DFpfUNmnswmOiSYwrHDv3Pk-MOblROTd8qI3RFr6NgLI9Z_tWvg2JNhObhg"
header = {"x-amz-access-token": token}

##############################################################################################
# Query all regions
query = requests.get(url=url, headers=header, timeout=10).json()

# Aqui lo guardo en un json, pero el query del response ya basta obvio
with open("./regions_response.json", "w") as writer:
    json.dump(dict(query), writer, indent=4, separators=[",", ":"])

##############################################################################################
