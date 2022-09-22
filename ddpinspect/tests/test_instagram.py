"""
Tests test the functionality of the instagram module
"""

import pytest
from pathlib import Path
from scanddp import instagram

DATA_DIR = Path(__file__).resolve().parent / "data"


@pytest.mark.parametrize("file", ["ads_interests.json_2022_09_22"])
def test_read_instagram_interests(file: str) -> None:
    """
    Check if ads_interests.json file from instagram ddp is read correctly
    and if interests are identified
    """

    f_to_check = DATA_DIR / file
    with open(f_to_check, "rb") as f:
        interests_listdict = instagram.instagram_bytesio_to_dict(f)

    assert (
        len(interests_listdict) != 0
    ), f"{file} did not produce output, list should not be empty"

    interests = instagram.instagram_interests_to_list(interests_listdict)
    assert (
        "Interest 1" and "Interest 2" in interests
    ), f"Interests were not found in {file}"
