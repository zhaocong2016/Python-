# -*- coding: utf-8 -*-
import  urllib
import  urllib2
import  re
import  cookielib

verifyURL = 'http://218.75.197.124:83/CheckCode.aspx'
mainURL = 'http://218.75.197.124:83/'

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

username = '14408300135'
password = '5201314ace'

picture = opener.open(verifyURL).read()

local  =open('verify.jpg','wb')
local.write(picture)
local.close()

secretCode = raw_input('输入验证码：')

postData = {
    '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz4lPcdmHNydfQHS9Y5hivAN74ikCQ==',
    'txtUserName': username,
    'TextBox2' : password,
    'txtSecretCode' : secretCode,
    'RadioButtonList1' : '学生',
    'Button1' : '',
    'Button2' : '',
    'lbLanguage' : ''
}

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Connection' : 'keep-alive',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'
    }

data = urllib.urlencode(postData)
request = urllib2.Request(mainURL,data,headers)

try:
    response = opener.open(request)
    result = response.read().decode('gb2312')
    print '成功进入教务系统！'
except urllib2.HTTPError,e:
    print e.code

postData1 = {

}
# request1 = urllib2.Request('http://218.75.197.124:83/xscjcx.aspx?xh=14408300135&xm=赵聪&gnmkdm=N121605')
# response1 = opener.open(request1)
# result1 = response1.read().decode('gb2312')
# print result1
