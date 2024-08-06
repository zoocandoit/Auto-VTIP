# AUTO_VTIP

**Filtering IP using VirusTotal API**

AUTO_VTIP is a Python tool for automated IP address analysis using the VirusTotal API. This tool allows you to analyze single IP addresses or bulk IP addresses efficiently.

AUTO_VTIP는 VirusTotal API를 사용하여 자동화된 IP 주소 분석을 위한 Python 도구입니다. 이 도구를 사용하면 단일 IP 주소 또는 대량 IP 주소를 효율적으로 분석할 수 있습니다.

// 실무에서 이용하는 F/W에 IP 차단리스트를 추가하기 위해 제작하였습니다.

## Usage
main.py [-h] [-s SINGLE_ENTRY] [-i IP_LIST] [-V]


### Arguments

- `-h, --help`  
  Show this help message and exit.
  
- `-s SINGLE_ENTRY, --single-entry SINGLE_ENTRY`  
  IP for analysis.
  
- `-i IP_LIST, --ip-list IP_LIST`  
  Bulk IP address analysis.
  
- `-V, --version`  
  Show program version.

## Examples

### Bulk IP Analysis
```sh
python main.py -i <path_to_ip_list>
