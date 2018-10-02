# Serve or deny content based on an IP address list (whose address?)

from wsgiref.simple_server import make_server, demo_app

SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 8051

class AuthenticationMiddleware:
    """
    A modified version of an original example at:
    http://isapi-wsgi.python-hosting.com/wiki/WSGI-Gateway-or-Glue
    """
    def __init__(self, app, allowed_addresses):
        """
        @param app: the WSGI app we will that comes after us                eh?
        @param allowed_addresses: list of remote addresses from which to allow access
        """
        self.app = app
        self.allowed_addresses = allowed_addresses

    def __call__(self, environ, start_response):
        """The standard WSGI interface"""
        addr = environ.get('REMOTE_ADDR','UNKNOWN')
        if addr in self.allowed_addresses:
            # pass through to the next app
            return self.app(environ, start_response)
        else:
            # put up a response denied
            start_response( '403 Forbidden', [('Content-type', 'text/html')])
            return ['You are forbidden to view this resource'.encode('utf-8')]

# addresses = [SERVER_HOSTNAME]       # 403 Forbidden
address = ['127.0.0.1']             # Succeeds
simple_app_with_auth = AuthenticationMiddleware(demo_app, addresses)

if __name__ == '__main__':
    httpd = make_server('', SERVER_PORT, simple_app_with_auth)
    print("Serving HTTP on {}:{}".format(SERVER_HOSTNAME, SERVER_PORT))
    # Respond to requests until process is killed
    httpd.serve_forever()
