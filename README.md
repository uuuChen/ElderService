
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
  * Users can interact with line bot by sending english words, such as `love`, `flower`, ..., etc.

## System Structure

* ![System Structure](https://i.imgur.com/3bzkkyp.jpg)

## Requirements

* ngrox
* docker

## Build

* Must add `config.ini` file under the root of the project, i.e.,  `ElderService/config.ini`, and it must have the following variables set:

    ```=ini
    [line-bot]
    CHANNEL_ACCESS_TOKEN = { REPLACE_BY_YOUR_CHANNEL_ACCESS_TOKEN }
    CHANNEL_SECRET = { REPLACE_BY_YOUR_CHANNEL_SECRET }

    [unsplash]
    CLIENT_ID = { REPLACE_BY_YOUR_CLIENT_ID }
    ```

* `$ sh tools/build.sh`

## Run

* `$ docker run -d -p 5000:5000 lobster/elder-service`
* `$ ngrok http 5000`
* Edit line bot Webhook URL based on `Session Status [Forwarding-https]` of ngrok (for example: `https://e52f-1-161-177-196.ngrok.io/callback`, Note that `/callback` is needed)
  * ![Webhook URL](https://i.imgur.com/KSWvVbW.png)
* Send message to line bot
  * ![Example of sending message](https://i.imgur.com/jWtvOO1.png)
