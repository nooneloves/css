#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

CorrectUsername = "ali"
CorrectPassword = "sher"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[1;93mTool Username \x1b[1;93m»» \x1b[1;96m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[1;93mTool Password \x1b[1;93m»» \x1b[1;96m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open http://pcleph.com/18643//9ovEy/?sc=1&sc=1&l=1&ppy=6677355&i=6677355')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open http://pcleph.com/18643//9ovEy/?sc=1&sc=1&l=1&ppy=6677355&i=6677355')
        id = raw_input('\033[1;96m[+] \x1b[1;97mID/Email\x1b[1;92m: \x1b[1;96m')
	pwd = raw_input('\033[1;96m[+] \x1b[1;97mPassword\x1b[1;92m: \x1b[1;96m')
	tik()
