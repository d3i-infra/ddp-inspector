######################################################################################################
# My own testing grounds
# pieces of code that I run to test stuff

import logging
logging.basicConfig(level=logging.INFO)

from examineddp.scanddp import scanfolder
from examineddp.scanddp import scanjson
from examineddp.scanddp import unzipddp

# unzip folder leaving the folder structure in tact
unzipddp.recursive_unzip("./Example_DDPs.zip")

df_folder_structure = scanfolder.scan_folder("./Example_DDPs/Example_DDPs/Instagram_data_zenodo")
df_json_structure = scanjson.scan_json_all("./Example_DDPs/Example_DDPs/Instagram_data_zenodo")

df_folder_structure




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

from pathlib import Path
paths = Path("./Example_DDPs/Example_DDPs/Sample_SocialMedia/sample-platform-gonzalezkatherine-0/").glob("**/*.zip")

for p in paths:
    print(p)

r.encoding='utf-8-sig'
data = json.loads(r.text)




import json


with open(check) as f:
    dat = json.load(f)


dat
test = {}

if test:
    print("Asd")


import logging
logging.basicConfig(level=logging.DEBUG)
from examineddp.scanddp import scanjson

example = "Example_DDPs/Example_DDPs/Instagram_data_zenodo/horsesarecool52_20201020/settings.json"
check = "Example_DDPs/Example_DDPs/Instagram_data_zenodo/katsaremeow_20201020/uploaded_contacts.json"
asd = scanjson.read_json_from_file(check)
asd = scanjson.read_json_from_file(example)
asd
type(asd)

with open(check, encoding="utf-8-sig") as f:
    dat = json.load(f)



if not None:
    print("ASD")


from pathlib import Path
import zipfile
import time
path = Path("asdasd/asdasd")

with zipfile.ZipFile("./Example_DDPs.zip", 'r') as zf:
    # see https://stackoverflow.com/a/23133992
    for zi in zf.infolist():
        date_time = time.mktime(zi.date_time + (0, 0, -1))
        print(zi)
        print(zi.filename)
        print(date_time)
        newp = path/Path(zi.filename).name
        print(newp)


        zf.extract(zi)
        date_time = time.mktime(zi.date_time + (0, 0, -1))
        os.utime(zi.filename, (date_time, date_time))







with zipfile.ZipFile("./Example_DDPs.zip", 'r') as zf:
    # see https://stackoverflow.com/a/23133992
    for zi in zf.infolist():
        date_time = time.mktime(zi.date_time + (0, 0, -1))
        print(zi)
        print(zi.filename)
        print(date_time)
        newp = path/Path(zi.filename).name
        print(newp)

###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
# Explore zip

import logging
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logging.basicConfig(level=logging.INFO)


from examineddp.scanddp import unzipddp
from examineddp.scanddp import twitter

twitter_zip = "./Example_DDPs/twitter/twitter-2022-09-08-7b4bc3e1887ddc4becc57fb106a7a4e86751b45fa7b18258909a2a52bd73af08.zip"

# Happy flow
my_bytes = unzipddp.extract_file_from_zip(twitter_zip, "personalization.js")  
my_dict = twitter.twitter_bytesio_to_listdict(my_bytes)
check = twitter.twitter_interests_from_listdict(my_dict)
check

# Bad flow ,file not found
my_bytes = unzipddp.extract_file_from_zip(twitter_zip, "personali.js")  
my_dict = twitter.twitter_bytesio_to_listdict(my_bytes)
check = twitter.twitter_interests_from_listdict(my_dict)
check


# Bad flow, file the file is a different file and an empty json
my_bytes = unzipddp.extract_file_from_zip(twitter_zip, "contact.js")  
my_dict = twitter.twitter_bytesio_to_listdict(my_bytes)
check = twitter.twitter_interests_from_listdict(my_dict)
check

# Bad flow, file the file is a different file 
my_bytes = unzipddp.extract_file_from_zip(twitter_zip, "ad-impressions.js")  
my_dict = twitter.twitter_bytesio_to_listdict(my_bytes)
check = twitter.twitter_interests_from_listdict(my_dict)
check
