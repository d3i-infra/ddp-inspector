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
    "zipfile,expected_statuscode,expected_category_id",
    [
        ("instagram_2022_09_26.zip", 0, "json_en"),
        ("instagram_html_2022_09_26.zip", 0, None),
        ("ads_interests.json_2022_09_22", 1, None),
        ("empty.zip", 0, None),
    ],
)
def test_validate_instagram_zip(zipfile: str, expected_statuscode: int, expected_category_id: str) -> None:
    """
    Check if twitter.js file is read correctly
    and if interests are identified
    """

    validation = instagram.validate_zip(DATA_DIR / zipfile)
    assert validation.status_code.id == expected_statuscode
    if expected_category_id:
        assert validation.ddp_category.id == expected_category_id
    else:
        assert validation.ddp_category is None
