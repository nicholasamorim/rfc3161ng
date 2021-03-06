=========
rfc3161ng_async (aiohttp / tornado)
=========

.. image:: https://img.shields.io/pypi/l/rfc3161ng.svg
   :target: https://raw.githubusercontent.com/trbs/rfc3161ng/master/LICENSE

.. image:: https://travis-ci.org/trbs/rfc3161ng.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/trbs/rfc3161ng

.. image:: https://img.shields.io/pypi/v/rfc3161ng.svg
    :target: https://pypi.python.org/pypi/rfc3161ng/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/wheel/rfc3161ng.svg
    :target: https://pypi.python.org/pypi/rfc3161ng/
    :alt: Supports Wheel format

A simple client library for cryptographic timestamping service implementing the protocol from RFC3161 using async code.

This started as a fork of https://github.com/trbs/rfc3161ng and
is compatible only with Python 3.7+. This library includes support for aiohttp and `tornado <https://www.tornadoweb.org/en/stable/>`__ and `aiohttp <https://aiohttp.readthedocs.io/en/stable/>`__.

The latest version of this library is available from
https://github.com/nicholasamorim/rfc3161ng/ .


Public providers
================

There are several timestamping services around.  Here is a list of
publicly available services you can try:

 * http://freetsa.org/tsr
 * http://time.certum.pl
 * http://timestamp.comodoca.com/rfc3161
 * http://timestamp.geotrust.com/tsa
 * http://timestamp.globalsign.com/scripts/timstamp.dll
 * http://tsa.starfieldtech.com
 * https://teszt.e-szigno.hu:440/tsa

Example
=======

    >>> import rfc3161ng_async
    >>> rfc3161_async.api.HTTP_CLIENT = 'tornado'
    >>> certificate = open('data/certum_certificate.crt', 'rb').read()
    >>> rt = yield rfc3161ng_async.RemoteTimestamper('http://time.certum.pl', certificate=certificate)
    >>> tst = rt.timestamp(data=b'John Doe')
    >>> rt.check(tst, data=b'John Doe')
    True
    >>> rfc3161ng_async.get_timestamp(tst)
    datetime.datetime(2017, 8, 31, 15, 42, 58, tzinfo=tzutc())


Verifying timestamp using OpenSSL
=================================

One can verify the timestamp returned by the timeserver by using OpenSSL.
For example with:

  $ openssl ts -verify -data data_file.txt -in data_file.tsr -CAfile cacert.pem -untrusted tsa.crt

To save the tsr you can use code similar to:

    >>> from pyasn1.codec.der import encoder
    >>> import rfc3161ng_async
    >>> ...
    >>> timestamper = yield rfc3161ng_async.RemoteTimestamper('http://freetsa.org/tsr', certificate=certificate_data)
    >>> tsr = timestamper(data=data_file.read(), return_tsr=True)
    >>> with open("data_file.tsr", "wb") as f:
    >>>     f.write(encoder.encode(tsr))

Alternatively you can just save the raw `response.content` returned from the certification server.

There is a test which also covers this in `test_verify_timestamp_response_with_openssl`.


Authors
=======

 * Nicholas Amorim <nicholas@alienretro.com>
 * Benjamin Dauvergne <bdauvergne@entrouvert.com>
 * Michael Gebetsroither <michael@mgeb.org>
 * Bas van Oostveen <trbs@trbs.net>
