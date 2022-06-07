[![Betterme](https://telegra.ph/file/044017033ca7028c9fc85.jpg)](https://youtu.be/s2TktuIA9-s)

# Eunha Mirror
![GitHub Repo stars](https://img.shields.io/github/stars/vincreator/eunhamirror?color=blue&style=flat)
![GitHub forks](https://img.shields.io/github/forks/vincreator/eunhamirror?color=green&style=flat)
![GitHub issues](https://img.shields.io/github/issues/vincreator/eunhamirror)
![GitHub closed issues](https://img.shields.io/github/issues-closed/vincreator/eunhamirror)
![GitHub pull requests](https://img.shields.io/github/issues-pr/vincreator/eunhamirror)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/vincreator/eunhamirror)
![GitHub contributors](https://img.shields.io/github/contributors/vincreator/eunhamirror?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/vincreator/eunhamirror?color=red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/vincreator/eunhamirror)
![GitHub](https://img.shields.io/github/license/vincreator/eunhamirror)
[![Channel](https://img.shields.io/badge/Channel-blue)](https://t.me/Namexian)

**Eunha Mirror** is a _multipurpose_ Telegram Bot writen in Python for mirroring files on the Internet to Google Drive and Upload to telegram.

# Features supported:
<details>
    <summary><b>Click Here For More Details</b></summary>

- Mirror direct download links, Torrent, and Telegram files to Google Drive
- Mirror Mega.nz links to Google Drive
- Copy files from someone's Drive to your Drive (Using Autorclone)
- Download/Upload progress, Speeds and ETAs
- Mirror all yt-dlp supported links
- Docker support
- Uploading to Team Drive
- Index Link support
- Service Account support
- Delete files from Drive
- Shortener support
- Multiple Trackers support
- Shell and Executor
- Add sudo users
- Custom Filename* (Only for direct links, Telegram files and yt-dlp. Not for Mega links, Gdrive links or Torrents)
- Extract password protected files
- Extract these filetypes and uploads to Google Drive
  > ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, NTFS, RPM, SquashFS, UDF, VHD, XAR, Z, TAR.XZ
- qBittorrent
- Select files from Torrent before downloading using qbittorrent
- Leech (splitting, thumbnail for each user, setting as document or as media for each user)
- Size limiting for Torrent/Direct, Zip/Unzip, Mega and Clone
- Stop duplicates for all tasks except yt-dlp tasks
- Zip/Unzip G-Drive links
- Counting files/folders from Google Drive link
- View Link button, extra button to open file index link in broswer instead of direct download
- Status Pages for unlimited tasks
- Clone status
- Search in multiple Drive folder/TeamDrive
- Recursive Search (only with `root` or TeamDrive ID, folder ids will be listed with non-recursive method)
- Multi-TD list by token.pickle if exists
- Extract rar, zip and 7z splits with or without password
- Zip file/folder with or without password
- Use Token.pickle if file not found with Service Account for all Gdrive functions
- Random Service Account at startup
- Mirror/Leech/Watch/Clone/Count/Del by reply
- YT-DLP quality buttons
- Search on torrents with Torrent Search API or with variable plugins using qBittorrent search engine
- Docker image support for linux `amd64, arm64, arm/v7, arm/v6, s390x, arm64/v8` (**Note**: Use `anasty17/mltb:arm64` for `arm64/v8` or oracle)
- Update bot at startup and with restart command using `UPSTREAM_REPO`
- Qbittorrent seed until reaching specific ratio or time
- Rss feed and filter. Based on this repository [rss-chan](https://github.com/hyPnOtICDo0g/rss-chan)
- Save leech settings including thumbnails in database
- Mirror/Leech/Clone multi links/files with one command
- Extenstion Filter for uploading/cloning files
- Incomplete task notifier to get incomplete task messages after restart, works with database.

- Direct links Supported:
```
letsupload.io, hxfile.co, anonfiles.com, bayfiles.com, antfiles, fembed.com, fembed.net, femax20.com, layarkacaxxi.icu, fcdn.stream, sbplay.org, naniplay.com, naniplay.nanime.in, naniplay.nanime.biz, sbembed.com, streamtape.com, streamsb.net, feurl.com, pixeldrain.com, racaty.net, 1fichier.com, 1drv.ms (Only works for file not folder or business account), uptobox.com (Uptobox account must be premium) and solidfiles.com
```
</details>

# How to deploy?
Deploying is pretty much straight forward and is divided into several steps as follows:

## Installing requirements
<details>
    <summary><b>Click here for more details</b></summary>

- Clone this repo:
```
git clone https://github.com/vincreator/eunha/
cd mirrorbot
```

- Install requirements
For Debian based distros
```
sudo apt install python3
```
Install Docker by following the [`official Docker docs`](https://docs.docker.com/engine/install/debian/)

OR
```
sudo snap install docker 
```
- For Arch and it's derivatives:
```
sudo pacman -S docker python
```
- Install dependencies for running setup scripts:
```
pip3 install -r requirements-cli.txt
```
</details>

## Setting up config file
<details>
    <summary><b>Click here for more details</b></summary>

```
cp config_sample.env config.env
```
- Remove the first line saying:
```
_____REMOVE_THIS_LINE_____=True
```
Fill up rest of the fields. Meaning of each fields are discussed below:
### Required Field
- `BOT_TOKEN`: The Telegram Bot Token that you got from [@BotFather](https://t.me/BotFather)
- `GDRIVE_FOLDER_ID`: This is the Folder/TeamDrive ID of the Google Drive Folder to which you want to upload all the mirrors.
- `OWNER_ID`: The Telegram User ID (not username) of the Owner of the bot. `Int`
- `DOWNLOAD_DIR`: The path to the local folder where the downloads should be downloaded to.
- `DOWNLOAD_STATUS_UPDATE_INTERVAL`: Time in seconds after which the progress/status message will be updated. Recommended `10` seconds at least. `Int`
- `AUTO_DELETE_MESSAGE_DURATION`: Interval of time (in seconds), after which the bot deletes it's message and command message which is expected to be viewed instantly. **NOTE**: Set to `-1` to disable auto message deletion. `Int`
- `IS_TEAM_DRIVE`: Set `True` if uploading to TeamDrive. Default is `False`. `Bool`
- `TELEGRAM_API`: This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org. `Int`
- `TELEGRAM_HASH`: This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org.

**2. Optional Fields**
- `DATABASE_URL`: Your SQL Database URL. Follow this [Generate Database](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#generate-database) to generate database. Data will be saved in Database: auth and sudo users, leech settings including thumbnails for each user, rss data and incomplete tasks. **NOTE**: If deploying on heroku and using heroku postgresql delete this variable from **config.env** file. **DATABASE_URL** will be grabbed from heroku variables.
- `AUTHORIZED_CHATS`: Fill user_id and chat_id of groups/users you want to authorize. Separate them by space.
- `SUDO_USERS`: Fill user_id of users whom you want to give sudo permission. Separate them by space.
- `IGNORE_PENDING_REQUESTS`: Ignore pending requests after restart. Default is `False`. `Bool`
- `USE_SERVICE_ACCOUNTS`: Whether to use Service Accounts or not. For this to work see [Using Service Accounts](https://github.com/anasty17/mirror-leech-telegram-bot#generate-service-accounts-what-is-service-account) section below. Default is `False`. `Bool`
- `INDEX_URL`: Refer to https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index.
- `STATUS_LIMIT`: Limit the no. of tasks shown in status message with buttons. **NOTE**: Recommended limit is `4` tasks.
- `STOP_DUPLICATE`: Bot will check file in Drive, if it is present in Drive, downloading or cloning will be stopped. (**NOTE**: File will be checked using filename not file hash, so this feature is not perfect yet). Default is `False`. `Bool`
- `CMD_INDEX`: commands index number. This number will added at the end all commands.
- `UPTOBOX_TOKEN`: Uptobox token to mirror uptobox links. Get it from [Uptobox Premium Account](https://uptobox.com/my_account).
- `TORRENT_TIMEOUT`: Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds.
- `EXTENTION_FILTER`: File extentions that won't upload/clone. Separate them by space.
- `INCOMPLETE_TASK_NOTIFIER`: Get incomplete task messages after restart. Require database and (supergroup or channel). Default is `False`. `Bool`

### Update
- `UPSTREAM_REPO`: Your github repository link, if your repo is private add `https://username:{githubtoken}@github.com/{username}/{reponame}` format. Get token from [Github settings](https://github.com/settings/tokens). So you can update your bot from filled repository on each restart. **NOTE**: Any change in docker or requirements you need to deploy/build again with updated repo to take effect. DON'T delete .gitignore file. For more information read [THIS](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#upstream-repo-recommended).
- `UPSTREAM_BRANCH`: Upstream branch for update. Default is `master`.

### Leech
- `TG_SPLIT_SIZE`: Size of split in bytes. Default is `2GB`.
- `AS_DOCUMENT`: Default type of Telegram file upload. Default is `False` mean as media. `Bool`
- `EQUAL_SPLITS`: Split files larger than **TG_SPLIT_SIZE** into equal parts size (Not working with zip cmd). Default is `False`. `Bool`
- `CUSTOM_FILENAME`: Add custom word to leeched file name.

### qBittorrent
- `BASE_URL_OF_BOT`: Valid BASE URL where the bot is deployed to use qbittorrent web selection. Format of URL should be `http://myip`, where `myip` is the IP/Domain(public) of your bot or if you have chosen port other than `80` so write it in this format `http://myip:port` (`http` and not `https`). This Var is optional on VPS and required for Heroku specially to avoid app sleeping/idling. For Heroku fill `https://yourappname.herokuapp.com`. Still got idling? You can use http://cron-job.org to ping your Heroku app.
- `SERVER_PORT`: Only For VPS even if `IS_VPS` is `False`, which is the **BASE_URL_OF_BOT** Port.
- `WEB_PINCODE`: If empty or `False` means no more pincode required while qbit web selection. `Bool`
- `QB_SEED`: QB torrent will be seeded after and while uploading until reaching specific ratio or time, edit `MaxRatio` or `GlobalMaxSeedingMinutes` or both from qbittorrent.conf (`-1` means no limit, but u can cancel manually by gid). **NOTE**: 1. Don't change `MaxRatioAction`, 2. Only works with `/qbmirror` and `/qbzipmirror`. Default is `False`. `Bool`
  - **Qbittorrent NOTE**: If your facing ram exceeded issue then set limit for `MaxConnecs`, decrease `AsyncIOThreadsCount` in qbittorrent config and set limit of `DiskWriteCacheSize` to `32`.

### RSS
- `RSS_DELAY`: Time in seconds for rss refresh interval. Recommended `900` second at least. Default is `900` in sec.
- `RSS_COMMAND`: Choose command for the desired action.
- `RSS_CHAT_ID`: Chat ID where rss links will be sent. If using channel then add channel id.
- `USER_SESSION_STRING`: To send rss links from your telegram account instead of adding bot to channel then linking the channel to group to get rss link since bot will not read command from itself or other bot. To generate session string use this command `python3 generate_string_session.py` after mounting repo folder for sure.
  - **RSS NOTE**: `DATABASE_URL` and `RSS_CHAT_ID` is required, otherwise all rss commands will not work. You must use bot in group. You can add the bot to a channel and add link this channel to group so messages sent by bot to channel will be forwarded to group without using `USER_STRING_SESSION`.

### Private Files
- `ACCOUNTS_ZIP_URL`: Only if you want to load your Service Account externally from an Index Link or by any direct download link NOT webpage link. Archive the accounts folder to ZIP file. Fill this with the direct download link of zip file. If index need authentication so add direct download as shown below:
  - `https://username:password@example.workers.dev/...`
- `TOKEN_PICKLE_URL`: Only if you want to load your **token.pickle** externally from an Index Link. Fill this with the direct link of that file.
- `MULTI_SEARCH_URL`: Check `drive_folder` setup [here](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#multi-search-ids). Write **drive_folder** file [here](https://gist.github.com/). Open the raw file of that gist, it's URL will be your required variable. Should be in this form after removing commit id: https://gist.githubusercontent.com/username/gist-id/raw/drive_folder
- `YT_COOKIES_URL`: Youtube authentication cookies. Check setup [Here](https://github.com/ytdl-org/youtube-dl#how-do-i-pass-cookies-to-youtube-dl). Use gist raw link and remove commit id from the link, so you can edit it from gists only.
- `NETRC_URL`: To create .netrc file contains authentication for aria2c and yt-dlp. Use gist raw link and remove commit id from the link, so you can edit it from gists only. **NOTE**: After editing .nterc you need to restart the docker or if deployed on heroku so restart dyno in case your edits related to aria2c authentication.
  - **NOTE**: All above url variables used incase you want edit them in future easily without deploying again or if you want to deploy from public fork. If deploying using cli or private fork you can leave these variables empty add token.pickle, accounts folder, drive_folder, .netrc and cookies.txt directly to root but you can't update them without rebuild OR simply leave all above variables and use private UPSTREAM_REPO.

### MEGA
- `MEGA_API_KEY`: Mega.nz API key to mirror mega.nz links. Get it from [Mega SDK Page](https://mega.nz/sdk)
- `MEGA_EMAIL_ID`: E-Mail ID used to sign up on mega.nz for using premium account.
- `MEGA_PASSWORD`: Password for mega.nz account.

### Shortener
- `SHORTENER_API`: Fill your Shortener API key.
- `SHORTENER`: Shortener URL.
  - Supported URL Shorteners:
  >exe.io, gplinks.in, shrinkme.io, urlshortx.com, shortzon.com, bit.ly, shorte.st, linkvertise.com , ouo.io, adfoc.us, cutt.ly

### GDTOT
- `CRYPT`: Cookie for gdtot google drive link generator. Follow these [steps](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#gdtot-cookies).

### Size Limits
- `TORRENT_DIRECT_LIMIT`: To limit the Torrent/Direct mirror size. Don't add unit. Default unit is `GB`.
- `ZIP_UNZIP_LIMIT`: To limit the size of zip and unzip commands. Don't add unit. Default unit is `GB`.
- `CLONE_LIMIT`: To limit the size of Google Drive folder/file which you can clone. Don't add unit. Default unit is `GB`.
- `MEGA_LIMIT`: To limit the size of Mega download. Don't add unit. Default unit is `GB`.
- `STORAGE_THRESHOLD`: To leave specific storage free and any download will lead to leave free storage less than this value will be cancelled. Don't add unit. Default unit is `GB`.

### Buttons
- `VIEW_LINK`: View Link button to open file Index Link in browser instead of direct download link, you can figure out if it's compatible with your Index code or not, open any video from you Index and check if its URL ends with `?a=view`, if yes make it `True`, compatible with [BhadooIndex](https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index) Code. Default is `False`. `Bool`

- Three buttons are already added including Drive Link, Index Link, and View Link, you can add extra buttons, if you don't know what are the below entries, simply leave them empty.
  - `BUTTON_FOUR_NAME`:
  - `BUTTON_FOUR_URL`:
  - `BUTTON_FIVE_NAME`:
  - `BUTTON_FIVE_URL`:
  - `BUTTON_SIX_NAME`:
  - `BUTTON_SIX_URL`:

### Torrent Search
- `SEARCH_API_LINK`: Search api app link. Get your api from deploying this [repository](https://github.com/Ryuk-me/Torrent-Api-py).
  - Supported Sites:
  >1337x, Piratebay, Nyaasi, Torlock, Torrent Galaxy, Zooqle, Kickass, Bitsearch, MagnetDL, Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject and YourBittorrent
- `SEARCH_LIMIT`: Search limit for search api, limit for each site and not overall result limit. Default is zero (Default api limit for each site).
- `SEARCH_PLUGINS`: List of qBittorrent search plugins (github raw links). I have added some plugins, you can remove/add plugins as you want. Main Source: [qBittorrent Search Plugins (Official/Unofficial)](https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins).
</details>

## Deploying
<details>
    <summary><b>Click here for more details</b></summary>
    
**IMPORTANT NOTE**: In start.sh you must replace $PORT with 80 or any other port you want to use

- Start Docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t eunhamirror
```
- Run the image:
```
sudo docker run -p 80:80 eunhamirror
```
OR

**NOTE**: If you want to use port other than 80, so change it in docker-compose.yml

- Using Docker-compose so you can edit and build your image in seconds:
```
sudo apt install docker-compose
```
- Build and run Docker image:
```
sudo docker-compose up
```
- After edit files with nano for example (nano start.sh):
```
sudo docker-compose build
sudo docker-compose up
```
or
```
sudo docker-compose up --build
```
- To stop docker run 
```
sudo docker ps
```
```
sudo docker stop id
```
- To clear the container (this will not effect on image):
```
sudo docker container prune
```
- To delete the image:
```
sudo docker image prune -a
```
</details>

## Getting Google OAuth API credential file
<details>
    <summary><b>Click here for more details</b></summary>

- Visit the [`Google Cloud Console`](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of Eunhabot, and rename it to **credentials.json**
- Visit [`Google API page`](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate **token.pickle** file for Google Drive:
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```
</details>

## Generate Database
<details>
    <summary><b>Click here for more details</b></summary>

**1. Using ElephantSQL**

- Go to [`ElephantSql`](https://elephantsql.com) and create account (**skip this if you already have ElephantSQL account**)
- Hit **`Create New Instance`**
- Follow the further instructions in the screen
- Hit **`Select Region`**
- Hit **`Review`**
- Hit **`Create instance`**
- Select your database name
- Copy your database url, and fill to **`DATABASE_URL`** in `config.env`

**2. Using Clever**

- Go to [`Clever`](https://www.clever-cloud.com) and create account by sign-up (**skip this if you already have**)
- Directly go to your [`console`](https://console.clever-cloud.com) (**Make sure use Desktop Version on your browser**)
- Click on **`Personal space`** and click button **`+ Create`** then choose **`an add-on`**
- Select `PostgresSQL` (**With logo elephant**)
- Choose **`PLAN NAME DEV`** just click on it and scroll down then click **`Next`**
- Select on **`Paris France`** and put the name of your database (**what ever you want**) then click **`Next`**
- On Addon dashboard go to `CONNECTION URI` copy and fill to **`DATABASE_URL`** in `config.env`

</details>

## Using Service Accounts for uploading to avoid user rate limit
<details>
    <summary><b>Click here for more details</b></summary>

For Service Account to work, you must set **USE_SERVICE_ACCOUNTS=**"True" in config file or environment variables, 
Many thanks to [`AutoRClone`](https://github.com/xyou365/AutoRclone) for the scripts.
**NOTE**: Using Service Accounts is only recommended while uploading to a Team Drive.
</details>

## Generate Service Accounts.
- [`What is Service Account`](https://cloud.google.com/iam/docs/service-accounts)
<details>
    <summary><b>Click here for more details</b></summary>

Let us create only the Service Accounts that we need. 
**Warning**: abuse of this feature is not the aim of this project and we do **NOT** recommend that you make a lot of projects, just one project and 100 SAs allow you plenty of use, its also possible that over abuse might get your projects banned by Google. 

**NOTE:** 1 Service Account can copy around 750gb a day, 1 project can make 100 Service Accounts so that's 75tb a day, for most users this should easily suffice.
```
python3 gen_sa_accounts.py --quick-setup 1 --new-only
```
A folder named accounts will be created which will contain keys for the Service Accounts.

Or you can create Service Accounts to current project, no need to create new one

- List your projects ids
```
python3 gen_sa_accounts.py --list-projects
```
- Enable services automatically by this command
```
python3 gen_sa_accounts.py --enable-services $PROJECTID
```
- Create Sevice Accounts to current project
```
python3 gen_sa_accounts.py --create-sas $PROJECTID
```
- Download Sevice Accounts as accounts folder
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```
If you want to add Service Accounts to Google Group, follow these steps

- Mount accounts folder
```
cd accounts
```
- Grab emails form all accounts to emails.txt file that would be created in accounts folder
```
grep -oPh '"client_email": "\K[^"]+' *.json > emails.txt
```
- Unmount acounts folder
```
cd -
```
Then add emails from emails.txt to Google Group, after that add Google Group to your Shared Drive and promote it to manager.

**NOTE**: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys project_id
```

</details>

## Add all the Service Accounts to the Team Drive
<details>
    <summary><b>Click here for more details</b></summary>

- Run:
```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```
</details>

# Youtube-dl authentication using .netrc file
<details>
    <summary><b>Click here for more details</b></summary>
    
For using your premium accounts in Youtube-dl or for protected Index Links, edit the netrc file according to following format:
```
machine host login username password my_youtube_password
```
For Index Link with only password without username, even http auth will not work, so this is the solution.
```
machine example.workers.dev password index_password
```

**NOTE**: Since this bot using yt-dlp. 
```
.netrc maybe not working at all, but if you using netrc you can notice some warning
say about using cookies option maybe since youtube have been slightly changed
```

Where host is the name of extractor (eg. Youtube, Twitch). Multiple accounts of different hosts can be added each separated by a new line.

</details>

# Uptime your apps
this function is to turn on your bot so it doesn't fall asleep.
<details>
    <summary><b>Click here for more details</b></summary>

choose one of these:

- [`Cron Job`](https://cron-job.org) Just put your app link
- [`Uptime Robot`](https://uptimerobot.com) Just put your app link
- [`Kaffeine`](https://kaffeine.herokuapp.com) Just put your app link
- [`PingDom`](https://pingdom.com) Just put your app link

</details>            

## Index-Repo
Recommended Index repo for [`eunhamirror`](https://github.com/vincreator/eunhamirror)
<details>
    <summary><b>Click here for more details</b></summary>

- [`Bhadoo Index`](https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index) by Parveen
- [`GDIndex`](https://github.com/maple3142/GDIndex) by maple3142
- [`goindex`](https://github.com/alx-xlx/goindex) by alx-xlx
- [`goIndex-theme-nexmoe`](https://github.com/5MayRain/goIndex-theme-nexmoe) by 5MayRain

**NOTE**: If you any problem with your Index, report the problem to dev Index repo which you use it.

</details>

# Credits

Thanks to:
<details>
    <summary><b>Click here for more details</b></summary>
    
- [`out386`](https://github.com/out386) heavily inspired from Telegram Bot which is written in JS
- [`Izzy12`](https://github.com/lzzy12/) for original repo
- [`jaskaranSM`](https://github.com/jaskaranSM) for build up this bot from scratch
- [`Dank-del`](https://github.com/Dank-del/) for base repo
- [`magneto261290`](https://github.com/magneto261290/) for some features
- [`SVR666`](https://github.com/SVR666/) for some features & fixes
- [`anasty17`](https://github.com/anasty17) for some features & help
- [`breakdowns`](https://github.com/breakdowns) for slam-aria-mirror-bot
- [`zevtyardt`](https://github.com/zevtyardt) for some direct links
- [`yash-dk`](https://github.com/yash-dk) for implementation qBittorrent on Python

</details>

And many more people who aren't mentioned here, but may be found in [`Contributors`](https://github.com/vincreator/eunha/graphs/contributors).
