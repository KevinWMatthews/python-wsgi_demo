# Instead of using wsgiref's simple_server, we can use a server provided by flup
# https://www.saddi.com/software/flup/

def application(environ, start_response):
    response_body = 'Hello, world!\n'

    # Send status and headers to the server
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)

    # Return response body to server
    return [response_body]

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(application).run()
