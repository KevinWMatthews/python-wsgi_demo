# WSGI

WSGI is a Python spec, [PEP 3333](https://www.python.org/dev/peps/pep-3333).

It details how a server and an application can communicate.

## Background

A WSGI compliant server can:

  * Receive a request from a client
  * Pass this request to an application
  * Receive the application's response
  * Send this response to the client

That's it. It can not create a response.

A WSGI compliant application can:

  * ?
  * Receive a request from a server
  * Create a response
  * Send this response to the server

WSGI applications can be stacked. This middleware behaves as

  * an application to the application on top of it
  * as a server to the application below it
