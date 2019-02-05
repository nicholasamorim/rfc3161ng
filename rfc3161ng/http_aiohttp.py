import aiohttp

SESSION = None
HTTP_EXCEPTIONS = (aiohttp.ClientResponseError, )


async def run_request(url, data, headers, timeout=10):
    """Uses aiohttp to perform a request.
    """
    global SESSION
    if not SESSION:
        SESSION = session = aiohttp.ClientSession()

    async with SESSION:
        request = session.post(url, data=data, headers=headers, timeout=timeout)
        async with request as response:
            response.raise_for_status()
            content = await response.read()

    return content
