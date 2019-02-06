import aiohttp

HTTP_EXCEPTIONS = (aiohttp.ClientResponseError, )


async def run_request(url, data, headers, timeout=10):
    """Uses aiohttp to perform a request.
    """
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        request = session.post(url, data=data, headers=headers, timeout=timeout)
        async with request as response:
            content = await response.read()

    return content
