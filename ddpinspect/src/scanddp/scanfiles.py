"""
This module contains functions to scan the files contained inside a DDP
"""

from pathlib import Path
from pathlib import PurePath
from typing import Any, Union
import logging
import datetime
import json
import uuid

import magic
import pandas as pd

from parserlib import stringparse

logger = logging.getLogger(__name__)


def read_json_from_file(path_to_json: Path) -> Union[dict[Any, Any], list[Any]]:
    """
    Reads json from file if succesful it returns the result from json.load()
    """
    path_to_json = Path(path_to_json)
    out: Union[dict[Any, Any], list[Any]]

    try:
        with open(path_to_json, encoding="utf8") as f:
            out = json.load(f)
        logger.debug("succesfully opened: %s", path_to_json.name)
    except json.JSONDecodeError:
        try:
            with open(path_to_json, encoding="utf-8-sig") as f:
                out = json.load(f)
            logger.debug("succesfully opened: %s", path_to_json.name)
        except Exception as e:
            logger.error("%s, could not open: %s", e, path_to_json)
            raise e
    except Exception as e:
        logger.error("%s, could not open: %s", e, path_to_json)
        raise e

    return out


def scan_json(path_to_json: Path) -> list[tuple[Any, ...]]:
    """
    Reads the contents of a json file and assembles it into a set of datapoints

    This function denests a json and assembles each entry into a data-point (tuple)
    """

    # scan_json_inner use the variables: out, and last_modified, they are gobal to the outerscope
    def scan_json_inner(obj, name: str, parent: str) -> None:

        objtype = type(obj)
        objid = uuid.uuid4().hex
        is_ip = is_time = is_url = None

        if objtype == dict:
            obj = dict(sorted(obj.items()))
            info = ":".join(obj.keys())
            for k, v in obj.items():
                scan_json_inner(v, k, objid)

        elif objtype == list:
            info = "list object"
            for index, item in enumerate(obj):
                scan_json_inner(item, f"{name}_{index}", objid)

        elif objtype == str:
            info = obj

            is_ip = stringparse.is_ipaddress(obj)
            is_time = stringparse.is_timestamp(obj)
            is_url = stringparse.has_url(obj)

        else:
            info = obj

        out.append(
            (
                path_to_json.name,
                last_modified,
                name,
                objid,
                parent,
                str(objtype),
                info,
                is_ip,
                is_time,
                is_url,
            )
        )

    # Globals used by scan_json_inner
    out: list[tuple[Any, ...]] = []
    last_modified = datetime.datetime.fromtimestamp(
        path_to_json.stat().st_mtime
    ).isoformat()

    obj = read_json_from_file(path_to_json)
    if obj:
        scan_json_inner(obj, "toplevel", "")

    return out


def scan_json_all(foldername: Path) -> pd.DataFrame:
    """
    Reads contents of all json files in a folder recursively
    Returns a pandas dataframe
    """

    foldername = Path(foldername)
    try:
        assert foldername.exists(), f"{foldername.name} does not exist"
        assert foldername.is_dir(), f"{foldername.name} is not a directory"
    except AssertionError as e:
        logger.critical(e)
        raise e

    try:
        out = []
        paths = foldername.glob("**/*.json")
        for p in paths:
            out.extend(scan_json(p))

        df = pd.DataFrame(
            out,
            columns=[
                "filename",
                "last_modified",
                "name",
                "objid",
                "parent",
                "objtype",
                "info",
                "is_ip",
                "is_time",
                "is_url",
            ],
        )

        return df

    except Exception as e:
        logger.critical(e)
        raise e


def scan_all_files(foldername: Path) -> pd.DataFrame:
    """
    Recursively examines all files in folder
    and collects meta data about that file
    """

    foldername = Path(foldername)
    try:
        assert foldername.exists(), f"{foldername.name} does not exist"
        assert foldername.is_dir(), f"{foldername.name} is not a directory"
    except AssertionError as e:
        logger.critical(e)
        raise e

    out = []
    paths = Path(foldername).glob("**/*")
    for p in paths:
        try:
            name = p.name
            parent = str(PurePath(p.parent).relative_to(foldername.parent))
            suffix = " ".join(p.suffixes)
            isdir = p.is_dir()

            # Obtain file statistics
            filestats = p.stat()
            mtime = datetime.datetime.fromtimestamp(filestats.st_mtime).isoformat()

            filesize = filestats.st_size

            # Examine files with python package: magic
            # Equivalent to the unix "file" command
            if not isdir:
                filedescription = magic.from_file(p)
                mimetype = magic.from_file(p, mime=True)
            else:
                filedescription = None
                mimetype = None

            out.append(
                (
                    name,
                    parent,
                    suffix,
                    isdir,
                    mtime,
                    filesize,
                    filedescription,
                    mimetype,
                )
            )

            logger.debug("Examined file/folder: %s", p)
        except Exception as e:
            logger.error("%s, could not examine file/folder %s", e, p)
            raise e

    df = pd.DataFrame(
        out,
        columns=[
            "name",
            "parent",
            "suffix",
            "is_dir",
            "last_modified",
            "file_size",
            "file_description",
            "mimetype",
        ],
    )
    return df
