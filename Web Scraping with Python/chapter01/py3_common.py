# -*- coding: utf-8 -*-

import requests


def download1(url):
    return requests.get(url).text


def download2(url):
    print('Downloading:', url)
    try:
        html = requests.get(url).text
    except Exception as err:
        print('Downloading error:', err)
        html = None
    return html


def download3(url, num_retries=5):
    print('Downloading:', url)
    try:
        response = requests.get(url)
        html = response.text
        if 500 <= response.status_code < 600:
            html = None
            if num_retries > 0:
                return download3(url, num_retries - 1)

    except Exception as err:
        print('Downloading error:', err)
        return download3(url, num_retries - 1)

    return html


def download4(url, num_retries=5, user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'):
    print('Downloading:', url)
    try:
        headers = {'User-agent': user_agent}
        response = requests.get(url, headers=headers)
        # print(response.status_code)
        html = response.text
        if 500 <= response.status_code < 600:
            html = None
            if num_retries > 0:
                return download4(url, num_retries - 1)

    except Exception as err:
        print('Downloading error:', err)
        return download4(url, num_retries - 1, user_agent)

    return html


def download5(url, num_retries=5, proxies=None, user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'):
    print('Downloading:', url)
    try:
        headers = {'User-agent': user_agent}
        response = requests.get(url, headers=headers, proxies=proxies)
        html = response.text
        if 500 <= response.status_code < 600:
            html = None
            if num_retries > 0:
                return download5(url, num_retries - 1, proxies, user_agent)

    except Exception as err:
        print('Downloading error:', err)
        return download5(url, num_retries - 1, proxies, user_agent)

    return html


download = download5

if __name__ == '__main__':
    print(download('http://example.webscraping.com/sitemap.xml'))
