# YouTube MP3 Data Generation Tool 

#### Tool for using Youtube videos for generating an audio dataset. Downloads youtube video using ytmp3 web service and extracts possible metadata using Deezer API. 

### **Installation Steps**
1. Clone the repository onto local machine
2. Sign up for a FREE [RapidAPI](https://rapidapi.com) account and get the API key for the service.
3. Download a geckodriver and ad blocker. As of now only works with [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases). Additionally, all testing has been performed with [uBlock extension](https://github.com/gorhill/uBlock/releases/download/1.32.1b0/uBlock0_1.32.1b0.firefox.signed.xpi).
4. Install python dependencies with `pip3 install -r requirements.txt`
5. Run tool by running `python3 run.py` script with additional arguments to be discussed in a section below.

### **Configuration**

#### **Dotenv File**
A `.env` needs to be created inside of `/src` directory unless otherwise specified in the `config.py` `DOT_ENV_PATH` setting. Variables in the `.env` file include:
- **RAPIDAPI_KEY=** stores the RapidAPI API key.

#### **Config File**
The `config.py` file under `/src` stores global configuration details and constants used throughout the program. Settings in the `config.py` file include:
- **DOT_ENV_PATH=** path to the dotenv file
- **HEADLESS=** hether to run selenium in headless mode. **NOT** currently implamented thus setting has no effect as of now.
- **GECKODRIVER_PATH=** path to the geckodriver binary
- **EXTENSIONS_DIR=** directory where all extensions should be stored. Ex the Ublock extension.
- **DOWNLOAD_TYPE=** whether to download videos as mp4 or mp3.
- **OUTPUT_DIR=** directory where the downloaded mp3/mp4 files should go.
- **RAPIDAPI_KEY=** do not touch. automatically loads it from dotenv file.
- **MAX_WORKERS=** concurrency multiplier. Max number of workers.
- **CSV_FILE_PATH=** directory of csv file for metadata of songs
- **CSV_FILE_NAME=** name of csv file for metadata of songs

#### **Data Config File**
The `data_config.py` file under `/src/data_harvesting` stores  configuration details and constants related to CSV labels. Settings in the `data_config.py` file include:
- **LABELS=** labels to be used for the CSV file. Note that changing the labels would also require changing logic inside of `record.py` to populate these labels. By default all labels are set to an empty string.

### **CommandLine options for `run.py`**
Use only one or the two. File flag has dominance in the case of both flags being accidently used.
- `-u/--url` URL for yt video to be downloaded. Flags could be repeated as internally a list is created of all the links. Additionally, an optional Deezer title could be provided through a **","** (comma) delimeter for improving query results for Deezer's search query.
- `-f/--file` File that holds onto all of the yt video links. Additionally, on the same line as url link, an optional Deezer title could be provided through a **","** (comma) delimeter for improving query results for Deezer's search query. 