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
import pandas as pd

my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"

my_bytes = unzipddp.extract_file_from_zip(my_zip, "watch-history.json")
watch_history = unzipddp.read_json_from_bytes(my_bytes)
df = youtube.to_df(watch_history)

def crunch_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove all columns that have constant values
    if the number of rows is larger than 1
    """
    if len(df.index) > 1:
        cols = df.columns[df.nunique(dropna=False) >= 2]
        df = df[cols]

    return df

x = crunch_df(pd.DataFrame())

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
logging.basicConfig(level=logging.INFO)

from ddpinspect import unzipddp
from ddpinspect import youtube

my_zip = "/home/turbo/ddp-inspector/example_ddps/youtube/takeout_nl.zip"
my_zip = "/home/turbo/ddp-inspector/example_ddps/youtube/takeout-20220921T133717Z-001.zip"

my_bytes = unzipddp.extract_file_from_zip(my_zip, "my-comments.html")
df = youtube.comments_to_df(my_bytes)
df



##################################################################
# check if

import logging 
logging.basicConfig(level=logging.INFO)

from ddpinspect import twitter
from ddpinspect import unzipddp

myzip = "./example_ddps/twitter/twitter-2022-09-08-7b4bc3e1887ddc4becc57fb106a7a4e86751b45fa7b18258909a2a52bd73af08.zip"
my_bytes = unzipddp.extract_file_from_zip(myzip, "account.js")  
my_dict = twitter.bytesio_to_listdict(my_bytes)
check = twitter.account_created_at_to_list(my_dict)
check



##################################################################
# instgram creation date
# Go with dict_denester approach
# easier to deal with in the future

from ddpinspect import unzipddp
from ddpinspect import instagram
from ddpinspect import facebook
from ddpinspect import scanfiles
from parserlib import stringparse
import logging

my_zip = "./example_ddps/instagram/turboknul_20220921.zip"
logging.basicConfig(level=logging.DEBUG)

# Happy flow
my_bytes = unzipddp.extract_file_from_zip(my_zip, "signup_information.json")  
my_dict = unzipddp.read_json_from_bytes(my_bytes)
instagram.account_created_at_to_list(my_dict)


my_zip = "/home/turbo/ddp-inspector/example_ddps/facebook/facebook-niek.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "profile_information.json")  
my_dict = unzipddp.read_json_from_bytes(my_bytes)
facebook.account_created_at_to_list(my_dict)

###########################################
# test rewritten read_json_from_file 

from ddpinspect import unzipddp
from ddpinspect import instagram
from ddpinspect import facebook
from ddpinspect import scanfiles
import logging
import io


logging.basicConfig(level=logging.DEBUG)

json_to_test = io.BytesIO(b'\xef\xbb\xbf{"a":"b"}')
unzipddp.read_json_from_bytes(json_to_test)


json_to_test = io.BytesIO(b'{"a":"b"}')
unzipddp.read_json_from_bytes(json_to_test)




##############################################
# Prototype comments


my_bytes = unzipddp.extract_file_from_zip(my_zip, "profile_information.json")  
my_dict = unzipddp.read_json_from_bytes(my_bytes)
facebook.account_created_at_to_list(my_dict)

###########################################
# test rewritten read_json_from_file 

from bs4 import BeautifulSoup
from ddpinspect import unzipddp
from ddpinspect import youtube
from ddpinspect import scanfiles
import logging
import io

logging.basicConfig(level=logging.DEBUG)

my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "my-comments.html")  

youtube.comments_to_df(my_bytes)

import re
import pandas as pd

def comments_to_df(comments: io.BytesIO) -> pd.DataFrame:
    """
    Parse comments from Youtube DDP 

    returns a pd.DataFrame
    with the comment, type of comment, and a video url
    """

    data_set = []
    df = pd.DataFrame()

    video_regex = r"(?P<video_url>^http[s]?://www\.youtube\.com/watch\?v=[a-z,A-Z,0-9,\-,_]+)(?P<rest>$|&.*)"
    video_pattern = re.compile(video_regex)

    # Big try except block due to lack of time
    try:
        soup = BeautifulSoup(comments, "html.parser")
        items = soup.find_all("li")
        for item in items:
            data_point = {}

            # Extract comments
            content = item.get_text(separator="<SEP>").split("<SEP>")
            message = content.pop()
            action = "".join(content)
            data_point["Comment"] = message
            data_point["Type of comment"] = action

            # Search through all references
            # if a video can be found:
            # 1. extract video url
            # 2. add data point
            for ref in item.find_all("a"):
                regex_result = video_pattern.match(ref.get("href"))
                if regex_result:
                    data_point["Video url"] = regex_result.group("video_url")
                    data_set.append(data_point)
                    break

        df = pd.DataFrame(data_set)

    except Exception as e:
        print(e)
        #logger.error("Exception was caught:  %s", e)

    finally:
        return df


url =  "http://www.youtube.com/watch?v=l3wswFnxhTE&lc=UgxBlYMVwrJxa_E3BFV4AaABAg"

import re



my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "my-comments.html")  
df1 = youtube.comments_to_df(my_bytes)

my_zip = "./example_ddps/youtube/takeout-20220921T133717Z-001.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "my-comments.html")  
df2 = comments_to_df(my_bytes)

for index, row in df1.iterrows():
    if row["Comment"] not in df2["Comment"].tolist():
        print("=====================================================")
        print(index)
        print(row["Comment"])
        print(row["Type of comment"])
        print(row["Context of comment 1"])
        print(row["Context of comment 2"])
        print(row["Context of comment 3"])




video_regex = r"(?P<video_url>^http[s]?://www\.youtube\.com/watch\?v=[a-z,A-Z,0-9,-,_]+)(?P<rest>$|&.*)"
video_pattern = re.compile(video_regex)

video_pattern.match("http://www.youtube.com/watch?v=g-qkhw_u2M8")


##############################################################
# Extract watch history html


from ddpinspect import youtube
from ddpinspect import unzipddp
import logging

logging.basicConfig(level=logging.DEBUG)

my_zip = "./example_ddps/youtube/takeout_youtube_html.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "kijkgeschiedenis.html")  
youtube.watch_history_html_to_df(my_bytes)



##############################################################
from ddpinspect import youtube
from ddpinspect import unzipddp
from bs4 import BeautifulSoup
import logging
import io

def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i)<128)

logging.basicConfig(level=logging.DEBUG)

my_zip = "/home/turbo/Downloads/youtube.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "watch-history.html")  
check = my_bytes.getvalue().decode("utf-8", errors="ignore")
check = remove_non_ascii_1(check)
check

soup = BeautifulSoup(check, "html.parser")


my_zip = "/home/turbo/Downloads/youtube.zip"
my_bytes = unzipddp.extract_file_from_zip(my_zip, "watch-history.html")  
youtube.watch_history_html_to_df(my_bytes)

