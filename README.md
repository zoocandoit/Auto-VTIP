# AUTO_VTIP

**Filtering IP using VirusTotal API**

AUTO_VTIP is a Python tool for automated IP address analysis using the VirusTotal API. This tool allows you to analyze single IP addresses or bulk IP addresses efficiently.

// 
실무에서 모든 IP리스트를 검증하기에는 공격벡터가 너무 많고 표면적이 넓었습니다.
F/W에 IP 차단리스트를 추가하기 위해 간단하게 제작하였습니다.


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
