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


## WSGI Application Spec

A WSGI application can be deceptively simple.

The WSGI application must be callable:

  * a function
  * a method
  * a class or instance with an object.__call__() method

This callable must accept two variables:

  * a set of CGI environment variables (set by the server)
  * a callback for sending a response to the server (provided by the server)

The server's callback is required to accept two arguments:

  * HTTP response code and message
  * response headers (iterable?)

Applications are expected to execute the callback and provide these arguments.


## Links

This tutorial is take from [codepoint.net](http://wsgi.tutorial.codepoint.net/intro)
Also learn about [parsing GET](http://wsgi.tutorial.codepoint.net/parsing-the-request-get)
and [parsing POST](http://wsgi.tutorial.codepoint.net/parsing-the-request-post) requests.

[flup](https://www.saddi.com/software/flup/)
