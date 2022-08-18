"""
Recursively unzip a DDP, DDPs could contain nested zips
"""
from pathlib import Path
import zipfile
import argparse
import os

import logging
logger = logging.getLogger(__name__)


def recursive_unzip(path_to_zip: Path, remove_source: bool = False) -> None:
    """
    Recursively unzips a file and extract in a new folder
    """
    p = Path(path_to_zip)

    try:
        new_location = p.parent/p.stem

        with zipfile.ZipFile(p, 'r') as z:
            logger.info("Extracting: %s", p)
            z.extractall(new_location)

        if remove_source:
            logger.debug("REMOVING: %s", p)
            os.remove(p)

        paths = Path(new_location).glob("**/*.zip")
        for p in paths:
            recursive_unzip(p, True)

    except (EOFError, zipfile.BadZipFile) as e:
        logger.error("Could NOT unzip: %s, %s", p, e)
        pass

    except Exception as e:
        logger.error("Could NOT unzip: %s, %s", p, e)
        raise e
        
