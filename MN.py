import os
import subprocess
import sys
import pyfiglet  # Import pyfiglet for big font text generation

# Function to print colorful text
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Clear the screen
os.system('clear')

# Define color codes
RED = '31'
GREEN = '32'
YELLOW = '33'
BLUE = '34'
MAGENTA = '35'
CYAN = '36'
RESET = '0'

# Display company name in big font using pyfiglet
company_name = pyfiglet.figlet_format("MN CORPORATION")
print_colored(company_name, MAGENTA)

# Welcome message
print_colored("\nWelcome to the Ultimate Downloader!", CYAN)
print_colored("This tool allows you to download videos and audio from YouTube and Instagram.", YELLOW)

# Display options
print_colored("\nChoose an option:", GREEN)
print_colored("1. Download from YouTube", CYAN)
print_colored("2. Download from Instagram", YELLOW)
print_colored("3. Exit", RED)

# Get user input
choice = input("\nEnter your choice (1/2/3): ")

# Define function to download from YouTube in MP4
def download_youtube(url):
    print_colored("\nDownloading from YouTube...", CYAN)
    try:
        # Download the best video in MP4 format using yt-dlp
        subprocess.run(['yt-dlp', '-f', 'bestvideo+bestaudio/best', '--merge-output-format', 'mp4', url], check=True)
        print_colored("Download complete in MP4 format!", GREEN)
    except subprocess.CalledProcessError:
        print_colored("Error downloading YouTube video.", RED)

# Define function to download from Instagram
def download_instagram(url):
    print_colored("\nDownloading from Instagram...", CYAN)
    try:
        # Instagram posts (images/videos) are downloaded as .jpg or .mp4 by default using instaloader
        subprocess.run(['instaloader', '--video-mp4', '--dirname-pattern', './downloads', url], check=True)
        print_colored("Download complete in MP4 format!", GREEN)
    except subprocess.CalledProcessError:
        print_colored("Error downloading Instagram post.", RED)

# Execute based on user's choice
if choice == '1':
    url = input("\nEnter the YouTube video URL: ")
    download_youtube(url)
elif choice == '2':
    url = input("\nEnter the Instagram post URL: ")
    download_instagram(url)
elif choice == '3':
    print_colored("Exiting downloader. Goodbye!", RED)
    sys.exit(0)
else:
    print_colored("Invalid choice! Please try again.", YELLOW)
