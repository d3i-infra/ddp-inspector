from pathlib import Path
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
        if zipfile.is_zipfile(p):
            with zipfile.ZipFile(p, 'r') as z:
                z.extractall(p.parent)
                logging.info("Extracting: %s", p)
                for f in z.namelist():
                    recursive_unzip(f, remove_source)
            if remove_source:
                logging.debug("REMOVING: %s", p)
                os.remove(p)

        else:
            logging.debug("NOT a zipfile returning, %s", p)
            return

    except EOFError:
        logging.error("Could NOT unzip: %s, %s", p, "EOFError")
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



