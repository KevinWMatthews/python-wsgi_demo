import wsgiref.simple_server

# Set to false to send a response from the middleware
PASS_DOWN_STACK = True

SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 8051

def simple_app(environ, start_response):
    response_body = 'Hello, World!\n'.encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)
    return [response_body]

class Middleware():
    ''' Middleware that passes data down the WSGI stack '''

    # Server interface?
    def __init__(self, app):
        '''
        "Wrap" the application.
        This allows us to capture (and process) all calls to and
        responses from the application.
        '''
        self.wrapped_app = app

    # WSGI application interface:
    #   a class that contains a __call__() method
    def __call__(self, environ, start_response):
        if PASS_DOWN_STACK:
            # Pass data down the WSGI stack
            # Let the wrapped app execute the server's callback
            #
            # We could edit this response if we wanted to?
            return self.wrapped_app(environ, start_response)
        else:
            # Send a response to the server without passing data to the app below
            response_body = 'Response from middleware\n'.encode('utf-8')
            status = '403 Forbidden'
            response_headers = [
                ('Content-Type', 'text/plain'),
                ('Content-Length', str(len(response_body))),
            ]
            start_response(status, response_headers)
            return [response_body]


if __name__ == '__main__':
    middleware = Middleware(simple_app)

    httpd = wsgiref.simple_server.make_server(
        SERVER_HOSTNAME,
        SERVER_PORT,
        middleware
    )
    print('Listening for a single request at {}:{}'.format(SERVER_HOSTNAME, SERVER_PORT))
    httpd.handle_request()
