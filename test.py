######################################################################################################
# My own testing grounds
# pieces of code that I run to test stuff

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
log_stream = io.StringIO()    
logging.basicConfig(stream=log_stream, level=logging.INFO)




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
my_bytes = unzipddp.extract_file_from_zip(my_zip, "subscriptions.csv")
data = unzipddp.read_csv_from_bytes(my_bytes)

df = pd.DataFrame(data)
df.to_excel("subscriptions.xlsx")



########################################################################


import logging 

logging.basicConfig(level=logging.DEBUG)

from ddpinspect import unzipddp
from ddpinspect import scanfiles
from ddpinspect import youtube


my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"

my_bytes = unzipddp.extract_file_from_zip(my_zip, "watch-history.json")
watch_history = unzipddp.read_json_from_bytes(my_bytes)
df = youtube.watch_history_to_df(watch_history)

df.to_excel("watch_history.xlsx")


scanfiles.dict_denester(watch_history)
dir(unzipddp)



############################################################################
import pandas as pd

import logging
import io

#log to stream
log_stream = io.StringIO()    
logging.basicConfig(stream=log_stream,
                    level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z"
                    )

from ddpinspect import unzipddp
from ddpinspect import scanfiles
from ddpinspect import youtube

my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"

my_bytes = unzipddp.extract_file_from_zip(my_zip, "watch-history.json")
watch_history = unzipddp.read_json_from_bytes(my_bytes)
df = youtube.to_df(watch_history)

log_stream.getvalue()

log_stream.truncate(0)
log_stream.seek(0)

pd.DataFrame(LOG_STREAM.getvalue().split("\n"), columns=["log messages"])


def create_log_table():
    log_string = LOG_STREAM.getvalue()  # read the log stream
    LOG_STREAM.truncate(0)              # flush stream
    LOG_STREAM.seek(0)

    if log_string:
        log_data = log_string.split("\n")
    else:
        log_data = ["no log messages"]

    df_logs = pd.DataFrame(log_data, columns=["Log Messages"])

    return PropsUIPromptConsentFormTable("log_messages", "Log messages:", df_logs)

###########

##################################################################

from ddpinspect import instagram
my_zip = "/home/turbo/ddp-inspector/example_ddps/instagram/turboknul_20220921.zip"


validation = instagram.validate_zip(my_zip)
validation.status_code.id
validation
assert validation.status_code.id == expected



##################################################################
import logging 
logging.basicConfig(level=logging.DEBUG)

from ddpinspect import facebook
from ddpinspect import unzipddp
my_zip = "/home/turbo/ddp-inspector/example_ddps/facebook/facebook.zip"


validation = facebook.validate_zip(my_zip)
validation.status_code.id


my_bytes = unzipddp.extract_file_from_zip(my_zip, "ads_interests.json")
res = unzipddp.read_json_from_bytes(my_bytes)
facebook.interests_to_list(res)


res["topics_v2"]

my_bytes = unzipddp.extract_file_from_zip(my_zip, "your_topics.json")
res = unzipddp.read_json_from_bytes(my_bytes)
res
facebook.your_topics_to_list(res)



##################################################################
# Comments scrape

import logging 
logging.basicConfig(level=logging.DEBUG)

from ddpinspect import unzipddp

my_zip = "/home/turbo/ddp-inspector/example_ddps/youtube/takeout-20220921T133717Z-001.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "my-comments.html")

import pandas as pd

from bs4 import BeautifulSoup


def comments_to_df(comments):
    """
    Parse comments from Youtube DDP
    Function can handle any language 
    Note a tradeoff has been made between having clean data and interpretability for the participant
    """

    data_set = []

    # Big try except block due to lack of time
    try:
        soup = BeautifulSoup(comments, "html.parser")
        items = soup.find_all("li")
        for item in items:
            data_point = {}

            # Extract comments
            content = item.get_text(separator="<SEP>").split("<SEP>")
            message = content.pop()
            action = ''.join(content)
            data_point["Comment"] = message
            data_point["Type of comment"] = action

            # Extract references
            for i, ref in enumerate(item.find_all("a")):
                data_point[f"Context of comment {i + 1}"] = ref.text  + ': ' + ref.get("href")
                
            data_set.append(data_point)

        df = pd.DataFrame(data_set)
    except:
        df = pd.DataFrame()
        
    return df


df.to_excel("./TEST_EXCEL.xlsx")


