#  -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../")
# from byteplus_sdk.example.cdn import ak, sk
from byteplus_sdk.cdn.service import CDNService

# print (sys.arg)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python script.py <ak> <sk> <url>")
        sys.exit(1)

    ak = sys.argv[1]
    sk = sys.argv[2]
    url = sys.argv[3]

    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)

    body = {
        "Type": "dir",
        "Prefix": True,
        "Urls": url
    }

    resp = svc.submit_refresh_task(body)
    print(resp)
