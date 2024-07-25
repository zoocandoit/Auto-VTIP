import argparse
import requests
import re
import json
import os
from dotenv import load_dotenv
import certifi
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Retrieve API key from .env file and store in a variable
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Please set it in the .env file.")

# Initialize the parser
parser = argparse.ArgumentParser(description="Python Automated VT API v3 IP address analysis")
parser.add_argument("-i", "--ip-list", help="bulk ip address analysis")
parser.add_argument("-V", "--version", help="show program version", action="store_true")

# Create a session and set retries
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)

# Function to get IP report
def ipReport(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        "Accept": "application/json",
        "x-apikey": API_KEY
    }

    try:
        response = session.get(url, headers=headers, verify=False)  # SSL 인증 비활성화
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None

    decodedResponse = json.loads(response.text)
    return decodedResponse

# Function to handle IP list and extract malicious IPs
def urlReportIPLst(arg):
    print("Option 3:")
    with open(arg) as fh:
        string = fh.readlines()

    pattern = re.compile(r'(^0\.)|(^10\.)|(^100\.6[4-9]\.)|(^100\.[7-9]\d\.)|(^100\.1[0-1]\d\.)|(^100\.12[0-7]\.)|(^127\.)|(^169\.254\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.0\.0\.)|(^192\.0\.2\.)|(^192\.88\.99\.)|(^192\.168\.)|(^198\.1[8-9]\.)|(^198\.51\.100\.)|(^203.0\.113\.)|(^22[4-9]\.)|(^23[0-9]\.)|(^24[0-9]\.)|(^25[0-5]\.)')

    Public_IPs = [line.rstrip() for line in string if not pattern.search(line.rstrip())]

    pattern2 = re.compile(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')
    valid_ips = [ip for ip in Public_IPs if pattern2.search(ip)]

    print("Valid Public IPs")
    print(valid_ips, "\n")

    malicious_ips = []
    for ip in valid_ips:
        report = ipReport(ip)
        if report and report['data']['attributes']['last_analysis_stats']['malicious'] > 0:
            malicious_ips.append(ip)
            print(f"Malicious IP found: {ip}")

    return malicious_ips

# Read arguments from the command line
args = parser.parse_args()

# Check for --ip-list or -i
if args.ip_list:
    malicious_ips = urlReportIPLst(args.ip_list)
    print(f"Malicious IPs: {malicious_ips}")
# Check for --version or -V
elif args.version:
    print("VT API v3 IP address analysis")
# Print usage information if no arguments are provided
else:
    print("usage: vt-ip-url-analysis.py [-h] [-i IP_LIST] [-V]")