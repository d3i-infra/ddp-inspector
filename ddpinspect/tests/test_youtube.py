"""
Tests test the functionality of the instagram module
"""

import pytest
from pathlib import Path

from ddpinspect import unzipddp
from ddpinspect import youtube

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data" / "youtube"


@pytest.mark.parametrize(
    "fun_to_test,extraction_fun,file,df_expected",
    [
        (
            "to_df",
            "read_json_from_bytes",
            "watch-history.json_2022_09_22",
            pd.DataFrame(
                [
                    (
                        "YouTube",
                        "Video 1",
                        "https://www.youtube.com/",
                        "Channel 1",
                        "https://www.youtube.com/channel/channel1",
                        "2022-09-21T11:52:59.995Z",
                        "YouTube",
                        "YouTube watch history",
                    ),
                    (
                        "YouTube",
                        "Video 2",
                        "https://www.youtube.com/",
                        "Channel 2",
                        "https://www.youtube.com/channel/channel2",
                        "2022-09-20T21:38:27.221Z",
                        "YouTube",
                        "YouTube watch history",
                    ),
                ],
                columns=[
                    "header",
                    "title",
                    "titleUrl",
                    "subtitles_0_name",
                    "subtitles_0_url",
                    "time",
                    "products_0",
                    "activityControls_0",
                ],
            ),
        ),
        (
            "to_df",
            "read_csv_from_bytes",
            "subscriptions.csv_2022_09_22",
            pd.DataFrame(
                [
                    (
                        "UAConmtkj459834=XASD10jf",
                        "http://www.youtube.com/channel/UAConmtkj459834=XASD10jf",
                        "Fake Channel Name 1",
                    ),
                    (
                        "UACo1mtkj459834=XASD10jf",
                        "http://www.youtube.com/channel/UACo1mtkj459834=XASD10jf",
                        "Fake Channel Name 2",
                    ),
                ],
                columns=["Channel Id", "Channel Url", "Channel Title"],
            ),
        ),
    ],
)
def test_youtube(
    fun_to_test: str, extraction_fun: str, file: str, df_expected: pd.DataFrame
) -> None:
    """
    Test if correct items are extracted from the Youtube ddp
    """

    file_to_check = DATA_DIR / file
    fun_to_test = getattr(youtube, fun_to_test)
    extraction_fun = getattr(unzipddp, extraction_fun)

    with open(file_to_check, "rb") as b:
        to_check_dict = extraction_fun(b)

    assert (
        len(to_check_dict) != 0
    ), f"{file} did not produce output, list should not be empty"

    df_result = fun_to_test(to_check_dict)
    assert pd.testing.assert_frame_equal(df_result, df_expected) is None


@pytest.mark.parametrize(
    "zipfile,expected",
    [
        ("takeout-20220921T133717Z-001_2022_09_22.zip", "Valid Youtube zipfile"),
        ("subscriptions.csv_2022_09_22", "Bad zipfile"),
        ("empty.zip", "Not a Youtube zipfile"),
    ],
 )
def test_validate_youtube_zip(zipfile: str, expected: str) -> None:
    """
    Check if twitter.js file is read correctly
    and if interests are identified
    """

    result = youtube.validate_zip(DATA_DIR / zipfile)
    assert result.get_status_description() == expected
