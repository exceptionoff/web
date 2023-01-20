#! /usr/bin/python
#
def myapp(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    qs: str = environ["QUERY_STRING"]

    return qs.replace("&", "\n")
    # return qs.split("&")