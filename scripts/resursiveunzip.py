from pathlib import Path
import time
import zipfile
import argparse
import os

import logging
LOGGING_FORMAT='%(asctime)s - %(levelname)s - %(message)s'

def recursive_unzip(path_to_zip: Path, remove_source: bool = False) -> None:
    """
    Recursively unzips a file and extract in a new folder
    """
    p = Path(path_to_zip)

    try:
        new_location = p.parent/p.stem

        with zipfile.ZipFile(p, 'r') as zf:
            logging.info("Extracting: %s", p)

            # see https://stackoverflow.com/a/23133992
            # zipfile overwrite modification times
            # keep the original
            for zi in zf.infolist():
                date_time = time.mktime(zi.date_time + (0, 0, -1))
                zf.extract(zi, new_location)
                os.utime(new_location/zi.filename, (date_time, date_time))

        if remove_source:
            logging.debug("REMOVING: %s", p)
            os.remove(p)

        paths = Path(new_location).glob("**/*.zip")
        for p in paths:
            recursive_unzip(p, True)

    except (EOFError, zipfile.BadZipFile) as e:
        logging.error("Could NOT unzip: %s, %s", p, e)
        pass

    except Exception as e:
        logging.error("Could NOT unzip: %s, %s", p, e)
        raise e
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Unzip a folder resursively')
    parser.add_argument('path', 
            help='Path to zipfile to unzip')
    parser.add_argument( '-log',
                     '--loglevel',
                     default='info',
                     help='Provide logging level. Example --loglevel debug, default=info' )
    parser.add_argument('-r', 
                        '--remove-source',
                        action=argparse.BooleanOptionalAction,
                        default=False,
                        help="Remove source .zip files")

    args = parser.parse_args()
    logging.basicConfig(format=LOGGING_FORMAT, level=args.loglevel.upper())

    recursive_unzip(args.path, args.remove_source)



