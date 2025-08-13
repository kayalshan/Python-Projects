# Filename: download_youtube_playlist.py
"""
Case Study #2
-------------
Task: Download all videos from a given YouTube playlist.

This script:
1. Downloads all videos from a YouTube playlist using yt-dlp.
2. Generates an interactive HTML table (Bokeh) listing downloaded videos with clickable file paths.
"""

import os
import sys
import subprocess
import glob
from urllib.parse import quote

import pandas as pd
from bokeh.models import ColumnDataSource, DataTable, TableColumn, HTMLTemplateFormatter
from bokeh.plotting import output_file, save


def check_and_install_ytdlp():
    """Ensure yt-dlp is installed."""
    try:
        import yt_dlp
    except ImportError:
        print("Installing yt-dlp...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        import yt_dlp  # noqa


def download_playlist(playlist_url: str, output_dir: str = "downloads"):
    """
    Download all videos from a YouTube playlist.

    Args:
        playlist_url (str): The full playlist URL.
        output_dir (str): Directory to store downloaded videos.
    """
    check_and_install_ytdlp()
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(playlist_index)s - %(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "ignoreerrors": True
    }

    try:
        import yt_dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("\nDownload completed successfully.")
    except Exception as e:
        print(f"\nError downloading playlist: {e}")

    return output_dir


def generate_bokeh_table(output_dir: str, table_file: str = "downloaded_videos.html"):
    """
    Create an interactive Bokeh table for downloaded videos.

    Args:
        output_dir (str): Directory containing downloaded videos.
        table_file (str): Output HTML file for the table.
    """
    # List all video files in directory
    files = glob.glob(os.path.join(output_dir, "*.mp4"))
    if not files:
        print("No downloaded videos found.")
        return

    # Prepare DataFrame
    data = []
    for f in files:
        filename = os.path.basename(f)
        link = f"file:///{quote(os.path.abspath(f))}"
        data.append({"Video Name": filename, "Video Link": link})

    df = pd.DataFrame(data)

    # Create Bokeh table
    source = ColumnDataSource(df)
    link_template = '<a href="<%= value %>" target="_blank">Open</a>'
    columns = [
        TableColumn(field="Video Name", title="Video Name"),
        TableColumn(field="Video Link", title="Link", formatter=HTMLTemplateFormatter(template=link_template))
    ]
    data_table = DataTable(source=source, columns=columns, width=800, height=400, sortable=True)

    output_file(table_file)
    save(data_table)
    print(f"Interactive table saved to: {table_file}")


if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ").strip()
    download_dir = download_playlist(playlist_url)
    generate_bokeh_table(download_dir)


# if __name__ == "__main__":
#     # Replace this URL with your desired playlist
#     # PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD"
#     input_url = input("Enter the YouTube playlist URL: ").strip()
#     download_playlist(input_url)
# input_url
