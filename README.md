Python Projects-Tube2Bokeh
A Python-based case study project that combines web scraping, data visualization with Bokeh, and YouTube playlist downloading into one workflow.
Features

Web Scraping: Extract names and hyperlinks from a given webpage and store them in CSV format.
Data Visualization (Bokeh): Convert scraped data into an interactive HTML table.
YouTube Playlist Downloader: Download entire playlists using yt-dlp in the highest available quality.

Project Structure
Tube2Bokeh/
│
├── create_csv_from_html.py       # Scrapes data from webpage and saves to CSV
├── download_youtube_playlist.py  # Downloads full YouTube playlists
├── indian_leaders.html           # Example saved HTML page (scraped)
├── indian_leaders.csv            # CSV file generated from scraped HTML
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

Installation

Clone the Repository
git clone https://github.com/kayalshan/Tube2Bokeh.git
cd Tube2Bokeh


Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Install Dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt



Usage

Scraping Data & Generating Bokeh Table

Run:python create_csv_from_html.py


Prompts user for a URL
Saves HTML locally
Extracts Name and Hyperlink
Creates a CSV
Generates an interactive Bokeh HTML table


Downloading YouTube Playlist

Run:python download_youtube_playlist.py


Prompts for a YouTube playlist URL
Downloads all videos in highest quality into downloads/ folder



Example Workflow

Run Web Scraper → Generates CSV and interactive HTML table
Use CSV Data → For reports, analysis, or embedding into web pages
Run Playlist Downloader → Store offline learning resources

Requirements
See requirements.txt for exact versions. Key libraries:

requests – HTTP requests
beautifulsoup4 – HTML parsing
pandas – CSV handling
bokeh – Interactive visualization
yt-dlp – YouTube downloads

License
This project is licensed under the MIT License.

Author
Developed by Kayalvizhi Shanmugam
