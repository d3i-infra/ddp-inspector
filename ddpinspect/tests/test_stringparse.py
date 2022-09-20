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
        f"Timestamp: {test_input} is not identified as bool: {expected}"


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


has_email(input_string: str, exact: bool = False) -> bool:
#
#def is_ipaddress(input_string: str) -> bool:



# geolocatie
# telnummer
# is path vs has path
