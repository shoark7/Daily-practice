"""Fetch web page data and get word frequency in csv format

    This file uses lxml, urllib instead of BeautifulSoup, requests.
    It's better when we think they are built-in modules.
    Also, original file uses konlpy for fetch noun words only,
    but this module uses JDK, etc, not available for me now.

    So I just use str.split to split by whitespaces.
    And for command line usage, argparse module is used.

    Start date: 2017/11/27
    End date  : 2017/11/27
"""
import argparse
import csv
import sys
from collections import Counter
from lxml import html
from urllib.request import urlopen
# from konlp.tag import Twitter


def fetch(url, xpath):
    res = urlopen(url).read().decode('utf-8')
    page = html.fromstring(res)
    return '\n'.join(page.xpath(xpath))


def extract_words(text, max_n=500, min_freq=2):
    # analyzer = Twitter()
    # nouns = [ n for n in analyzer.nouns(text) if len(n) > 2]
    nouns = text.split()
    count = Counter(nouns)

    return [
        {'word': n, 'freq': freq}
        for n, freq in count.most_common(max_n)
        if freq > min_freq
    ]


def to_csv(stream, objs):
    w = csv.DictWriter(stream, objs[0].keys())
    # csv.DictWriter's first argument is 'f'. And the fact that name of the argument here is
    # 'stream' is remarkable. By this way, code became more scalable because
    # stream can be piped into a file.
    w.writeheader()
    w.writerows(objs)


parser = argparse.ArgumentParser(description="Extract frequent words from URL.")
parser.add_argument('url', help='URL to fetch')
parser.add_argument('xpath', help='XPath expression')
args = parser.parse_args()

output = fetch(args.url, args.xpath)
words = extract_words(output)
to_csv(sys.stdout, words)
# By pointing sys.stdout, you can print it out on terminal screen,
# And into a file if you want. It's more portable.
