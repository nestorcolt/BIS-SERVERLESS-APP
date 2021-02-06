import boto3

USER_POOL_NAME = "bis-api-gateway-cognito-pool"
client = boto3.client('cognito-idp')


##############################################################################################
def authenticate_and_get_token():
    config = get_cognito_configuration()

    resp = client.admin_initiate_auth(
        UserPoolId=config["pool"],
        ClientId=config["client"],
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            "USERNAME": "web",
            "PASSWORD": "Cognito18990129e!"
        }
    )

    print("Log in success")
    print("Access token:", resp['AuthenticationResult']['AccessToken'])
    print("Refresh token:", resp['AuthenticationResult']['RefreshToken'])
    print("ID token:", resp['AuthenticationResult']['IdToken'])
    print(resp)


##############################################################################################

def get_cognito_configuration():
    pools = [itm for itm in client.list_user_pools(MaxResults=10)["UserPools"] if itm["Name"] == USER_POOL_NAME]

    if pools:
        client_apps = client.list_user_pool_clients(UserPoolId=pools[0]["Id"])["UserPoolClients"]

        if client_apps:
            return {"pool": pools[0]["Id"], "client": client_apps[0]["ClientId"]}


##############################################################################################
authenticate_and_get_token()
