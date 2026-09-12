def https_server(status):
    match status:
        case 200:
            return "success"
        case 400:
            return "Bad request"
        case 401:
            return "Authentication error"
        case 404:
            return "page not found"
print(https_server(200))
