# -*- coding: utf-8 -*-
import  urllib
import  urllib2
import  re
import  cookielib
import  HTMLParser

# 解析HTML页面的类
class MyHTMLParser (HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "td":
            if len(attrs) == 0:
                pass
            else:
                for(variable, value) in attrs:
                    if variable == "td":
                        self.links.append(value)

# 数据参数
verifyURL = 'http://172.16.65.99/CheckCode.aspx'
mainURL = 'http://172.16.65.99/default2.aspx'
username = '14408300135'
password = '5201314ace'
name = '赵聪'
gnmkdm = 'N121605'

# 生成cookie处理器来乱来存储所有访问的网站的cookies数据
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

#访问并下载验证码
picture = opener.open(verifyURL).read()
local  =open('verify.jpg', 'wb')
local.write(picture)
local.close()

secretCode = raw_input('输入验证码：')

#登录发送的数据
postData = {
    '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz4hAtqyqUyL0G3Bvv9ESSw7WqdQ5Q==',  #*******
    'txtUserName': username,
    'TextBox2' : password,
    'txtSecretCode' : secretCode,   #验证码数据
    'RadioButtonList1' : '学生',
    'Button1' : '',
    'Button2' : '',
    'lbLanguage' : ''
}

#登录发送的验证
headers = {
    # 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Language' : 'zh-CN,zh;q=0.8',
    # 'Connection' : 'keep-alive',
    # 'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
    # 'Origin' : 'http://218.75.197.124:83',
    # 'Referer' : 'http://218.75.197.124:83/default2.aspx',
    # 'Host' : '218.75.197.124:83',
    # 'Cookie' : 'ASP.NET_SessionId=rtoq3r554zza4a45uw0k0bb',
    }

#开始登录
data = urllib.urlencode(postData)
request = urllib2.Request(mainURL,data,headers)

try:
    response = opener.open(request)
    result = response.read().decode('gb2312')
    print '成功进入教务系统！'
    print result
except urllib2.HTTPError,e:
    print e.code

for i in cookie:
    Cookie = i.name + "=" + i.value
print Cookie


#到达查询成绩界面所需的验证数据
headers1 = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'Connection' : 'keep-alive',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
    'Origin' : 'http://218.75.197.124',
    'Referer': 'http://218.75.197.124/xs_main.aspx?xh=' + username,  #Referer
    'Host' : '218.75.197.124:83',
    'Cookie': Cookie,
    'Pragma': 'no-cache',
}

#查询成绩界面的URL的地址数据
URLdata = urllib.urlencode({
     'xh': '14408300135',
     'xm':  name,
     'gnmkdm': 'N121605'
})

# data1 = urllib.urlencode(URLdata)

#查询成绩的超链接引用,并进入从而获得 __VIEWSTATE 的值
hrefURL = 'http://218.75.197.124:83/xscjcx.aspx?' + URLdata
print  hrefURL
request1 = urllib2.Request(hrefURL,None,headers1)
loginPage = unicode(opener.open(request1).read(),'gb2312').encode("utf-8")

#正则表达式来匹配（__VIEWSTATE）的值
string = r'name="__VIEWSTATE" value="(.+?)"> '
view = re.compile(string)
__VIEWSTATE = view.findall(hrefURL)[0]

#访问成绩页面所需发送的数据
postData2 = {
    '__VIEWSTATE' : __VIEWSTATE,
    'btn_zcj' : "历年成绩"
}
data2 = urllib.urlencode(postData2)

#进入hrefURL并发送data2数据来得到历年成绩的页面数据
request2 = urllib2.Request(hrefURL,data2,headers1)
scoreHtml = opener.open(request2)
scorePage = scoreHtml.read().decode('gb2312')

#解析页面打印成绩
htmlParser = MyHTMLParser()
htmlParser.feed(scorePage)
htmlParser.close()
print htmlParser.links


