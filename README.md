# Web Scraping for Jakarta Regulations

This Python script is designed to scrape information from the Jakarta Legal Information Center (JDIH) website to gather data on regulations and legislative documents. It utilizes the `requests` library to make HTTP requests, `BeautifulSoup` (bs4) for parsing HTML, and `csv` for data storage.

## Prerequisites

Before running the script, ensure that you have the necessary Python libraries installed:

- [requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup4 (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [csv](https://docs.python.org/3/library/csv.html)

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Set the constants in the code, such as `BASE_URL`, `TIMEOUT`, and `HEADERS`, to match your requirements.

2. Run the script by executing `python your_script_name.py`.

3. The script will scrape data from multiple pages on the JDIH website, gather information about various regulations, and store the data in a CSV file named `data_jdih_jakarta.csv`.

## Code Structure

- `extract_text(element)`: A function that extracts and cleans text from an HTML element.

- `fetch_peraturan_data(session, peraturan_url)`: A function that scrapes data for a specific regulation document.

- `main()`: The main function that manages the scraping process. It iterates through multiple pages, collects data for each regulation, and writes the information to a CSV file.

## License

This code is provided under the [MIT License](LICENSE).

Please note that web scraping may be subject to website terms of service and legal regulations. Always make sure you have the appropriate permissions to scrape data from a website.

 
