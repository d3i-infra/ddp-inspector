# Usability Scripts

#### recursiveuzip.py

Unzips a folder recursively, leaving the folder structure unchanged. 
```
usage: resursiveunzip.py [-h] [-log LOGLEVEL] [-r | --remove-source | --no-remove-source] path

Unzip a folder resursively

positional arguments:
  path                  Path to zipfile to unzip

options:
  -h, --help            show this help message and exit
  -log LOGLEVEL, --loglevel LOGLEVEL
                        Provide logging level. Example --loglevel debug, default=info
  -r, --remove-source, --no-remove-source
                        Remove source .zip files (default: False)
```
