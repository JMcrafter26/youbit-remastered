# if script is running for the first time, then show a message to install youbit

import os

# check if it is running for the first time, by checking the temp folder for a file called "youbit"
if not os.path.exists(os.path.expanduser("~") + "/.youbit"):
    print("\033[91m" + "IMPORTANT: youbit must be installed! Please go to " + '\033[0m' + "\033[94m" + "https://github.com/MeViMo/youbit" + '\033[0m' + "\033[91m" + " for instructions on how to install it." + '\033[0m')
    # user has to press enter to continue
    input("Press Enter to continue...")
    # clear the screen
    print("\033c")
    # create a file called "youbit" in the temp folder
    open(os.path.expanduser("~") + "/.youbit", "w+")
from youbit import decode_local, Metadata

video_id = input("Enter the youtube video id to download: ")
# video_id = "dnhlx48t-h4"
while len(video_id) < 5:
    video_id = input("\033[91m" + "Enter the youtube video id to download: " + '\033[0m')

# get the json from https://iv.ggtyler.dev/api/v1/videos/[vide_id]?fields=title,description,formatStreams
# and parse it to get the title, description and formatStreams

url = "https://iv.ggtyler.dev/api/v1/videos/" + video_id + "?fields=title,description,formatStreams,adaptiveFormats"
import requests
import json

response = requests.get(url)
data = json.loads(response.text)

title = data['title']
description = data['description']
adaptiveFormat = data['adaptiveFormats']

# print the title
print('\033[92m' + "Downloading: " + title + '\033[0m')

itag_to_download = 137  # Specify the `itag` value you want to download
download_url = None

# Find the adaptive format with the specified `itag`
for fmt in adaptiveFormat:
    if 'itag' in fmt and fmt['itag'] == str(itag_to_download):
        download_url = fmt['url']
        break


# get the url from the formatStream
# download_url = formatStream['url']
print(download_url)


# print("\033c")

# download the video to the temp folder and while downloading, show the progress
import urllib.request


temp_folder = os.path.expanduser("~\\youbit\\temp\\")

# Check if the parent directory exists, and create it if it doesn't
parent_folder = os.path.dirname(temp_folder)
if parent_folder and not os.path.exists(parent_folder):
    os.makedirs(parent_folder)

# Check if the temp folder exists or is not a directory, and create it if needed
if not os.path.exists(temp_folder) or not os.path.isdir(temp_folder):
    os.makedirs(temp_folder)

print("\033c")


# before downloading the file, check if the file already exists in the temp folder
if os.path.exists(temp_folder + video_id + ".mp4"):
    print('\033[92m' + "The video is already downloaded! Continuing with the next step..." + '\033[0m')
else:
    # example url https://rr3---sn-t0a7lnee.googlevideo.com/videoplayback?expire=1685846516&ei=lKV7ZPzdIsyU_9EP9ZCJwAQ&ip=167.114.211.189&id=o-AERBqFDDxlmxaytYa_VOp8ZeTGWr5NdoY45gXJq1e6wY&itag=22&source=youtube&requiressl=yes&mh=ca&mm=31%2C29&mn=sn-t0a7lnee%2Csn-t0a7sn7d&ms=au%2Crdu&mv=m&mvi=3&pl=23&pcm2=yes&initcwndbps=216250&spc=qEK7Bw_s1p-FxMkTucw9g4dg-FNV-sg&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=22.058&lmt=1657030008993876&mt=1685824601&fvip=4&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=5318224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgfPqbeX70YHAgPSNOtGyBk3LXw-RoGXbWpnzVGkKmPZQCIQCl7iS5KLmE0H3rLr1s_AkFqzI40C2FWDapOkOuhh15Sg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPp_KaPLc_W7MZVoeUEAup5UEbFfaOZCpGKuIoQwJpHnAiAt_CLDsrLvmsjMA2xO_EFepST_M2vAUjhDt4eol1PMkA%3D%3D&host=rr3---sn-t0a7lnee.googlevideo.com
    # download the file to the temp folder
    urllib.request.urlretrieve(download_url, temp_folder + video_id + ".mp4", reporthook=lambda blocknum, blocksize, totalsize: 
                               # print a progress bar like this: [=====>    50%]
                               print('\033[92m' + "Downloading " + title + " (" + video_id + ")" + '\033[0m' + "\n" + "\r" + '\033[92m' + '\033[0m' + '\033[93m' + "[" + "=" * int(blocknum * blocksize * 100 / totalsize / 2) + ">" + " " * (50 - int(blocknum * blocksize * 100 / totalsize / 2)) + "]" + str(int(blocknum * blocksize * 100 / totalsize)) + "%" + '\033[0m' + '\033[92m' + " ( " + str(int(blocknum * blocksize / 1024 / 1024)) + " MB / " + str(int(totalsize / 1024 / 1024)) + " MB )" + "\r" + '\033[F' + '\033[F'), data=None)

print("\033c")


# check if the file was downloaded successfully
if not os.path.exists(temp_folder + video_id + ".mp4"):
    print("\033[91m" + "Error downloading the file! Exiting..." + '\033[0m')
    # exit the program with exit code 1
    exit(1)
    # else, if the file was downloaded successfully, then print a success message
else:
    print("\033[92m" + "Downloaded successfully to " + temp_folder + video_id + ".mp4" + '\033[0m')



# set meta to the video description
meta = description
print(meta + "\n")


# set filename to the video id
filename = video_id + ".mp4"
print(filename + "\n")

# get users desktop path
desktop = os.path.expanduser("~\\Desktop\\")

# if the length of the input is less than 10, then prompt the user to enter a valid input
while len(meta) < 15:
    meta = input("\033[91m" + "Something went wrong! Please enter the metadata (strange string in the yt video description): " + '\033[0m')

# clear the screen
# print("\033c")

metadata = Metadata.create_from_base64(description)

# if the metadata is invalid, then exit the program
if metadata is None:
    print("\033[91m" + "Invalid metadata! Exiting..." + '\033[0m')
    # exit the program with exit code 1
    exit(1)

export = decode_local(temp_folder + filename, desktop, metadata)

# save the file to the same directory as the original file

# Print the path to the file in green
print('\033[92m' + "File saved to: " + desktop + '\033[0m')

# exit the program
exit()