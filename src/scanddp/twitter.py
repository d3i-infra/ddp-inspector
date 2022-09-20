"""
DDP Twitter module

This module contains functions to handle *.js files contained within a twitter ddp
"""

import json
import io
import re
import logging

logger = logging.getLogger(__name__)


class ObjectIsNotADict(Exception):
    pass


def twitter_bytesio_to_listdict(bytes_to_read: io.BytesIO) -> list[dict]:
    """
    Converts a io.BytesIO buffer containing a twitter.js file, to a list of dicts
    """

    out = []
    lines = []

    try:
        with io.TextIOWrapper(bytes_to_read, encoding ="utf8") as f:
            lines = f.readlines()

        # remove first and element from list
        lines[0] = re.sub('^.*? = ', '', lines[0])

        # convert to a list of dicts
        out = json.loads("".join(lines))

    except json.decoder.JSONDecodeError as e :
        logger.error("The input buffer did not contain a valid JSON:  %s", e)
    except IndexError as e:
        logger.error("No lines were read, could be empty input buffer:  %s", e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return out


def twitter_interests_from_listdict(interest_list: list[dict]) -> list:
    """ 
    This function extracts twitter interests from a list[dict]
    This list[dict] should be obtained from personalization.js

    This function should be rewritten as personalization.js changed
    """
    out = []

    try:
        dict_with_interests = interest_list[0]

        if not isinstance(dict_with_interests, dict):
            raise ObjectIsNotADict("The first item in interest_list is not a dict")

        # traverse into the nested dict
        for key in ["p13nData", "interests", "interests"]:
            dict_with_interests = dict_with_interests[key]

        out = [d.get("name") for d in dict_with_interests]

    except IndexError as e:
        logger.error("The input object is an empty list:  %s", e)
    except ObjectIsNotADict as e:
        logger.error("The input list did not contain a dict:  %s", e)
    except KeyError as e:
        logger.error("The a dict did not contain the interests:  %s", e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return out


