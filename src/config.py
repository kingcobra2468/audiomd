from dotenv import load_dotenv
import os

DOT_ENV_PATH = './.env'

load_dotenv('./.env')

# Selenium
HEADLESS = False
GECKODRIVER_PATH = './bin/selenium/geckodriver'
EXTENSIONS_DIR = './bin/selenium/extensions/'

# YT Client
DOWNLOAD_TYPE = 'MP3'  # either 'MP3' or 'MP4'
OUTPUT_DIR = '/mnt/harddrive/Programming/Python/TMTrack/Songs_v2/'  # output directory

# METADATA SCRAPPER
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

# SCRAPPER SETTINGS
MAX_WORKERS = 15
CONTENT_SCRAPPER = 'youtube_dl'  # possible options are 'youtube_dl' or 'ytmp3'
METADATA_SCRAPPERS = ['deezer']  # possible options are 'deezer'

# Youtube-DL Settings
YDL_FILENAME='%(id)s'

# CSV SETTINGS
CSV_FILE_PATH = './'
CSV_FILE_NAME = 'song_data.csv'
