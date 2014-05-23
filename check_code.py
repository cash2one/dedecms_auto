#!/usr/bin/env python
#-*- coding: utf-8 -*-
#__author__ = 'Ario'


from pytesser import getCheckCode
import urllib2


def downloadCheckCode(url,headers):
    '''
    get check code image
    '''
    with open(codeFile,"wb") as f:
        try:
            req = urllib2.Request(url,headers=headers)
            res = urllib2.urlopen(req)
            f.write(res.read())
            return True
        except Exception,e:
            print "[+] Error:",str(e)
            return False

def main():
    baseUrl="http://localhost/dedecms/5.7"
    global  codeFile
    codeFile="code.jpg"
    checkCodeBaseUrl="/include/vdimgck.php"
    headers={
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":"PHPSESSID=4bncpf8cudfmnquxxdcpkrb12s97; DedeUserID=1; DedeUserID__ckMd5=3e8e80104cbfad5d; DedeLoginTime=1397994952; DedeLoginTime__ckMd5=faedace47fa2ac95"
            }
    checkCodeUrl=baseUrl+checkCodeBaseUrl
    print "[+] download check code now ..."
    tof = downloadCheckCode(checkCodeUrl,headers)
    if tof == False:
        print "[+] download check code Error!"
        print "[+] jsut try again!"
        exit()
    else:
        print "[+] download check code ok!"
    print "[+] image to code now ..."
    code = getCheckCode(codeFile)
    if code == False or len(code)!=4:
        print "[+] image to code Error!"
        print "[+] just try again!"
        exit()
    else:
        print "[+] image to code ok!"
        print "[+] check code is:",code


if __name__ == "__main__":
    try:
        main()
    except Exception,e:
        print "[+] Error: ",str(e)