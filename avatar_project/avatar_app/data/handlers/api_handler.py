import requests

def api_request(endpoint: str, method: str, data=None, params=None):
    
    method_list = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
    }
    
    if method.upper() not in method_list: raise ValueError(f"Invalid Method:{method}")

    request_type = method_list[method.upper()]
    
    response = request_type(endpoint, data=data, params=params)
    response.raise_for_status()
    return response.json()