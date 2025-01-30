#!/usr/bin/env python3
#
# Name: check_truenas_scale.py
# Description: Check TrueNAS scale alerts via RestAPI
# License: GPLv3
# Copyright (c) 2025 Tsvetan Gerov

import argparse
import requests
import json
import sys
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def alerts(hostname, token):
    warning = 0
    critical = 0
    message = ""

    url = f"https://{hostname}/api/v2.0/alert/list"
    headers = {
        'Authorization': "Bearer " + token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['level'] == "CRITICAL" and not item['dismissed']:
                critical = critical +1
                message = message + item['formatted'] + " "

            elif item['level'] == "WARNING" and not item['dismissed']:
                warning = warning +1
                message = message + item['formatted'] + " "

    else:
        print(f"[UNKNOWN] Unable to connect: Error {response.status_code}")
        sys.exit(3)

    if critical > 0:
        print(f"[CRITICAL] ({critical}) {remove_html_tags(message)})")
        sys.exit(2)
    elif warning > 0:
        print(f"[WARNING] ({warning}) {remove_html_tags(message)}")
        sys.exit(1)
    else:
        print("[OK] All good!")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(
                    prog='check_truenas_scale.py',
                    description="Check TrueNAS scale alerts via RestAPI",
                    epilog='Send email to checks@gerov.eu if you have questions regarding use of this software.')
    parser.add_argument('-H', '--hostname', required=True, type=str, help='Host name or IP Address')
    parser.add_argument('-t', '--token', required=True, type=str, help='API token')

    args = parser.parse_args()

    alerts(args.hostname, args.token)

if __name__ == '__main__':
    main()
