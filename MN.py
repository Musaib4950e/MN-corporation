import yt_dlp
import pyfiglet
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def download_video(url, resolution):
    # Select the best video and audio quality based on user choice
    formats = {
        '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    }

    if resolution in formats:
        selected_format = formats[resolution]
    else:
        print(f"{Fore.RED}Resolution {resolution} is not available. Defaulting to best quality.")
        selected_format = 'bestvideo+bestaudio/best'

    ydl_opts = {
        'format': selected_format,  # Ensure best video and audio are downloaded
        'outtmpl': '/storage/emulated/0/Download/%(title)s.%(ext)s',  # Save to Download folder
        'merge_output_format': 'mp4',  # Ensure the output format is MP4
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Use FFmpeg to merge audio and video
            'preferedformat': 'mp4',  # Convert to MP4 format
        }],
        'noplaylist': True,  # Avoid downloading entire playlists
        'quiet': False,  # Show detailed progress
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{Fore.GREEN}Downloading video at {resolution}...")
            ydl.download([url])
            print(f"{Fore.YELLOW}Download completed! File saved to Downloads.")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

def main():
    # ASCII Art and Welcome Message
    ascii_logo = pyfiglet.figlet_format("MN CORPORATION", font="slant")
    print(Fore.CYAN + ascii_logo)
    print(f"{Fore.CYAN}{'='*40}")
    print(f"{Fore.CYAN}Welcome to MN CORPORATION YouTube Downloader!")
    print(f"{Fore.CYAN}Developed by MN CORPORATION - The Best Download Experience")
    print(f"{Fore.CYAN}{'='*40}")

    # User Input for URL and Resolution
    video_url = input(f"{Fore.YELLOW}Enter the YouTube video URL: ")

    print(f"{Fore.MAGENTA}Choose the video quality:")
    print(f"{Fore.MAGENTA}1. 480p")
    print(f"{Fore.MAGENTA}2. 720p")
    print(f"{Fore.MAGENTA}3. 1080p")

    choice = input(f"{Fore.CYAN}Enter the number corresponding to the quality you want (1/2/3): ")

    if choice == '1':
        resolution = '480p'
    elif choice == '2':
        resolution = '720p'
    elif choice == '3':
        resolution = '1080p'
    else:
        print(f"{Fore.RED}Invalid choice. Defaulting to 720p.")
        resolution = '720p'

    # Call download function
    download_video(video_url, resolution)

if __name__ == "__main__":
    main()
