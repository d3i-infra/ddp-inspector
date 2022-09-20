"""
Tests test the functionality of the twitter module
"""

import pytest
from pathlib import Path
from scanddp import twitter

DATA_DIR = Path(__file__).resolve().parent / "data"


@pytest.mark.parametrize("file", [
    "personalization.js_2022_09-20"
])
def test_read_twitter_interests(file: str) -> None:
    """
    Check if twitter.js file is read correctly
    and if interests are identified
    """

    f_to_check = DATA_DIR / file
    with open(f_to_check, 'rb') as f:
        interests_listdict = twitter.twitter_bytesio_to_listdict(f)

    assert len(interests_listdict) != 0,\
        f"{file} did not produce output, list should not be empty"

    interests = twitter.twitter_interests_from_listdict(interests_listdict)
    assert "Interest 1" and "Interest 2" in interests,\
        f"Interests were not found in {file}"
