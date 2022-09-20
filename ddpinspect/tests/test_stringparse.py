"""
Tests to determine the functionality of functions in the parserlib module

Tests can be added and changed when needed
"""

import pytest
from parserlib import stringparse

@pytest.mark.parametrize("test_timestamp, expected", [
    ("2005-10-30 T 10:45 UTC", True),
    ("2007-11-09 T 11:20 UTC", True),
    ("Sat Jul 23 02:16:57 2005", True),
    ("2009-10-31T01:48:52Z", True),
    ("1969-07-21 T 02:56 UTC", True),
    ("07:38, 11 December 2012", True)
])
def test_is_timestamp(test_timestamp: str, expected: bool) -> None:
    """
    test stringparse.is_timestamp
    """
    assert stringparse.is_timestamp(test_timestamp) is expected,\
        f"Timestamp: {test_timestamp} is not identified as bool: {expected}"


@pytest.mark.parametrize("test_url, is_exact_url, expected", [
    ("www.url.com",                                    True,  True),
    ("https://banaan.com",                             True,  True),
    ("http://frikandelspeciaal.nl",                    True,  True),
    (" http://frikandelspeciaal.nl",                   True,  False),
    ("htp://frikandelspeciaal.nl",                     True,  False),
    ("     www.url.com",                               False, True),
    ("https://banaan.com check check",                 False, True),
    ("!@#%$%&$&https://frikandelspeciaal.nl*#@$^*^@#", False, True),
    ("  htp://frikandelspeciaal.nl ",                  False, True),
    ("        frikandelspeciaal.nl ",                  False, True),
])
def test_has_url(test_url: str, is_exact_url: bool, expected: bool) -> None:
    """
    test stringparse.has_url
    """
    assert stringparse.has_url(test_url, is_exact_url) is expected,\
        f"url: {test_url} in exact mode: {is_exact_url}, it should be bool: {expected}"


@pytest.mark.parametrize("test_email, is_exact_email, expected", [
    # These should evaluate to True
    (r'simple@example.com', True, True),
    (r'very.common@example.com', True, True),
    (r'disposable.style.email.with+symbol@example.com', True, True),
    (r'other.email-with-hyphen@example.com', True, True),
    (r'fully-qualified-domain@example.com', True, True),
    (r'user.name+tag+sorting@example.com', True, True),
    (r'x@example.com', True, True),
    (r'example-indeed@strange-example.com', True, True),
    (r'test/test@test.com', True, True),
    (r'example@s.example', True, True),
    (r'"john..doe"@example.org', True, True),
    (r'mailhost!username@example.org', True, True),
    (r'"very.(), :;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com', True, True),
    (r'user%example.com@example.org', True, True),
    (r'user-@example.org', True, True),
    (r'postmaster@[123.123.123.123]', True, True),
    # These should evaluate to True, but the current implementation evaluate them to False
    (r'postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]', True, False),
    (r'admin@mailserver1', True, False),
    (r'""@example.org ', True, False),
    # These should evaluate to False
    (r'Abc.example.com', True, False),
    ('A@b@c@example.co', True, False),
    (r'a"b(c)d,e:f;g<h>i[j\k]l@example.co', True, False),
    (r'just"not"right@example.co', True, False),
    (r'this is"not\allowed@example.co', True, False),
    (r'this\ still\"not\\allowed@example.co', True, False),
    (r'i_like_underscore@but_its_not_allowed_in_this_part.example.co', True, False),
    # These should evaluate to False, but the current implementation evaluate them to True
    (r'1234567890123456789012345678901234567890123456789012345678901234+x@example.co', True, True)
])
def test_has_email(test_email: str, is_exact_email: bool, expected: bool) -> None:
    """
    test stringparse.has_url

    Note a perfect regex does not exist.
    Determine whether the outcome of these test yourself
    """
    assert stringparse.has_email(test_email, is_exact_email) is expected,\
        f"email: {test_email} in exact mode: {is_exact_email}, it should be bool: {expected}"


@pytest.mark.parametrize("test_ip, expected", [
    ("127.0.0.1",                              True),
    ("1788727.0.0.1",                          False),
    ("127.0.0.256",                            False),
    ("2001:db8:3333:4444:5555:6666:7777:8888", True),
    ("2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF", True),
    ("2001:db8:3333:4444:CQCC:DDDD:EEEE:FFFF", False),
])
def test_is_ipaddress(test_ip: str, expected: bool) -> None:
    """
    test stringparse.has_ip
    """
    assert stringparse.is_ipaddress(test_ip) is expected,\
        f"ip: {test_ip}, it should be bool: {expected}"
