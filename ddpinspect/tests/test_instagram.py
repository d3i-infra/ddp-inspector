"""
Tests test the functionality of the instagram module
"""

import pytest
from pathlib import Path

from ddpinspect import instagram
from ddpinspect import unzipddp

DATA_DIR = Path(__file__).resolve().parent / "data" / "instagram"


@pytest.mark.parametrize(
    "fun_to_test,file,result",
    [
        (
            "interests_to_list",
            "ads_interests.json_2022_09_22",
            ["Interest 1", "Interest 2"],
        ),
        (
            "your_topics_to_list",
            "your_topics.json_2022_09_22",
            ["Topic 1", "Topic 2"],
        ),
    ],
)
def test_instagram_function(fun_to_test: str, file: str, result: list) -> None:
    """
    Test if correct items are extracted from the instagram ddp
    """

    f_to_check = DATA_DIR / file
    with open(f_to_check, "rb") as b:
        to_check_dict = unzipddp.read_json_from_bytes(b)

    assert (
        len(to_check_dict) != 0
    ), f"{file} did not produce output, list should not be empty"

    fun = getattr(instagram, fun_to_test)
    output = fun(to_check_dict)
    assert result == output, f"FAILED {fun_to_test}: {result} not found in {file}"


@pytest.mark.parametrize(
    "zipfile,expected",
    [
        ("instagram_2022_09_26.zip", "Valid Instagram zipfile"),
        ("instagram_html_2022_09_26.zip", "Instagram zipfile did not contain json"),
        ("ads_interests.json_2022_09_22", "Bad zipfile"),
        ("empty.zip", "Not an Instagram zipfile"),
    ],
)
def test_validate_instagram_zip(zipfile: str, expected: str) -> None:
    """
    Check if twitter.js file is read correctly
    and if interests are identified
    """

    result = instagram.validate_zip(DATA_DIR / zipfile)
    assert result.get_status_description() == expected
