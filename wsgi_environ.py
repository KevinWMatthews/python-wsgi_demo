import wsgiref.simple_server

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
    'localhost',
    8051,
    application
)

httpd.handle_request()
