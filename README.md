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

**Eunha Mirror** is a _multipurpose_ Telegram Bot writen in Python for mirroring files on the Internet to our beloved Google Drive.

# Features supported:
<details>
    <summary><b>Click Here For More Details</b></summary>

## Additional Features
<details>
    <summary><b>Click here for more details</b></summary>

- Updater (**NOTE**: You must upload your **token.pickle** to Index and fill your **token.pickle** url to **TOKEN_PICKLE_URL**, because your **token.pickle** will deleted after update)
- Limiting size Torrent/Direct, Tar/Unzip, Mega, cloning Google Drive support
- Get detailed info about replied media (Only for Telegram file)
- Stop duplicate cloning Google Drive & mirroring Mega support
- Tar/Unzip Google Drive link support
- Speedtest with picture results
- Sudo with Database support
- Multiple Trackers support
- Check Heroku dynos stats
- Updater (Only for Heroku)
- Extracting **tar.xz** support
- Create Tar Google Drive folder
- Custom image support
- Custom Progress bar
- Counting file/folder
- Shell and Executor
- View Link button
- Shell and Executor
- Qbittorrent supported
- Torrent search Supported:
```
nyaa.si, sukebei, 1337x, piratebay,
tgx, yts, eztv, torlock, rarbg
```
- Direct links Supported:
```
letsupload.io, hxfile.co, anonfiles.com, bayfiles.com, antfiles,
fembed.com, fembed.net, femax20.com, layarkacaxxi.icu, fcdn.stream,
sbplay.org, naniplay.com, naniplay.nanime.in, naniplay.nanime.biz, sbembed.com,
streamtape.com, streamsb.net, feurl.com, pixeldrain.com, racaty.net,
1fichier.com, solidfiles.com, 1drv.ms (Only works for file not folder or business account),
uptobox.com (Uptobox account must be premium)
```
</details>

## From Original Repos
<details>
    <summary><b>Click here for more details</b></summary>

- Mirroring direct download links, Torrent, and Telegram files to Google Drive
- Mirroring Mega.nz links to Google Drive (If your Mega account not premium, it will limit 4-5gb/day)
- Copy files from someone's Drive to your Drive (Using Autorclone)
- Download/Upload progress, Speeds and ETAs
- Mirror all Youtube-dl supported links
- Docker support
- Uploading to Team Drive
- Index Link support
- Service Account support
- Delete files from Drive
- Shortener support
- Custom Filename (Only for URL, Telegram files and Youtube-dl. Not for Mega links and Magnet/Torrents)
- Extracting password protected files, using custom filename and download from password protected Index Links see these examples:
<p><a href="https://telegra.ph/Magneto-Python-Aria---Custom-Filename-Examples-01-20"> <img src="https://img.shields.io/badge/see%20on%20telegraph-grey?style=for-the-badge" width="190""/></a></p>

- Extract these filetypes and uploads to Google Drive
```
ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, 
APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, 
HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, 
NTFS, RPM, SquashFS, UDF, VHD, XAR, Z.
```
</details>
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
Install Docker by following the [official Docker docs](https://docs.docker.com/engine/install/debian/)

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

## Generate Database

**1. Using ElephantSQL**
<details>
    <summary><b>Click here for more details</b></summary>

- Go to https://elephantsql.com/ and create account (skip this if you already have ElephantSQL account)
- Hit **Create New Instance**
- Follow the further instructions in the screen
- Hit **Select Region**
- Hit **Review**
- Hit **Create instance**
- Select your database name
- Copy your database url, and fill to **DATABASE_URL** in config

</details>

**2. Using Heroku PostgreSQL**
<p><a href="https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1"> <img src="https://img.shields.io/badge/see%20on%20dev.to-black?style=for-the-badge&logo=dev-dot-to" width="190""/></a></p>

**NOTE**: If you deploying on Heroku using Heroku button, no need to generate database manually, because it will automatic generate database when first deploying

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
- **BOT_TOKEN**: The Telegram bot token that you get from [@BotFather](https://t.me/BotFather)
- **TELEGRAM_API**: This is to authenticate to your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org DO NOT put this in quotes.
- **TELEGRAM_HASH**: This is to authenticate to your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org
- **OWNER_ID**: The Telegram user ID (not username) of the Owner of the bot
- **GDRIVE_FOLDER_ID**: This is the folder ID of the Google Drive Folder to which you want to upload all the mirrors.
- **DOWNLOAD_DIR**: The path to the local folder where the downloads should be downloaded to
- **DOWNLOAD_STATUS_UPDATE_INTERVAL**: A short interval of time in seconds after which the Mirror progress message is updated. (I recommend to keep it `5` seconds at least)  
- **AUTO_DELETE_MESSAGE_DURATION**: Interval of time (in seconds), after which the bot deletes it's message (and command message) which is expected to be viewed instantly. (**Note**: Set to `-1` to never automatically delete messages)
### Optional Field
- **ACCOUNTS_ZIP_URL**: Only if you want to load your Service Account externally from an Index Link. Archive your Service Account json files to a zip file directly (don't archive the accounts folder. Select all the jsons inside and zip them only instead. Name the zip file with whatever you want, it doesn't matter). Fill this with the direct link of that file.
- **TOKEN_PICKLE_URL**: Only if you want to load your **token.pickle** externally from an Index Link. Fill this with the direct link of that file.
- **DATABASE_URL**: Your Database URL. See [Generate Database](https://github.com/vincreator/eunhamirror/tree/master#generate-database) to generate database (**NOTE**: If you use database you can save your sudo id permanent using `/addsudo` command).
- **AUTHORIZED_CHATS**: Fill user_id and chat_id (not username) of you want to authorize, Seprate them with space, Examples: `-0123456789 -1122334455 6915401739`.
- **SUDO_USERS**: Fill user_id (not username) of you want to sudoers, Seprate them with space, Examples: `0123456789 1122334455 6915401739` (**NOTE**: If you want save sudo id permanent without database, you must fill your sudo id there).
- **IS_TEAM_DRIVE**: Set to `True` if `GDRIVE_FOLDER_ID` is from a Team Drive else `False` or Leave it empty.
- **USE_SERVICE_ACCOUNTS**: (Leave empty if unsure) Whether to use Service Accounts or not. For this to work see [Using Service Accounts](https://github.com/vincreator/eunhamirror#generate-service-accounts-what-is-service-account) section below.
- **INDEX_URL**: Refer to https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index The URL should not have any trailing '/'
- **MEGA_API_KEY**: Mega.nz api key to mirror mega.nz links. Get it from [Mega SDK Page](https://mega.nz/sdk)
- **MEGA_EMAIL_ID**: Your email id you used to sign up on mega.nz for using premium accounts (Leave th)
- **MEGA_PASSWORD**: Your password for your mega.nz account
- **BLOCK_MEGA_FOLDER**: If you want to remove mega.nz folder support, set it to `True`.
- **BLOCK_MEGA_LINKS**: If you want to remove mega.nz mirror support, set it to `True`.
- **STOP_DUPLICATE**: (Leave empty if unsure) if this field is set to `True`, bot will check file in Drive, if it is present in Drive, downloading or cloning will be stopped. (**Note**: File will be checked using filename, not using filehash, so this feature is not perfect yet)
- **CLONE_LIMIT**: To limit cloning Google Drive (leave space between number and unit, Available units is (gb or GB, tb or TB), Examples: `100 gb, 100 GB, 10 tb, 10 TB`
- **MEGA_LIMIT**: To limit downloading Mega (leave space between number and unit, Available units is (gb or GB, tb or TB), Examples: `100 gb, 100 GB, 10 tb, 10 TB`
- **TORRENT_DIRECT_LIMIT**: To limit the Torrent/Direct mirror size, Leave space between number and unit. Available units is (gb or GB, tb or TB), Examples: `100 gb, 100 GB, 10 tb, 10 TB`
- **TAR_UNZIP_LIMIT**: To limit mirroring as Tar or unzipmirror. Available units is (gb or GB, tb or TB), Examples: `100 gb, 100 GB, 10 tb, 10 TB`
- **VIEW_LINK**: View Link button to open file Index Link in browser instead of direct download link, you can figure out if it's compatible with your Index code or not, open any video from you Index and check if the END of link from browser link bar is `?a=view`, if yes make it `True` it will work (Compatible with [Bhadoo Index](https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index) Code)
- **UPTOBOX_TOKEN**: Uptobox token to mirror uptobox links. Get it from [Uptobox Premium Account](https://uptobox.com/my_account).
- **HEROKU_EMAIL**: Heroku Account email Id in which the above app will be deployed (**NOTE**: Only needed if you deploying on Heroku with Github Workflow).
- **HEROKU_API_KEY**: (Only if you deploying on Heroku) Your Heroku API key, get it from https://dashboard.heroku.com/account.
- **HEROKU_APP_NAME**: (Only if you deploying on Heroku) Your Heroku app name.
- **IGNORE_PENDING_REQUESTS**: If you want the bot to ignore pending requests after it restarts, set this to `True`.
- **STATUS_LIMIT**: Status limit with buttons (**NOTE**: Recommend limit status to `4` tasks max).
- **IS_VPS**: (Only for VPS) Don't set this to `True` even if you are using vps, unless facing error with web server. Also go to start.sh and replace `$PORT` by `80` or any port you want to use.
- **SERVER_PORT**: (Only if IS_VPS is `True`) Base URL Port
- **BASE_URL_OF_BOT**: (Required for Heroku) Valid BASE URL of where the bot is deploy. Ip/domain of your bot like `http://myip` or if you have chosen other port then `80` then `http://myip:port`, for Heroku fill `https://yourappname.herokuapp.com` (**NOTE**: No slash at the end)
- **SHORTENER_API**: Fill your Shortener api key if you are using Shortener.
- **SHORTENER**: if you want to use Shortener in Gdrive and index link, fill Shortener url here. Examples:
```
exe.io, gplinks.in, shrinkme.io, urlshortx.com, shortzon.com
```

Above are the supported url Shorteners. Except these only some url Shorteners are supported.

**Note**: You can limit maximum concurrent downloads by changing the value of **MAX_CONCURRENT_DOWNLOADS** in aria.sh. By default, it's set to `7`.
### Add more buttons (Optional Field)
Three buttons are already added of Drive Link, Index Link, and View Link, you can add extra buttons, these are optional, if you don't know what are below entries, simply leave them, don't fill anything in them.
- **BUTTON_FOUR_NAME**:
- **BUTTON_FOUR_URL**:
- **BUTTON_FIVE_NAME**:
- **BUTTON_FIVE_URL**:
- **BUTTON_SIX_NAME**:
- **BUTTON_SIX_URL**:

</details>

## Getting Google OAuth API credential file
<details>
    <summary><b>Click here for more details</b></summary>

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of Eunhabot, and rename it to **credentials.json**
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate **token.pickle** file for Google Drive:
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```
</details>

## Deploying
<details>
    <summary><b>Click here for more details</b></summary>

- Start Docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
docker build . --rm --force-rm --compress --no-cache=true --pull --file Dockerfile -t mirrorbot
```
- Run the image:
```
sudo docker run mirrorbot
```
</details>

## Deploying on Heroku with Github Workflows.
<details>
    <summary><b>Click here for more details</b></summary>
    
## Pre-requisites

- [token.pickle](https://github.com/vincreator/eunhamirror#getting-google-oauth-api-credential-file)
- [Heroku](heroku.com) accounts
- Recommended to use 1 App in 1 Heroku account
- Don't use bin/fake credits card, because your Heroku account will get banned.

## Deployment

1. Give a star and Fork this repo then upload **token.pickle** to your forks, or you can upload your **token.pickle** to your Index and put your **token.pickle** link to `TOKEN_PICKLE_URL` (**NOTE**: If you don't upload **token.pickle** uploading will not work).

2. Go to Repository `Settings` -> `Secrets`

	![secrets](https://telegra.ph/file/bb8cb0eced5caad68a41b.jpg)

3. Add the below Required Variables one by one by clicking `New Repository Secret` everytime.

	* `HEROKU_EMAIL` Heroku Account Email Id in which the above app will be deployed
	* `HEROKU_API_KEY` Your Heroku API key, get it from https://dashboard.heroku.com/account
	* `HEROKU_APP_NAME` Your Heroku app name, Name Must be unique
	* `CONFIG_FILE_URL` Fill [This](https://raw.githubusercontent.com/vincreator/eunhamirror/master/config_sample.env) in any text editor. Remove the `_____REMOVE_THIS_LINE_____=True` line and fill the variables. Go to https://gist.github.com and paste your config data. Rename the file to `config.env` then create secret gist. Click on Raw, copy the link. This will be your `CONFIG_FILE_URL`. Refer to below images for clarity. 

	![steps 1 to 3](https://telegra.ph/file/1d8fec16516a87ba9d1ac.jpg)

	![step 4](https://telegra.ph/file/1491f99836cd694ea1195.jpg)

	![step 5](https://telegra.ph/file/416a550f7ded579b63272.jpg)

- **NOTE**: Remove commit id from raw link to be able to change variables without updating the `CONFIG_FILE_URL` in secrets.
  should be in this form: https://gist.githubusercontent.com/username/gist-id/raw/config.env
  - Before: https://gist.githubusercontent.com/anasty17/8cce4a4b4e7f4ea47e948b2d058e52ac/raw/19ba5ab5eb43016422193319f28bc3c7dfb60f25/config.env
  - After: https://gist.githubusercontent.com/anasty17/8cce4a4b4e7f4ea47e948b2d058e52ac/raw/config.env

  - You only need to restart your bot after editing `config.env` gist secret.

4. After adding all the above Required Variables go to Github Actions tab in your repo

5. Select `Manually Deploy to Heroku` workflow as shown below:

	![Example Manually Deploy to Heroku](https://telegra.ph/file/38ffda0165d9671f1d5dc.jpg)

6. Then click on Run workflow

	![Run workflow](https://telegra.ph/file/c5b4c2e02f585cb59fe5c.jpg)

7. _Done!_ your bot will be deployed now.

## NOTE
- Don't change/edit variables from Heroku if you want to change/edit do it from `config.env`

## Credits
- [arghyac35](https://github.com/arghyac35) for Tutorial
- [AkhileshNS](https://github.com/AkhileshNS) for Github workflow method to deploy Heroku app

</details>

## Deploy on Heroku with heroku-cli
<details>
    <summary><b>Click here for more details</b></summary>

- Install [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- Login into your heroku account with command:
```
heroku login
```
- Create a new heroku app:
```
heroku create appname
```
- Select This App in your Heroku-cli: 
```
heroku git:remote -a appname
```
- Change Dyno Stack to a Docker Container:
```
heroku stack:set container -a appname
```
- Clone this repo:
```
git clone https://github.com/vincreator/eunhamirror
ls
cd eunha
```
- get token [Read here](https://github.com/vincreator/eunhamirror#getting-google-oauth-api-credential-file)
- get sa token (opsional) [Read here](https://github.com/vincreator/eunhamirror#generate-service-accounts)
- Init the repo clone
```
git init
```
- Add all stuff:
```
git add .
git add * -f
git add .gitignore
```
- Commit new changes:
```
git commit -m "EunhaMirror Updates"
```
- Push Code to Heroku:
```
git push heroku master
```
- Restart Worker by these commands or you can Do it manually too in heroku.
- For Turning off the Bot:
```
heroku ps:scale web=0 -a appname
```
- For Turning on the Bot:
```
heroku ps:scale web=1 -a appname
```
- **Note**:
- Deploy 2 Times to unsuspend (Delete your apps and make it new with same name)
- Don't add config on heroku, Use `config.env`

</details>

# Using Service Accounts for uploading to avoid user rate limit
<details>
    <summary><b>Click here for more details</b></summary>

For Service Account to work, you must set **USE_SERVICE_ACCOUNTS=**"True" in config file or environment variables, 
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) for the scripts.
**NOTE**: Using Service Accounts is only recommended while uploading to a Team Drive.
</details>

## Generate Service Accounts. [What is Service Account](https://cloud.google.com/iam/docs/service-accounts)
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
Where host is the name of extractor (eg. Youtube, Twitch). Multiple accounts of different hosts can be added each separated by a new line.

</details>

# Uptime your apps
this function is to turn on your bot so it doesn't fall asleep.
<details>
    <summary><b>Click here for more details</b></summary>

choose one of these:

- [Cron Job](https://cron-job.org) Just put your app link
- [Uptime Robot](https://uptimerobot.com) Just put your app link
- [Kaffeine](https://kaffeine.herokuapp.com) Just put your app link
- [PingDom](https://pingdom.com) Just put your app link
- [AddOn Newrelic](https://elements.heroku.com/addons/newrelic)
- [AddOn Scheduler](https://elements.heroku.com/addons/scheduler)

</details>            
            
# Credits

Thanks to:
<details>
    <summary><b>Click here for more details</b></summary>
    
- [out386](https://github.com/out386) heavily inspired from Telegram Bot which is written in JS
- [Izzy12](https://github.com/lzzy12/) for original repo
- [Dank-del](https://github.com/Dank-del/) for base repo
- [magneto261290](https://github.com/magneto261290/) for some features
- [SVR666](https://github.com/SVR666/) for some features & fixes
- [anasty17](https://github.com/anasty17) for some features & help
- [breakdowns](https://github.com/breakdowns) for slam-aria-mirror-bot
- [zevtyardt](https://github.com/zevtyardt) for some direct links

</details>

And many more people who aren't mentioned here, but may be found in [Contributors](https://github.com/vincreator/eunha/graphs/contributors).
