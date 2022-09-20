import re
import pandas as pd
import ipaddress
import warnings

from examineddp.parserlib import urldetectionregex

import logging
logger = logging.getLogger(__name__)


def is_timestamp(input_string: str) -> bool:
    """
    Detects if string is a timestamp
    relies on pandas.to_datetime() to detect the time format
    """
    with warnings.catch_warnings():
        warnings.filterwarnings('error')  # temporary behaviour

        try:
            assert isinstance(input_string, str)
            assert input_string != ''
            assert input_string.isdigit() is False

            pd.to_datetime(input_string)

            logger.debug("timestamp FOUND in: '%s'", input_string)
            return True

        except (ValueError, AssertionError) as e:
            logger.debug("Timestamp NOT found in: '%s', %s", input_string, e)
            return False

        except Warning as e:
            logger.warning("WARNING was raised as exception "
                           "probably NO timestamp in: "
                           "'%s', %s", input_string, e)
            return False

        except Exception as e:
            logger.error(e)
            return False


def has_url(input_string: str, exact: bool = False) -> bool:
    """
    Detects if string contains urls, use exact is True if the string is a url
    see ./urldetectionregex for the regexes

    Note: I tried the package: urlextractor which is too slow
    regex is magnitudes faster
    """
    try:
        regex = urldetectionregex.URL_REGEX if exact is False\
                else urldetectionregex.URL_REGEX_MATCH_BEGIN_AND_ENDLINE
        assert re.search(regex, input_string) is not None
        logger.debug("urls FOUND in: '%s'", input_string)
        return True

    except AssertionError as e:
        logger.debug("%s, urls NOT found in: '%s'", e, input_string)
        return False

    except Exception as e:
        logger.error(e)
        return False


def has_email(input_string: str, exact: bool = False) -> bool:
    """
    Detects if string contains emails
    use exact is True if the string is an email
    see ./urldetectionregex for the regexes
    """
    try:
        regex = urldetectionregex.EMAIL_REGEX if exact is False\
                else urldetectionregex.EMAIL_REGEX_MATCH_BEGIN_AND_ENDLINE
        assert re.search(regex, input_string) is not None
        logger.debug("emails FOUND in: '%s'", input_string)
        return True

    except AssertionError as e:
        logger.debug("%s, emails NOT found in: '%s'", e, input_string)
        return False

    except Exception as e:
        logger.error(e)
        return False


def is_ipaddress(input_string: str) -> bool:
    """
    Detects if string is a valid IPv4 or IPv6 address returns bool
    """
    try:
        assert isinstance(input_string, str)
        ipaddress.ip_address(input_string)
        logger.debug("IP found in string: '%s'", input_string)
        return True

    except (ValueError, AssertionError) as e:
        logger.debug("%s, IP NOT found in string: '%s'", e, input_string)
        return False

    except Exception as e:
        logger.error(e)
        return False


# geolocatie
# telnummer
# is path vs has path
