# ElderService
## Overview
We want to make an images generator for the elderly. There are several features of our project:
* Source of the images
  * High quality images from `unsplash.com `
  * Store the images in the database, so we don't need to keep sending requests to `unsplash.com` (For Free: 50 requests / hour)
* Content of the images
  * Automatically select suitable images according to festivals
  * Automatically adjust font color, size and position according to the image
  * Automatically adjust the text content according to the time and festival
* Line Bot
  * Send images to `line` with `line notify` at fixed times each day

## System Structure
* ![](https://i.imgur.com/3bzkkyp.jpg)

## Requirements
* conda

## Build
* `$ sh scripts/build_env.sh`
* Must add `config.ini` file under the root of the project, i.e.,  `ElderService/config.ini`, and it must have the following variables set:
    ```
    [line-bot]
    CHANNEL_ACCESS_TOKEN = { REPLACE_BY_YOUR_CHANNEL_ACCESS_TOKEN }
    CHANNEL_SECRET = { REPLACE_BY_YOUR_CHANNEL_SECRET }

    [unsplash]
    CLIENT_ID = { REPLACE_BY_YOUR_CLIENT_ID }
    ```

## Run
* `$ python3 elder_service/main.py`
