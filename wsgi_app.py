# Python has a built-in WSGI server
from wsgiref.simple_server import make_server

# All WSGI compliant applications must accept two variables:
#   a set of CGI environment variables (set by the server)
#   a callback for sending a response to the server (provided by the server)
def application(environ, start_response):
    response_body = 'Request method: {}'.format(environ['REQUEST_METHOD'])

    # Send status and headers to the server
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)

    # Return the response body to the server
    response = bytes(response_body, 'utf-8')
    return [response]       # Returned value must be iterable


# Instantiate a server
httpd = make_server(
    'localhost',
    8051,
    application
)

httpd.handle_request()
