"""
DDP Youtube module

This module contains functions to handle files contained within an youtube ddp
"""

from pathlib import Path
from typing import Any
import logging
import zipfile
import io
import re

import pandas as pd
from bs4 import BeautifulSoup

from ddpinspect.validate import (
    DDPCategory,
    StatusCode,
    ValidateInput,
    Language,
    DDPFiletype,
)
from ddpinspect import scanfiles

logger = logging.getLogger(__name__)

DDP_CATEGORIES = [
    DDPCategory(
        id="json_en",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.EN,
        known_files=[
            "archive_browser.html",
            "watch-history.json",
            "my-comments.html",
            "my-live-chat-messages.html",
            "subscriptions.csv",
        ],
    ),
    DDPCategory(
        id="html_en",
        ddp_filetype=DDPFiletype.HTML,
        language=Language.EN,
        known_files=[
            "archive_browser.html",
            "watch-history.html",
            "my-comments.html",
            "my-live-chat-messages.html",
            "subscriptions.csv",
        ],
    ),
    DDPCategory(
        id="json_nl",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.NL,
        known_files=[
            "archive_browser.html",
            "kijkgeschiedenis.json",
            "mijn-reacties.html",
            "abonnementen.csv",
        ],
    ),
    DDPCategory(
        id="html_nl",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.NL,
        known_files=[
            "archive_browser.html",
            "kijkgeschiedenis.html",
            "mijn-reacties.html",
            "abonnementen.csv",
        ],
    ),
]

STATUS_CODES = [
    StatusCode(id=0, description="Valid zip", message="Valid zip"),
    StatusCode(id=1, description="Bad zipfile", message="Bad zipfile"),
]


def validate_zip(zfile: Path) -> ValidateInput:
    """
    Validates the input of a Youtube zipfile
    """

    validate = ValidateInput(STATUS_CODES, DDP_CATEGORIES)

    try:
        paths = []
        with zipfile.ZipFile(zfile, "r") as zf:
            for f in zf.namelist():
                p = Path(f)
                if p.suffix in (".html", ".json", ".csv"):
                    logger.debug("Found: %s in zip", p.name)
                    paths.append(p.name)

        validate.set_status_code(0)
        validate.infer_ddp_category(paths)
    except zipfile.BadZipFile:
        validate.set_status_code(1)

    return validate


def to_df(youtube_list: list[dict[Any, Any]] | Any) -> pd.DataFrame:
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
        df_out = scanfiles.remove_const_cols_from_df(df_out)

    except TypeError as e:
        logger.error(e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return df_out


def comments_to_df(comments: io.BytesIO) -> pd.DataFrame:
    """
    Parse comments from Youtube DDP

    returns a pd.DataFrame
    with the comment, type of comment, and a video url
    """

    data_set = []
    df = pd.DataFrame()

    video_regex = r"(?P<video_url>^http[s]?://www\.youtube\.com/watch\?v=[a-z,A-Z,0-9,\-,_]+)(?P<rest>$|&.*)"
    video_pattern = re.compile(video_regex)

    # Big try except block due to lack of time
    try:
        soup = BeautifulSoup(comments, "html.parser")
        items = soup.find_all("li")
        for item in items:
            data_point = {}

            # Extract comments
            content = item.get_text(separator="<SEP>").split("<SEP>")
            message = content.pop()
            action = "".join(content)
            data_point["Comment"] = message
            data_point["Type of comment"] = action

            # Search through all references
            # if a video can be found:
            # 1. extract video url
            # 2. add data point
            for ref in item.find_all("a"):
                regex_result = video_pattern.match(ref.get("href"))
                if regex_result:
                    data_point["Video url"] = regex_result.group("video_url")
                    data_set.append(data_point)
                    break

        df = pd.DataFrame(data_set)

    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return df
