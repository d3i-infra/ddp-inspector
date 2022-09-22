"""
DDP Instagram module

This module contains functions to handle *.jons files contained within an instagram ddp
"""

import json
import io
import logging
from typing import Any

from scanddp.my_exceptions import ObjectIsNotADict

logger = logging.getLogger(__name__)


def instagram_bytesio_to_dict(bytes_to_read: io.BytesIO) -> dict[Any, Any]:
    """
    Converts a io.BytesIO buffer containing an instagram json file to a dict
    """

    out = {}
    try:
        out = json.load(bytes_to_read)

    except json.decoder.JSONDecodeError as e:
        logger.error("The input buffer did not contain a valid JSON: %s", e)
    except Exception as e:
        logger.error("Exception was caught: %s", e)

    finally:
        return out


def instagram_interests_to_list(dict_with_interests: dict[Any, Any]) -> list[str]:
    """
    This function extracts instagram interests from a dict
    This dict should be obtained from ads_interests.json

    This function should be rewritten as ads_interests.json changes
    """
    out = []

    try:
        if not isinstance(dict_with_interests, dict):
            raise ObjectIsNotADict("The input to this function was not dict")

        # The compleet lookup is:
        # "inferred_data_ig_interest" -> "string_map_data" -> "Interesse"
        # "Interesse is the only key, and the spelling is dutch
        # I suspect this might change with difference language settings
        # Therefore popitem()
        for item in dict_with_interests["inferred_data_ig_interest"]:
            res = item["string_map_data"].popitem()
            out.append(res[1]["value"])

    except ObjectIsNotADict as e:
        logger.error("The input list did not contain a dict: %s", e)
    except KeyError as e:
        logger.error("The a dict did not contain the interests: %s", e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return out
