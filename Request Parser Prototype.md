# Problem Description
The task is to create a request parser prototype to validate HTTP requests and parse their URL parameters. The prototype should handle both GET and POST requests, validating their authentication tokens and CSRF tokens (for POST requests). Once validated, the URL parameters should be parsed as a comma-separated string.

## Function Signature
```
def getResponses(valid_auth_tokens: List[str], requests: List[List[str]]) -> List[str]:
```
## Input
valid_auth_tokens: A list of strings representing the valid authentication tokens.
requests: A 2D list of strings representing the request types and URLs.
Output
The function should return a list of strings containing the responses for each request.

## Constraints
1 <= m (length of valid_auth_tokens) <= 2000
1 <= n (number of requests) <= 5000
12 <= length of each valid_auth_tokens[i]
Length of requests[i][1] <= 200

## Example 
```
valid_auth_tokens = ["ah37j2ha483u", "safh34ywbOp5", "ba34wyi8t9021"]
requests = [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"],
    ["POST", "https://example.com/?token=safh34ywbOp5&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
]

responses = getResponses(valid_auth_tokens, requests)
print(responses)

#Output
['INVALID', 'VALID,name,sam', 'INVALID', 'VALID,name,chris']

```

## Explanation
The first request has an authentication token 347sd6yk8iu2, which is not in the list of valid tokens. So the request is INVALID.
The second request has an authentication token safh34ywb0p5, which is in the list of valid tokens. The request is VALID, and the parameter is "name=sam".
The third request has an authentication token safh34ywbOp.5, which is in the list of valid tokens, but it is a POST request, and it lacks a valid CSRF token. So the request is INVALID.
The fourth request has an authentication token safh34ywb0p5, which is in the list of valid tokens. It also has a valid CSRF token ak2sh32dy (length >= 8). So the request is VALID, and the parameter is "name=chris".

# Code solution

```
def getResponses(valid_auth_tokens, requests):
    responses = []
    
    for request in requests:
        req_type, req_url = request
        
        # Extracting the token and parameters from the URL
        url_parts = req_url.split('?')
        params = {}
        
        if len(url_parts) == 2:
            param_str = url_parts[1]
            param_pairs = param_str.split('&')
            
            for pair in param_pairs:
                key, value = pair.split('=')
                params[key] = value
        
        # Validating the authentication token
        token = params.get('token')
        if token not in valid_auth_tokens:
            responses.append("INVALID")
            continue
        
        # Validating POST request with CSRF token
        if req_type == "POST":
            csrf_token = params.get('csrf')
            
            if csrf_token is None or not csrf_token.isalnum() or len(csrf_token) < 8:
                responses.append("INVALID")
                continue
        
        # Constructing the response string
        response_str = "VALID"
        if params:
            for key, value in params.items():
                response_str += f",{key},{value}"
        
        responses.append(response_str)
    
    return responses
```

# Solution Example 
```
valid_auth_tokens = ["ah37j2ha483u", "safh34ywbOp5", "ba34wyi8t9021"]
requests = [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"],
    ["POST", "https://example.com/?token=safh34ywbOp5&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
]

responses = getResponses(valid_auth_tokens, requests)
print(responses)

#Output
['INVALID', 'VALID,name,sam', 'INVALID', 'VALID,name,chris']

```
