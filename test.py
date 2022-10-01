######################################################################################################
# My own testing grounds
# pieces of code that I run to test stuff
 import     
import logging
logging.basicConfig(level=logging.INFO)

from ddpinspect import scanfolder
from ddpinspect import scanjson
from ddpinspect import unzipddp

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

from examineddp.ddpinspect import scanjson
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
from examineddp.ddpinspect import scanfolder
importlib.reload(scanfolder)

example = "./Example_DDPs/Google_Search_History/"
out = scanfolder.scan_folder(example)
out.to_excel("test.xlsx")


######################################
import logging
import importlib
logging.basicConfig(level=logging.INFO)

from examineddp.ddpinspect import scanjson
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
from examineddp.ddpinspect import scanjson

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
import io


#log to stream
#log_stream = io.StringIO()    
#logging.basicConfig(stream=log_stream, level=logging.INFO)

logging.basicConfig(level=logging.INFO)

from ddpinspect import unzipddp
from ddpinspect import twitter


twitter_zip = "./example_ddps/twitter/twitter-2022-09-08-7b4bc3e1887ddc4becc57fb106a7a4e86751b45fa7b18258909a2a52bd73af08.zip"

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


print(log_stream.getvalue())

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


###################################################

from ddpinspect import unzipddp
from ddpinspect import instagram

import logging 
my_zip = "./example_ddps/instagram/turboknul_20220921.zip"

logging.basicConfig(level=logging.DEBUG)

# Happy flow
my_bytes = unzipddp.extract_file_from_zip(my_zip, "ads_interests.json")  
my_dict = instagram.instagram_bytesio_to_dict(my_bytes)
check = instagram.instagram_interests_to_list(my_dict)
check


# Bad flow
my_bytes = unzipddp.extract_file_from_zip(my_zip, "ads_erets.json")  
my_dict = instagram.instagram_bytesio_to_dict(my_bytes)
check = instagram.instagram_interests_to_list(my_dict)
check

my_bytes = unzipddp.extract_file_from_zip(my_zip, "recent_follow_requests.json")  
my_dict = instagram.instagram_bytesio_to_dict(my_bytes)
check = instagram.instagram_interests_to_list(my_dict)
check


###################################################

from ddpinspect import scanfiles
import logging 

my_folder = "./example_ddps/instagram/turboknul_20220921/"

logging.basicConfig(level=logging.DEBUG)

dir(scanfiles)

# Happy flow
scanfiles.flatten_json_all(my_folder)
scanfiles.scan_files_all(my_folder)


# Bad flow
my_folder = "./example_ddps/instagram/turboknul_201/"
scanfiles.scan_files_all(my_folder)

###################################################

from pathlib import Path

my_folder = "./example_ddps/instagram/turboknul_20220921/"
my_fer = "./exapedp/ntrm/turboknul_20220921/"

yay = Path(my_folder)
nay = Path(my_fer)


def path_exists(p: Path) -> None:
    """ Checks if path exists """
    if p.exists():
        return None
    else :
        raise FileNotFoundError(f"Path: {p} does not exists")



###################################################
# your_topics

from ddpinspect import instagram
from ddpinspect import unzipddp

import logging 
my_zip = "./example_ddps/instagram/turboknul_20220921.zip"

logging.basicConfig(level=logging.DEBUG)

# Happy flow
my_bytes = unzipddp.extract_file_from_zip(my_zip, "your_topics.json")  
my_dict = instagram.instagram_bytesio_to_dict(my_bytes)
check = instagram.instagram_your_topics_to_list(my_dict)
check




###################################################

from ddpinspect import instagram

my_zip = "./example_ddps/instagram/turboknul_20220921.zip"
my_zip = "./example_ddps/instagram/turboknul_20220926_html.zip"
x = instagram.validate_instagram_zip(my_zip)
x.get_status_message()
x.get_status_description()
x.status_code = 123



###################################################

from ddpinspect import twitter
dir(twitter)

my_zip = "./example_ddps/twitter/twitter-2022-09-08-7b4bc3e1887ddc4becc57fb106a7a4e86751b45fa7b18258909a2a52bd73af08.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "personalization.js")
my_dict = twitter.bytesio_to_listdict(my_bytes)
check = twitter.interests_to_list(my_dict)
check 


###################################################

import csv
import io
from ddpinspect import unzipddp
import pandas as pd

my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "Liked videos.csv")
out =  []
with io.TextIOWrapper(my_bytes, encoding="utf8") as b:
    reader = csv.DictReader(b)
    for row in reader:
        out.append(row)

out[10]




###################################################

from ddpinspect import unzipddp
from ddpinspect import scanfiles
import pandas as pd
import logging 
import json 
import io 
logging.basicConfig(level=logging.DEBUG)


my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "watch-history.json")
my_d = unzipddp.read_json_from_bytes(my_bytes)

df = pd.DataFrame([scanfiles.dict_denester(d) for d in my_d])

pd.to_datetime(df['time']).isoformat() > (datetime.now() - timedelta(days=360)).isoformat()


from datetime import datetime, timedelta



def watch_history_to_df(history: dict[Any, Any]) -> pd.DataFrame:
    df = pd.DataFrame([scanfiles.dict_denester(d) for d in out])



json.load(my_bytes)

time = [
    "2022-01-02",
    "2022-02-01",
    "2022-02-28"
]

pd.to_datetime(time, infer_datetime_format=True)

time = [
    "2022-13-02",
    "2022-02-01",
    "2022-02-28"
]

pd.to_datetime(time, infer_datetime_format=True)

time = [
    "20-02-2022",
    "13-02-2022",
    "02-13-2022",
    "01-02-2022",
    "01-02-2022",
    "01-02-2022",
    "01-02-2022",
    "20-02-2022",
    "20-02-2022",
    "20-02-2022",
]

pd.to_datetime(time, infer_datetime_format=True)






# to_datetime is by far the fastest option
# infer_datetime_format

# Not ISO TIME can be understood by to_datetime
# This case it infers the MMDDYYYY and applies it to the df
time = [
    "11-30-2022",
    "01-13-2022",
    "01-02-2022",
]

# Not ISO TIME can be understood by to_datetime
# This case it infers the DDMMYYYY and applies it to the df
# Warns for 11-30-2022
time = [
    "01-02-2022",
    "11-30-2022",
    "30-11-2022",
]

# Not ISO TIME can be understood by to_datetime
# This case it infers the DDMMYYYY and applies it to the df
# Warns for the rest
time = [
    "01-02-2022",
    "01-13-2022",
    "01-14-2022",
    "01-15-2022",
]

# infers month first
time = [
    "01-13-2022",
    "01-14-2022",
    "01-15-2022",
]

time = [
    "2020-03-02T14:28:23.382748",
    "2020-03-01T14:28:23.382748",
    "2020-02-01T14:28:23.382748"
]

########################################################################

import pandas as pd
import logging 
import re 


logging.basicConfig(level=logging.DEBUG)

regex_iso8601_full = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'

regex_iso8601_date = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$'

match_iso8601_full = re.compile(regex_iso8601_full).match
match_iso8601_date = re.compile(regex_iso8601_date).match


def is_isoformat(datetime_str, check_minimum: int, date_only: bool = False) -> bool:
    """
    Check if list-like object has ISO 8601 date strings
    """

    regex_iso8601_full = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    regex_iso8601_date = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$'

    regex = regex_iso8601_full if date_only is False else regex_iso8601_date 

    try:
        for i in range(min(len(datetime_str), check_minimum)):
            if re.fullmatch(regex, datetime_str[i]) is None:
                logging.info("Could not detect ISO 8601 timestamp (date_only=%s): %s", date_only, datetime_str[i])
                return False

    except Exception as e:
        logging.info("Could not detect ISO 8601 timestamp (date_only=%s): %s", date_only, datetime_str[i])
        return False

    logging.info("ISO 8601 timestamp detected (date_only=%s)", date_only)
    return True
    


def is_epoch(datetime_int, check_minimum: int) -> bool:
    """
    Check if list-like object with ints or str that can be interpreted as ints
    epoch time (unit seconds) fall between the start of year 2000 and the year 2040
    """

    year2000 = 946684800
    year2040 = 2208988800

    try:
        for i in range(min(len(datetime_int), check_minimum)):
            check_time = int(datetime_int[i])
            if not (year2000 <= check_time <= year2040):
                logging.info("Could not detect epoch time timestamp: %s", check_time)
                return False

    except Exception as e:
        logging.info("Could not detect epoch time timestamp, %s", e)
        return False

    logging.info("Epoch timestamp detected")
    return True




def convert_timestamp(datetime_str):
    """
    If timestamps are ISO 8601 return those
    If timestamps are ints (epochtime) return those

    If first ambigous non NaN timestamps is encoutered 
    (and can be detected with infer_datetime_format=True and dayfirst-True) 
    every timestamp is interpreted as DD/MM/YYYY if possible, 
    if resulting in incorrect timestamp, then MM/DD/YYYY is used, 
    converting format is silently switched
    
    If first non-ambigous non NaN timestamps is encoutered 
    (and can be detected with infer_datetime_format=True and dayfirst-True) 
    every timestamp is interpreted as either DD/MM/YYYY or MM/DD/YYYY depending on the first timestamp
    If the other format is encountered, that would result in an error, format is silently switched

    If timestamp format cannot be detected with infer_datetime_format
    dateutils.parser.parse() is used with dayfirst is true setting
    Interpretering everything as DD/MM/YYYY except if that results in incorrect interpretation,
    then MM/DD/YYYY is used

    YYYY/MM/DD formats not ISO 8601 will be interpreted incorrectly, as YYYY/DD/MM if possible

    Note 1: to_datetime will be rewritten in a future pandas release
    Also to_datetime, guess_datetime_format will be made available in pandas.tools
    The silent format changes will be changed. 

    Note 2: This is a very complicated problem to solve, solving this problem myself is too difficult
    for what I might expect to gain in accuracy

    Concluding: Although a lot can go wrong, I expect the impact will be minor, 
    When american formats are encourted regularly things will go wrong most often
    """
    out = None
    try:

        if is_isoformat(datetime_str, 10):
            out = pd.to_datetime(datetime_str)

        elif is_isoformat(datetime_str, 10, date_only=True):
            out = pd.to_datetime(datetime_str)

        elif is_epoch(datetime_str, 10):
            out =  pd.to_datetime(datetime_str, unit="s")

        else:
            out = pd.to_datetime(datetime_str, infer_datetime_format=True, dayfirst=True)
        
    except (ValueError, TypeError) as e:
        logging.error("Could not convert timestamps: %s", e)
        raise e

    return out



is_isoformat(["2020-12-02T14:28:23.382748", "2020-12-01T14:28:23.382748"])
["1662630968", "2000000968"]
[pd.Timestamp("2022-09-08 09:56:08"), pd.Timestamp("2033-05-18 03:49:28")]
[1662630968, 2000000968]
[pd.Timestamp("2022-09-08 09:56:08"), pd.Timestamp("2033-05-18 03:49:28")]
["01/01/2022, 15:10:17", "02/01/2022, 15:20:25"]
["01-02-2022", "01-10-2022"]
["12-31-2022", "02-01-2022"]

["02-01-2022", "12-31-2022"]
["2022/02/01", "2022/01/02"]
["2022/01/02", "2022/02/01"]


convert_timestamp(["20200208"])
convert_timestamp(["20200102", "20200201"])
convert_timestamp(["2020-01-02", "2020-02-01"])


is_isoformat(["20200208"],10, date_only = True)
is_isoformat(["20200102", "20200201"], 10)
is_isoformat(["2020-12-02", "2020-01-01"], 10, date_only = True)


