# Python has a built-in WSGI server
from wsgiref.simple_server import make_server

SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 8051

# This WSGI application is a function
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
    response_body = bytes(response_body, 'utf-8')
    return [response_body]       # Returned value must be iterable


# Instantiate a server
httpd = make_server(
    SERVER_HOSTNAME,
    SERVER_PORT,
    application
)

print('Listening for a single request at {}:{}'.format(SERVER_HOSTNAME, SERVER_PORT))
httpd.handle_request()
