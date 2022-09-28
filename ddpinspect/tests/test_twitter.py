"""
Tests test the functionality of the twitter module
"""

import pytest
from pathlib import Path
from scanddp import twitter

DATA_DIR = Path(__file__).resolve().parent / "data"


@pytest.mark.parametrize("file", ["personalization.js_2022_09_20"])
def test_read_twitter_interests(file: str) -> None:
    """
    Test if twitter.js file is read correctly
    and if interests are identified
    """

    f_to_check = DATA_DIR / file
    with open(f_to_check, "rb") as f:
        interests_listdict = twitter.bytesio_to_listdict(f)

    assert (
        len(interests_listdict) != 0
    ), f"{file} did not produce output, list should not be empty"

    interests = twitter.interests_to_list(interests_listdict)
    assert (
        "Interest 1" and "Interest 2" in interests
    ), f"Interests were not found in {file}"


@pytest.mark.parametrize(
    "zipfile,expected",
    [
        ("twitter_2022_09_08.zip", "Valid Twitter zipfile"),
        ("ads_interests.json_2022_09_22", "Bad zipfile"),
        ("empty.zip", "Not a Twitter zipfile"),
    ],
)
def test_validate_twitter_zip(zipfile: str, expected: str) -> None:
    """
    Test the input validation for a twitter.zip
    """

    result = twitter.validate_zip(DATA_DIR / zipfile)
    assert result.get_status_description() == expected
