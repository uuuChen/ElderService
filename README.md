# ElderService
## Overview
We want to make an images generator for the elderly. There are several features of our project:
* Source of the images
  * High quality images from `unsplash.com `
  * Store the images in the database, so we don't need to keep sending requests to `unsplash.com`
* Content of the images
  * Automatically select suitable images according to festivals
  * Automatically adjust font color, size and position according to the image
  * Automatically adjust the text content according to the time and festival
* Notification
  * Send images to `line` with `line notify` at fixed times each day

## System Structure
* ![](https://i.imgur.com/3bzkkyp.jpg)

## Requirements
* conda

## Build
* `$ sh scripts/build_env.sh`
* Must add `.env` file under the root of the project, i.e.,  `ElderService/.env`, and it must have the following variables set: 
  1. `LINE_NOTIFY_TOKEN`: Get the token from `https://notify-bot.line.me/my/services/`
  2. `UNSPLASH_CLIENT_ID`: Get the client id from `https://unsplash.com/developers`

## Run
* `$ python3 elder_service/main.py`
