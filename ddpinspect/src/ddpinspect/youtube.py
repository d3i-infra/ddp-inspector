"""
DDP Youtube module

This module contains functions to handle files contained within an youtube ddp
"""

import logging
import zipfile
from typing import Any
from pathlib import Path
from dataclasses import dataclass, field

import pandas as pd

from ddpinspect import scanfiles

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
                "description": "Valid Youtube zipfile",
                "message": "Valid Youtube zipfile",
            },
            1: {
                "description": "Bad zipfile",
                "message": "We could not detect a zipfile could you recheck your selected file?",
            },
            2: {
                "description": "Not a Youtube zipfile",
                "message": "We could not detect a zipfile from Youtube could you recheck your selected file?",
            }
        }
    )
    known_files: list[str] = field(
        default_factory=lambda: [
            "archive_browser",
            "watch-history",
            "my-comments",
            "my-live-chat-messages",
            "subscriptions"
            ]
    )

    def get_status_message(self) -> str:
        """ returns code message, can be shown to user """
        return self.status_message.get(self.status_code, {}).get("message", "Not defined")

    def get_status_description(self) -> str:
        """ returns description, can be shown to debug """
        return self.status_message.get(self.status_code, {}).get("description", "Not defined")


def validate_zip(zfile: Path) -> ValidateInstagramInput:
    """
    Validates the input of a Youtube zipfile
    """

    validate = ValidateInstagramInput()

    paths = []
    try:
        with zipfile.ZipFile(zfile, "r") as zf:
            for f in zf.namelist():
                p = Path(f)
                if p.suffix in (".html", ".json", ".csv"):
                    logger.debug("Found: %s in zip", p)
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

    return validate


def to_df(youtube_list: list[dict[Any, Any]]) -> pd.DataFrame:
    """
    Converts list[dict[Any, Any]] obtained from youtube to pd.DataFrame

    I don't know yet whether this function is general enough to be moved to a different module
    For now I like it here
    """

    df_out = pd.DataFrame()

    try:
        if not isinstance(youtube_list, (dict, list)):
            raise TypeError("Incorrect input type expected dict or list")

        df_out = pd.DataFrame([scanfiles.dict_denester(item) for item in youtube_list])

    except TypeError as e:
        logger.error(e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return df_out
