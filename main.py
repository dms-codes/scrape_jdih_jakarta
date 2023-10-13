import requests
from bs4 import BeautifulSoup as bs
import csv

# Constants
BASE_URL = "https://jdih.jakarta.go.id/dokumen/peraturan-perundang-undangan?page="
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    return element.text.strip() if element else ''

def fetch_peraturan_data(session, peraturan_url):
    html = session.get(peraturan_url, timeout=TIMEOUT, headers=HEADERS).content
    soup = bs(html, 'html.parser')
    peraturan_data = {
        'Tipe Dokumen': extract_text(soup.find('div', class_='flex').find('p')),
        'Judul Peraturan': '',
        'URL': peraturan_url,
        'T.E.U Badan': '',
        'Nomor Peraturan': '',
        'Jenis Peraturan': '',
        'Singkatan Jenis': '',
        'Tempat Penetapan': '',
        'Tanggal Penetapan': '',
        'Tanggal Pengundangan': '',
        'Sumber': '',
        'Subjek': '',
        'Bidang Hukum': '',
        'Urusan Pemerintahan': '',
        'Pemrakarsa': '',
        'Penandatangan': '',
        'Bahasa': '',
        'Status Peraturan': '',
        'Keterangan Status': '',
        'Tag': '',
        'Full Text URL': ''
    }
    l = []
    for data in soup.find_all('div', class_='w-3/5'):
        l.append(extract_text(data.find('div', class_='flex').find('p')))
    peraturan_data.update(zip(peraturan_data,l))

    try:
        peraturan_data['Full Text URL'] = soup.find('div', class_='lamps').find('a', href=True)['href']
    except:pass
    return peraturan_data

def main():
    session = requests.Session()
    with open('data_jdih_jakarta.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Tipe Dokumen', 'Judul Peraturan', 'URL', 'T.E.U Badan', 'Nomor Peraturan', 'Jenis Peraturan', 'Singkatan Jenis',
                      'Tempat Penetapan', 'Tanggal Penetapan', 'Tanggal Pengundangan', 'Sumber',
                      'Subjek', 'Bidang Hukum', 'Urusan Pemerintahan', 'Pemrakarsa', 'Penandatangan', 'Bahasa',
                      'Status Peraturan', 'Keterangan Status', 'Tag', 'Full Text URL']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, 238):
            url = f"{BASE_URL}{i}"
            html = session.get(url, timeout=TIMEOUT, headers=HEADERS).content
            soup = bs(html, 'html.parser')
            for peraturan in soup.find_all('div', class_='data-dokumen w-full'):
                peraturan_url = peraturan.find('a', href=True)['href']
                print(i, url, peraturan_url)
                peraturan_data = fetch_peraturan_data(session, peraturan_url)
                writer.writerow(peraturan_data)
                f.flush()

if __name__ == '__main__':
    main()
