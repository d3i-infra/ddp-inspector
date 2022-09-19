# DDP Volatility Project

# TODO implement:

1. Create installable package
2. Create unit test
3. Automate testing with github actions

This folder contains scripts to extract the structure out of any data download package.
Thusfar, this repo contains functions: 

* To examine all files in a folder. Recursively, walk through a folder and record: `ls`-like statistics and file type using `python-magic` equivalent to the Linux `file` command. Returns results in a `pandas.DataFrame`
* To scan all json files in a folder. Flattens the structure of json files and record information about the key value pairs. Returns results in a `pandas.DataFrame`.


## Installation

Install the dependencies in requirements.txt in a virtual environment:

```
python3 -m venv ./env
source env/bin/activate
pip3 install -r requirements.txt
```


## Usage

``` python
import logging
logging.basicConfig(level=logging.INFO)

from examineddp.scanddp import scanfolder
from examineddp.scanddp import scanjson
from examineddp.scanddp import unzipddp

# unzip folder leaving the folder structure in tact
unzipddp.recursive_unzip("./Example_DDPs.zip")

df_folder_structure = scanfolder.scan_folder("./Example_DDPs/Example_DDPs/Instagram_data_zenodo")
df_json_structure = scanjson.scan_json_all("./Example_DDPs/Example_DDPs/Instagram_data_zenodo")
```

