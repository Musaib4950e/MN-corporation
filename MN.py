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

# Define function to download from YouTube in MP4 with quality options
def download_youtube(url):
    print_colored("\nSelect video quality:", GREEN)
    print_colored("1. 480p", CYAN)
    print_colored("2. 720p", CYAN)
    print_colored("3. 1080p", CYAN)

    # Get quality choice from user
    quality_choice = input("\nEnter your choice (1/2/3): ")

    # Determine format based on user selection
    if quality_choice == '1':
        format_choice = 'bestaudio[ext=m4a]+bestvideo[height<=480][ext=mp4]/best[height<=480]'
    elif quality_choice == '2':
        format_choice = 'bestaudio[ext=m4a]+bestvideo[height<=720][ext=mp4]/best[height<=720]'
    elif quality_choice == '3':
        format_choice = 'bestaudio[ext=m4a]+bestvideo[height<=1080][ext=mp4]/best[height<=1080]'
    else:
        print_colored("Invalid choice, defaulting to 720p.", YELLOW)
        format_choice = 'bestaudio[ext=m4a]+bestvideo[height<=720][ext=mp4]/best[height<=720]'

    # Set download path to /storage/emulated/0/Download
    download_path = "/storage/emulated/0/DCIM"

    print_colored(f"\nDownloading in {quality_choice}p quality to {download_path}...", CYAN)
    try:
        # Download the selected format and specify the output directory
        subprocess.run(['yt-dlp', '-f', format_choice, '--merge-output-format', 'mp4', '-o', f'{download_path}/%(title)s.%(ext)s', url], check=True)
        print_colored("Download complete in MP4 format!", GREEN)
    except subprocess.CalledProcessError:
        print_colored("Error downloading YouTube video.", RED)

# Define function to download from Instagram
# Define function to download from Instagram using yt-dlp
def download_instagram(url):
    print_colored("\nDownloading from Instagram...", CYAN)
    # Set download path
    download_path = "/storage/emulated/0/DCIM"
    try:
        # Use yt-dlp to download Instagram posts
        subprocess.run(['yt-dlp', '--output', f'{download_path}/%(title)s.%(ext)s', url], check=True)
        print_colored("Download complete!", GREEN)
    except subprocess.CalledProcessError:
        print_colored("Error downloading Instagram post.", RED)
