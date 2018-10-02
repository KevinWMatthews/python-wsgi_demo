import wsgiref.simple_server

SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 8051

def application(environ, start_response):
    response_body = []
    for key, value in sorted(environ.items()):
        response_body.append('{}: {}'.format(key, value))
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)
    response = bytes(response_body, 'utf-8')
    return [response]

httpd = wsgiref.simple_server.make_server(
    SERVER_HOSTNAME,
    SERVER_PORT,
    application
)

print('Listening for a single request at {}:{}'.format(SERVER_HOSTNAME, SERVER_PORT))
httpd.handle_request()
