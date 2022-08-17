import json
import uuid
import datetime

import pandas as pd
from pathlib import Path

from examineddp.parserlib import stringparse

import logging
logger = logging.getLogger(__name__)


def get_structure_json(path_to_json: Path) -> list[tuple]:
    """
    Reads the contents of a json file and assembles it into a set of datapoints
    """

    path_to_json = Path(path_to_json)
    out = []
    try:
        with open(path_to_json) as f:
            obj = json.load(f)
        logger.debug("succesfully opened: %s", path_to_json.name)
    except Exception as e:
        logger.error("%s, could not open: %s", e, path_to_json.name)
        return out

    # out is global in the scope of this function 
    # used by get_structure_json_inner, which is a recursive function
    last_modified = datetime.datetime.fromtimestamp(path_to_json.stat().st_mtime).isoformat()
    def get_structure_json_inner(obj: dict, name: str, parent: str) -> None:

        objtype = type(obj)
        objid = uuid.uuid4().hex
        is_ip = is_time = is_url = None

        if objtype == dict:
            obj = dict(sorted(obj.items()))
            info = ':'.join(obj.keys())
            for k, v in obj.items():
                get_structure_json_inner(v, k, objid)

        elif objtype == list:
            info = "list object"
            for index, item in enumerate(obj):
                get_structure_json_inner(item, f"{name}_{index}", objid)

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
                    is_url
                    )
                )

    get_structure_json_inner(obj, 'toplevel', '')

    return out


def scan_json_in_folder(foldername: Path) -> pd.DataFrame:
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
        return

    try:
        out = []
        paths = foldername.glob('**/*.json')
        for p in paths:
            out.extend(get_structure_json(p))

        df = pd.DataFrame(out, columns = ["filename", "last_modified", "name", "objid", "parent", "objtype", "info", "is_ip", "is_time", "is_url"])
        
        return df

    except Exception as e:
        logger.critical(e)
        raise(e)



