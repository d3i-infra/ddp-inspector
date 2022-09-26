"""
DDP Instagram module

This module contains functions to handle *.jons files contained within an instagram ddp
"""

from typing import Any
from pathlib import Path
from dataclasses import dataclass, field
import json
import io
import logging
import zipfile

from scanddp.my_exceptions import ObjectIsNotADict

logger = logging.getLogger(__name__)


@dataclass
class ValidateInstagramInput:
    """
    Class containing data regarding input checking an Instagram zipfile for correctness
    """
    status_code: int = 0
    status_message: dict[int, dict[str, str]] = field(
        default_factory=lambda: {
            0: {
                "description": "Valid Instagram zipfile",
                "message": "Valid Instagram zipfile",
            },
            1: {
                "description": "Bad zipfile",
                "message": "We could not detect a zipfile could you recheck your selected file?",
            },
            2: {
                "description": "Not an Instagram zipfile",
                "message": "We could not detect a zipfile from Instagram could you recheck your selected file?",
            },
            3: {
                "description": "Instagram zipfile did not contain json",
                "message": "We detected an Instagram zipfile but not in the correct format, could you download the json format instead of the html format?",
            },
        }
    )
    known_files: list[str] = field(
        default_factory=lambda: [
            "secret_conversations",
            "personal_information",
            "account_privacy_changes",
            "account_based_in",
            "recently_deleted_content",
            "liked_posts",
            "stories",
            "profile_photos",
            "followers",
            "signup_information",
            "comments_allowed_from",
            "login_activity",
            "your_topics",
            "camera_information",
            "recent_follow_requests",
            "devices",
            "professional_information",
            "follow_requests_you've_received",
            "eligibility",
            "pending_follow_requests",
            "videos_watched",
            "ads_interests",
            "account_searches",
            "following",
            "posts_viewed",
            "recently_unfollowed_accounts",
            "post_comments",
            "account_information",
            "accounts_you're_not_interested_in",
            "use_cross-app_messaging",
            "profile_changes",
            "reels",
        ]
    )

    def get_status_message(self) -> str:
        """ returns code message, can be shown to user """
        return self.status_message.get(self.status_code, {}).get("message", "Not defined")

    def get_status_description(self) -> str:
        """ returns description, can be shown to debug """
        return self.status_message.get(self.status_code, {}).get("description", "Not defined")


def validate_instagram_zip(instagram_zip: Path) -> ValidateInstagramInput:
    """
    Validates the input of an instagram zipfile

    Checks whether the file is a zipfile
    Checks whether its a zipfile containing html or json
    Check whether at least 30% of known "*.json" files are present in the zip

    3 mutually exclusive cases are possible
    - Not a zip
    - Not a recognized instagram zipfile
    - Not a json instagram zipfile
    - An instagram zipfile
    """
    validate = ValidateInstagramInput()

    paths = []
    try:
        with zipfile.ZipFile(instagram_zip, "r") as zf:
            for f in zf.namelist():
                p = Path(f)
                if p.suffix in (".html", ".json"):
                    paths.append(p)

    except zipfile.BadZipFile:
        validate.status_code = 1
        return validate

    # determine the percentage of known files in zipfile
    # 30% of the known files should be found
    stems = [p.stem for p in paths]
    n_files_found = [1 if f in stems else 0 for f in validate.known_files]
    p_files_found = sum(n_files_found) / len(validate.known_files) * 100
    if p_files_found <= 30:
        validate.status_code = 2
        return validate

    # Check whether there are more json than html files in zip
    suffixes = [p.suffix for p in paths]
    if suffixes.count(".json") < suffixes.count(".html"):
        validate.status_code = 3
        return validate

    return validate


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
        logger.error("The a dict did not contain key: %s", e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return out


def instagram_your_topics_to_list(dict_with_topics: dict[Any, Any]) -> list[str]:
    """
    This function extracts instagram your_topics from a dict
    This dict should be obtained from your_topics.json

    This function should be rewritten as your_topics.json changes
    """
    out = []

    try:
        if not isinstance(dict_with_topics, dict):
            raise ObjectIsNotADict("The input to this function was not dict")

        # The compleet lookup is:
        # "topics_your_topics" -> "string_map_data" -> "Name" -> "value"
        for item in dict_with_topics["topics_your_topics"]:
            res = item["string_map_data"].popitem()
            out.append(res[1]["value"])

    except ObjectIsNotADict as e:
        logger.error("The input list did not contain a dict: %s", e)
    except KeyError as e:
        logger.error("The a dict did not contain the key: %s", e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return out
