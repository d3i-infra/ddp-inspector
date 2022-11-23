"""
Tests test the functionality of the unzipdd module
"""

from typing import Any
import pytest
import io

from ddpinspect import unzipddp


@pytest.mark.parametrize(
    "bytes,expected",
    [
        (
            io.BytesIO(b'{"a": "b"}'),
            {"a": "b"}
        ),
        (
            io.BytesIO(b'[{"a": "b"}]'),
            [{"a": "b"}]
        ),
        (
            io.BytesIO(b'1'),
            {}
        ),
        (
            io.BytesIO(b'\xef\xbb\xbf{"a":"b"}'),  # json files with utf-8-BOM
            {"a": "b"}
        ),
    ],
)
def test_read_json_from_bytes(bytes: io.BytesIO, expected: Any) -> None:
    assert unzipddp.read_json_from_bytes(bytes) == expected
