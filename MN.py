import yt_dlp
import os

def download_video(url, output_dir="/storage/emulated/0/Download"):
    """
    Downloads a video from YouTube or Instagram using yt-dlp.

    Args:
        url (str): The URL of the video.
        output_dir (str): Directory to save the downloaded video.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set options for yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',  # Merge audio and video into mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading from: {url}")
            ydl.download([url])
            print(f"Download complete! Saved in {output_dir}")
        except Exception as e:
            print(f"Error downloading video: {e}")

def is_instagram_url(url):
    """
    Check if the URL is an Instagram URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is from Instagram, False otherwise.
    """
    return 'instagram.com' in url

def main():
    print("=== Video Downloader (YouTube & Instagram) ===")
    url = input("Enter the URL of the video: ").strip()

    # Set the default output directory to Android storage
    output_dir = "/storage/emulated/0/Download"

    # Check if the URL is an Instagram link
    if is_instagram_url(url):
        print("Detected Instagram URL.")
        download_video(url, output_dir)
    elif 'youtube.com' in url or 'youtu.be' in url:
        print("Detected YouTube URL.")
        download_video(url, output_dir)
    else:
        print("Unsupported URL. Please enter a valid YouTube or Instagram link.")

if __name__ == "__main__":
    main()
