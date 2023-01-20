import os, requests

def login(request):
    """Sending request to auth service internal endpoint /login."""
    auth = request.authorization
    if not auth:
        return(None, ("Missing credentials", 401))

    basicAuth = (auth.username, auth.password)

    response = requests.post(
        url=f'http://{os.environ.get("AUTH_SVC_ADDRESS")}/login',
        auth=basicAuth,
    )

    if response.status_code == 200:
        return(response.text, None)

    return(None, (response.text, response.status_code))
