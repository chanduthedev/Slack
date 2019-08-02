This is to download files from slack using python.

# Prerequisites
- Python3
- requests

# How to show list of uploaded files in slack
This is wil show all the uploaded files in the slack. 

1. Clone this repo
2. cd Slack
3. Update token in slack_display_files.py file with your slack token
4. python3 slack_display_files.py 

# How to download files
This slack_download.py file will take two parameters for file extension and no.of Days respectively.
File extension: Need to specify the file exntension like jpg, png, mp4 etc  which you want to download
no.of Days: Downloading file which is these no.of days old and it should be an Integer. Follow belos steps for downloading files from slack.

1. Clone this repo (Skip this if already done)
2. cd Slack (Skip this if already done)
3. Update token in slack_download.py file with your slack token
4. python3 slack_download.py file_exntension no_of_days

Thanks  to @jackcarter who did deleting files from slack in python. Refered this link for reading files https://gist.github.com/jackcarter/d86808449f0d95060a40.

