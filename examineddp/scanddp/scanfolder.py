from pathlib import Path
from pathlib import PurePath
import pandas as pd
import datetime
import magic


import logging
logger = logging.getLogger(__name__)


def scan_folder(foldername: Path) -> pd.DataFrame:
    """
    recursively examine files in folder
    """

    foldername = Path(foldername)
    try:
        assert foldername.exists(), f"{foldername.name} does not exist"
        assert foldername.is_dir(), f"{foldername.name} is not a directory"
    except AssertionError as e:
        logger.critical(e)
        return

    out = []
    paths = Path(foldername).glob('**/*')
    for p in paths:
        try:
            name = p.name
            parent = str(PurePath(p.parent).relative_to(foldername.parent))
            suffix = ' '.join(p.suffixes)
            isdir = p.is_dir()

            # Obtain file statistics
            filestats = p.stat()
            mtime = datetime.datetime\
                            .fromtimestamp(filestats.st_mtime)\
                            .isoformat()

            filesize = filestats.st_size

            # Examine files with python package: magic
            # Equivalent to the unix "file" command
            if not isdir:
                filedescription = magic.from_file(p)
                mimetype = magic.from_file(p, mime=True)
            else:
                filedescription = mimetype = None

            out.append(
                (
                    name,
                    parent,
                    suffix,
                    isdir,
                    mtime,
                    filesize,
                    filedescription,
                    mimetype
                )
            )

            logger.debug("Examined file/folder: %s", p)
        except Exception as e:
            logger.error("%s, could not examine file/folder %s", e, p)
            pass

    df = pd.DataFrame(out, columns=["name", "parent", "suffix",
                                    "is_dir", "last_modified", "file_size",
                                    "file_description", "mimetype"])
    return df
