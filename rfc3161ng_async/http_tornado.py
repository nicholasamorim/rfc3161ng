from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
HTTP_EXCEPTIONS = (HTTPError, )


async def run_request(url, data, headers, timeout=10):
    """Uses tornado to perform a request.
    """
    request = HTTPRequest(
        url, method='POST', body=data,
        request_timeout=timeout, headers=headers)
    response = await AsyncHTTPClient().fetch(request)
    return response.body
