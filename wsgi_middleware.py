import wsgiref.simple_server

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

if __name__ == '__main__':
    httpd = wsgiref.simple_server.make_server(
        SERVER_HOSTNAME,
        SERVER_PORT,
        simple_app
    )
    print('Listening for a single request at {}:{}'.format(SERVER_HOSTNAME, SERVER_PORT))
    httpd.handle_request()
