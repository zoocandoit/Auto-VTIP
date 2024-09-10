# AUTO_VTIP

**Filtering IP using VirusTotal API**

AUTO_VTIP is a Python tool for automated IP address analysis using the VirusTotal API. This tool allows you to analyze single IP addresses or bulk IP addresses efficiently.

> 실무에서 모든 IP리스트를 검증하기에는 공격벡터가 너무 많고 표면적이 넓었습니다.

> F/W, IPS에 IP 차단리스트를 작성하기 위해 간단하게 제작된 도구입니다.

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
```  

## Error Code
| HTTP Code | Error Code                    | Description                                                                                                                                                 |
|-----------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 400       | BadRequestError                | The API request is invalid or malformed. The message usually provides details about why the request is not valid.                                          |
| 400       | InvalidArgumentError           | Some of the provided arguments are incorrect.                                                                                                              |
| 400       | NotAvailableYet                | The resource is not available yet, but will become available later.                                                                                        |
| 400       | UnselectiveContentQueryError   | Content search query is not selective enough.                                                                                                              |
| 400       | UnsupportedContentQueryError   | Unsupported content search query.                                                                                                                          |
| 401       | AuthenticationRequiredError    | The operation requires an authenticated user. Verify that you have provided your API key.                                                                  |
| 401       | UserNotActiveError             | The user account is not active. Make sure you properly activated your account by following the link sent to your email.                                    |
| 401       | WrongCredentialsError          | The provided API key is incorrect.                                                                                                                         |
| 403       | ForbiddenError                 | You are not allowed to perform the requested operation.                                                                                                    |
| 404       | NotFoundError                  | The requested resource was not found.                                                                                                                      |
| 409       | AlreadyExistsError             | The resource already exists.                                                                                                                               |
| 424       | FailedDependencyError          | The request depended on another request and that request failed.                                                                                           |
| 429       | QuotaExceededError             | You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.                                            |
| 429       | TooManyRequestsError           | Too many requests.                                                                                                                                         |
| 503       | TransientError                 | Transient server error. Retry might work.                                                                                                                  |
| 504       | DeadlineExceededError          | The operation took too long to complete.                                                                                                                   |

