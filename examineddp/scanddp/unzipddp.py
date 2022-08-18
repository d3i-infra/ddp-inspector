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
        if zipfile.is_zipfile(p):
            with zipfile.ZipFile(p, 'r') as z:
                z.extractall(p.parent)
                logger.info("Extracting: %s", p)
                for f in z.namelist():
                    recursive_unzip(f, remove_source)
            if remove_source:
                logger.debug("REMOVING: %s", p)
                os.remove(p)

        else:
            logger.debug("NOT a zipfile returning, %s", p)
            return

    except EOFError:
        logger.error("Could NOT unzip: %s, %s", p, "EOFError")
        pass

    except Exception as e:
        logger.error("Could NOT unzip: %s, %s", p, e)
        raise e
