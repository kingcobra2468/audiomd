# YouTube MP3 Data Generation Tool 

Tool for generating an audio dataset for Youtube videos. Downloads Youtube videos using one of the available content scrappers and extracts possible metadata using the selected subset of metadata scrappers. 

## **Setup**
Regardless of the content and metadata scrappers used, the following steps must be done.
1. Install python dependencies with `pip3 install -r requirements.txt`.
2. Configure the content and metadata scrapper that will be used.
3. Run tool by running `python3 run.py` script with additional arguments to be discussed in a section below.

### **Setup for Selenium-based Scrappers**
If a selenium-based scrapper is configured, the following setup steps must be done. 
1. Download a geckodriver and ad blocker. As of now only works with [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases).
2. (Optional) Install extension such as [uBlock extension](https://github.com/gorhill/uBlock/releases/download/1.32.1b0/uBlock0_1.32.1b0.firefox.signed.xpi). *Note: given that many sites have pop-ups, it is best to do this step to avoid undefined behavior*.

### **Setup for Deezer Metadata Scrapper**
1. Sign up for a FREE [RapidAPI](https://rapidapi.com) account and get the API key for the service.
2. Put the API key in its correct location in the dotenv file.
   
## **Configuration**

### **Dotenv File**
A `.env` needs to be created inside of `'src/` directory unless otherwise specified in the `config.py` `DOT_ENV_PATH` setting. A sample `.env` file, called `.env.template`, exists in the project root directory and could be copied as a template. Variables in the `.env` file include:
- **RAPIDAPI_KEY=** stores the RapidAPI API key.

### **Config File**
The `config.py` file under `/src` stores global configuration details and constants used throughout the program. Settings in the `config.py` file include:
- **DOT_ENV_PATH=** path to the dotenv file.
- **HEADLESS=** whether to run selenium in headless mode. **NOT** currently implamented thus setting has no effect as of now.
- **GECKODRIVER_PATH=** path to the geckodriver binary.
- **EXTENSIONS_DIR=** directory where all extensions should be stored. Ex the Ublock extension.
- **DOWNLOAD_TYPE=** whether to download videos as mp4 or mp3.
- **OUTPUT_DIR=** directory where the downloaded mp3/mp4 files should go.
- **RAPIDAPI_KEY=** do not touch. automatically loads it from dotenv file.
- **MAX_WORKERS=** concurrency multiplier. Max number of workers.
- **CSV_FILE_PATH=** directory of csv file for metadata of songs.
- **CSV_FILE_NAME=** name of csv file for metadata of songs.
- **CONTENT_SCRAPPER=** the content scrapper that will be used to fetch the content.
- **METADATA_SCRAPPERS=** list of metadata scrappers that will be used for generating the csv.

## **Scrappers**
Within AudioMD, there exists two type of scrappers: metadata and content.  Both content and metadata scrappers can exist under two forms: api and web. Web-based scrappers are built on top of Selenium, and will require Selenium to be configured on the machine. API based scrappers are driven by web APIs/libraries and might require API keys and/or the creation of accounts to work.

### **Content Scrappers**
Content scrappers are intended at working with a Youtube video. The Youtube video will be download and put in the specified output directory on the local machine.

#### **Youtube-dl Scrapper**
This scrapper is based on the youtube-dl project. The scrapper is an api-based scrapper and requires no addtional configuration by the user. This scrapper is could be included as **'youtube_dl'**.

#### **YTmp3 Scrapper**
This scrapper is a selenium wrapper over ytmp3.cc website. Since this is a web-based scrapper, it will require Selenium to be [configured](#setup-for-selenium-based-scrappers). This scrapper is could be included as **'ytmp3'**.

### **Metadata Scrappers**
Metadata scrappers work by collecting additional metadata for a given youtube video by doing looked up based on the video title(unless overrided by the user).

#### **Deezer Scrapper**
This scrapper is a Deezer metadata wrapper which offers various metadata for a given song title. This scrapper requires the creation of a Rapid API account, and for the [generation of an API access key](#setup-for-deezer-metadata-scrapper). This scrapper is could be included as **'deezer'**.


## Sample Dataset Schema
With the content scrapper set to **youtube_dl** and the metadata scrapper set to **deezer**, the generated dataset consists of 5 columns labled: [artist, explicit, genre, file_name, youtube_url].

- **artist(string)=** the artist name(from deezer).
- **explicit(bool)=** whether the song is considered explicit(from deezer).
- **genre(string)=** genre type of the song(from deezer).
- **file_name(string)=** the name of the mp3 under the directory that was specified as **OUTPUT_DIR**.
- **youtube_url(string)=** the original youtube url that was used as the content to be downloaded.

### **Sample Data**
```
artist,explicit,genre,file_name,youtube_url
John Coltrane,False,,They Say It's Wonderful,"https://www.youtube.com/watch?v=vBlSbNTqOFM"
The Ink Spots,False,,To Each His Own (Karaoke Version),"https://www.youtube.com/watch?v=kruDTlJHmdo"
Ella Fitzgerald,False,,You Won't Be Satisfied Until You Break My Heart,"https://www.youtube.com/watch?v=sEueAU1Hqfo"
```

## **CommandLine options for `run.py`**
Use only one or the two. File flag has dominance in the case of both flags being accidently used.
- `-u/--url` URL for yt video to be downloaded. Flags could be repeated as internally a list is created of all the links. Additionally, an optional Deezer title could be provided through a **","** (comma) delimiter for improving query results for Deezer's search query.
- `-f/--file` File that holds onto all of the yt video links. Additionally, on the same line as url link, an optional Deezer title could be provided through a **","** (comma) delimiter for improving query results for Deezer's search query. 