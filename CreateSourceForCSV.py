# filename: CreateSourceForCSV.py
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from bokeh.models import ColumnDataSource, DataTable, TableColumn, HTMLTemplateFormatter
from bokeh.plotting import output_file, save


def fetch_page(url: str, html_file: str = "indian_leaders.html"):
    """Fetches the webpage content and saves it locally."""
    response = requests.get(url)
    response.raise_for_status()

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(response.text)

    return BeautifulSoup(response.text, "html.parser")


def extract_names_links(soup, csv_file: str = "indian_leaders.csv"):
    """Extracts names and hyperlinks from the soup and saves to CSV."""
    records = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        name = a_tag.get_text(strip=True)
        if href.startswith("/") and name:
            full_link = "https://www.thefamouspeople.com" + href
            records.append({"Name": name, "Hyperlink": full_link})

    if records:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Hyperlink"])
            writer.writeheader()
            writer.writerows(records)

    print(f"Saved {len(records)} records to {csv_file}")
    return records


def create_interactive_table(csv_file: str, output_html: str = "indian_leaders_table.html"):
    """Creates an interactive Bokeh table from CSV."""
    df = pd.read_csv(csv_file)

    # Create HTML clickable links
    df["LinkHTML"] = df["Hyperlink"].apply(lambda x: f'<a href="{x}" target="_blank">View Profile</a>')

    source = ColumnDataSource(df)

    columns = [
        TableColumn(field="Name", title="Leader Name"),
        TableColumn(field="LinkHTML", title="Profile Link", formatter=HTMLTemplateFormatter(template="<%= value %>"))
    ]

    data_table = DataTable(source=source, columns=columns, width=800, height=600, index_position=None)

    output_file(output_html)
    save(data_table)

    print(f"Interactive table saved to {output_html}")


if __name__ == "__main__":
    url = "https://www.thefamouspeople.com/indian-leaders.php"
    soup = fetch_page(url, "indian_leaders.html")
    extract_names_links(soup, "indian_leaders.csv")
    create_interactive_table("indian_leaders.csv", "indian_leaders_table.html")
