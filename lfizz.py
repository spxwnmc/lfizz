#!/usr/bin/env python
import requests
import argparse


def print_lfizz(url):
    print(f'\033[0;35m[+] {url} \033[0m')


def fuzz(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            ful_url = url + line.strip()
            rqs = requests.get(ful_url)
            size = len(rqs.content)
            if rqs.status_code == 200 and size > 3:
                print_lfizz(ful_url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='URL to fuzz', required=True)
    parser.add_argument('-w', '--wordlist',
                        help='Wordlist to use', required=True)
    args = parser.parse_args()

    fuzz(args.url, args.wordlist)
