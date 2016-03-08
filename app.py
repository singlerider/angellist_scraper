import sqlite3 as lite
from config import password, username, visitor_hash, extra_cookie

import requests
from bs4 import BeautifulSoup


def cleanup(data):
    cleaned_data = data
    pass
    return cleaned_data


def save_to_database(url):
    con = lite.connect('angellist.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applicants(
            id INTEGER PRIMARY KEY, first_name TEXT,
                email TEXT);
    """)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    cookie = {
        'visitor_hash': visitor_hash,
        "mp_6a8c8224f4f542ff59bd0e2312892d36_mixpanel": extra_cookie
    }
    resp = requests.get(url=url, auth=(username, password), headers=headers, cookies=cookie)
    data = resp.content
    print data
    soup = BeautifulSoup(data, "html.parser")
    texts = soup.findAll('a')#, class_="link_el")
    print "\n\n\n\n\n", texts
    return


def main():
    # url = "https://angel.co/candidates#job-listing-124102/o!all-candidates/f!%7B%22locations%22%3A%5B%22San%20Francisco%22%5D%2C%22roles%22%3A%5B%22Software%20Engineer%22%5D%2C%22looking_for%22%3A%5B%22full_time%22%5D%2C%22publicly_looking%22%3A%5B1%5D%2C%22us_authorized%22%3Atrue%2C%22last_active%22%3A%227%22%7D"
    url = "https://angel.co/resume/86282/6fe9397d7de60d7f378ee1385a8c78c9"
    save_to_database(url)

if __name__ == "__main__":
    main()
