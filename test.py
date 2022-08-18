######################################################################################################
# My own testing grounds
# pieces of code that I run to test stuff

# Create a sample dataset from a DDP

import logging
logging.basicConfig(level=logging.INFO)

from examineddp.scanddp import scanfolder
from examineddp.scanddp import scanjson
from examineddp.scanddp import unzipddp

unzipddp.recursive_unzip("./Example_DDPs.zip")

df_folderstructure = scanfolder.scan_folder("./Example_DDPs/Instagram_data_zenodo")
df_folderstructure = scanfolder.scan_("./Example_DDPs/Instagram_data_zenodo")







from pathlib import Path
import magic
import uuid
import json
import pandas as pd

from examineddp.parserlib import stringparse

import importlib

import logging
logging.basicConfig(level=logging.ERROR)


import json

example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/settings.json"
example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/events.json"
example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/account_history.json"
example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/settings.json"
example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/events.json"
example = Path("Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/account_history.json")
example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/media.json"
example = "Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/searches.json"

from examineddp.scanddp import scanjson
importlib.reload(scanjson)
out = scanjson.get_structure_json(example)
out = scanjson.get_structure_json("example")
out



check = pd.DataFrame(out, columns = ["name", "objid", "parent", "str(objtype)", "info", "is_ip", "is_time", "is_url"])
check.to_excel("check.xlsx")
check


check = scanjson.scan_json_in_folder("./Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020")
check.to_excel("check.xlsx")

Path(Path("./Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020")) == Path("./Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020")
paths = Path("./Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020").glob('**/*.json')
for p in paths:
    print(p.name)

pd.DataFrame

importlib.reload(scanjson)


test = []
test.extend([1,2,3])
test.extend([])

########################################################
########################################################
########################################################
########################################################
# Profile code
import cProfile
import pstats

profile = cProfile.Profile()
profile.runcall(get_structure_json, example)
ps = pstats.Stats(profile)
ps.print_stats()

########################################################
test =  [ "name", "parent", "type", "info"]


for k, i in enumerate(test):
    print(f"{k} {i}")


my_stamp = "2020-10-08T12:02:40+00:00"
non_working_stamp = "asdkjaskjsad"
non_working_stamp = None

test = " asd.asd.com"
stringparse.has_url(test, is_url=True)
stringparse.has_url(test)


stringparse.is_ipaddress("2a02:a210:2502:b280:d9cf:6454d:5bc2:35a")

pd.to_datetime("")

######################################
# test scanning folders

import logging
logging.basicConfig(level=logging.DEBUG)
from examineddp.scanddp import scanfolder
importlib.reload(scanfolder)

example = "./Example_DDPs/Google_Search_History/"
out = scanfolder.scan_folder(example)
out.to_excel("test.xlsx")


######################################
import logging
import importlib
logging.basicConfig(level=logging.INFO)

from examineddp.scanddp import scanjson
importlib.reload(scanjson)

example = "./Example_DDPs/Google_Search_History/"
out = scanjson.scan_json_in_folder(example)

out.to_excel("test.xlsx")


out = scanfolder.scan_folder("asdasd")
out = scanfolder.scan_folder(example)
list(out["mtime"])

out 

out = scanjson.get_structure_json("example")
out


Path("asdasdasd").exists()
Path("asdasdasd").is_dir()

from pathlib import PurePath
pp = PurePath(example)

str(pp.relative_to("Example_DDPs/"))


######################################
import importlib
from examineddp.parserlib import stringparse
importlib.reload(stringparse)


stringparse.has_email(" ncdeschipper@gmail.com kjasdkjaskdsakj", exact = True)
stringparse.has_email(" ncdeschipper@gmail.com kjasdkjaskdsakj")
stringparse.has_email("ncgmail.com", exact = True)


############################################
import warnings
warnings.filterwarnings("error")

import pandas as pd
wut = pd.to_datetime("0A5XJBV023")
wut 


pd.to_datetime("8P6HPMGL90")
check


try:
    check = pd.to_datetime("8P6HPMGL90")
except Warning as e:
    print(f"yolo, {e}")

import importlib
from examineddp.parserlib import stringparse
importlib.reload(stringparse)

stringparse.is_timestamp("8P6HPMGL90")





