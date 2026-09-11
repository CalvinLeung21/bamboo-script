# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")

from byteplus_sdk.cdn.service import CDNService


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python purge_bp_cdn.py <ak> <sk> <url1> [url2] [url3] [url4]")
        sys.exit(1)

    ak = sys.argv[1]
    sk = sys.argv[2]
    urls = sys.argv[3:]

    if len(urls) > 4:
        print("Error: Maximum 4 URLs can be submitted at once.")
        print("Received:", len(urls))
        sys.exit(1)

    urls_string = "\n".join(urls)

    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)

    body = {
        "Type": "dir",
        "Prefix": True,
        "Urls": urls_string
    }

    resp = svc.submit_refresh_task(body)
    print(resp)
