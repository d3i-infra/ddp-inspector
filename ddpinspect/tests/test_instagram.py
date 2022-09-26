"""
Tests test the functionality of the instagram module
"""

import pytest
from pathlib import Path
from scanddp import instagram

DATA_DIR = Path(__file__).resolve().parent / "data"


@pytest.mark.parametrize(
    "fun_to_test,file,result",
    [
        (
            "instagram_interests_to_list",
            "ads_interests.json_2022_09_22",
            ["Interest 1", "Interest 2"],
        ),
        (
            "instagram_your_topics_to_list",
            "your_topics.json_2022_09_22",
            ["Topic 1", "Topic 2"],
        ),
    ],
)
def test_instagram_function(fun_to_test: str, file: str, result: list) -> None:
    """
    Check if ads_interests.json file from instagram ddp is read correctly
    and if interests are identified
    """

    f_to_check = DATA_DIR / file
    with open(f_to_check, "rb") as f:
        to_check_dict = instagram.instagram_bytesio_to_dict(f)

    assert (
        len(to_check_dict) != 0
    ), f"{file} did not produce output, list should not be empty"

    fun = getattr(instagram, fun_to_test)
    output = fun(to_check_dict)
    assert result == output, f"FAILED {fun_to_test}: {result} not found in {file}"
