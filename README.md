# Get Last Youtube Video
Small script to get title and link to the latest video of a youtube channel.

## Installation
This script uses the [google-api-python-client](https://github.com/googleapis/google-api-python-client).
```sh
virtualenv env
source env/bin/activate
pip install google-api-python-client
```

Create a file named `key.json` in the format:
```
{
  "key": string
}
```

The string is the API key created in the [Google developers dashboard](https://console.developers.google.com/) with the Youtube Data API.

Follow this guide to generate API key: https://developers.google.com/youtube/v3/getting-started.


## Usage
Open the script with an editor and customize the variable `CHID` with the id of the channel you wish (the id is usually found in the channel link).