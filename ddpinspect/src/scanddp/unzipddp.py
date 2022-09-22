"""
Contains functions to deal with zipfiles
"""

from pathlib import Path
import zipfile
import time
import os
import io

import logging

from scanddp.my_exceptions import FileNotFoundInZipError

logger = logging.getLogger(__name__)


def recursive_unzip(path_to_zip: Path, remove_source: bool = False) -> None:
    """
    Recursively unzips a file and extract in a new folder
    """
    p = Path(path_to_zip)

    try:
        new_location = p.parent / p.stem

        with zipfile.ZipFile(p, "r") as zf:
            logger.info("Extracting: %s", p)

            # see https://stackoverflow.com/a/23133992
            # zipfile overwrite modification times
            # keep the original
            for zi in zf.infolist():
                date_time = time.mktime(zi.date_time + (0, 0, -1))
                zf.extract(zi, new_location)
                os.utime(new_location / zi.filename, (date_time, date_time))

        if remove_source:
            logger.debug("REMOVING: %s", p)
            os.remove(p)

        paths = Path(new_location).glob("**/*.zip")
        for p in paths:
            recursive_unzip(p, True)

    except (EOFError, zipfile.BadZipFile) as e:
        logger.error("Could NOT unzip: %s, %s", p, e)
    except Exception as e:
        logger.error("Could NOT unzip: %s, %s", p, e)
        raise e


def extract_file_from_zip(zfile: str, file_to_extract: str) -> io.BytesIO:
    """
    Extracts a specific file from a zipfile buffer
    Function always returns a buffer
    """
    file_to_extract_bytes = io.BytesIO()

    try:
        with zipfile.ZipFile(zfile, "r") as zf:
            file_found = False

            for f in zf.namelist():
                logger.debug("Contained in zip: %s", f)
                if Path(f).name == file_to_extract:
                    file_to_extract_bytes = io.BytesIO(zf.read(f))
                    file_found = True
                    break

        if not file_found:
            raise FileNotFoundInZipError("File not found in zip")

    except zipfile.BadZipFile as e:
        logger.error("BadZipFile:  %s", e)
    except FileNotFoundInZipError as e:
        logger.error("File not found:  %s: %s", file_to_extract, e)
    except Exception as e:
        logger.error("Exception was caught:  %s", e)

    finally:
        return file_to_extract_bytes
