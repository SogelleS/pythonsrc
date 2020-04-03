# http请求报文结构(4部分)
以百度为例
## 请求行
GET / HTTP/1.1
请求方式 请求服务器资源的路径 协议与版本

请求行单独占一行

## 请求头
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Sec-Fetch-Dest: document
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BDUSS=xxxxxxxxx

### host 
表示主机名
### Accept-Encoding: gzip, deflate, br
是浏览器发送给服务器声明浏览器支持的压缩编码类型
比如 gzip 实际上网页时被压缩后发送给客户端的所以
服务器需要知道浏览器支持的解压格式
### Accept-charset
表示浏览器支持的字符集
### Accept-Language: zh-CN,zh;q=0.9
表示浏览器接受的语言q表示权重 越大越优先
### Referer: http://xxxxxxxx
表示请求来自那个网站
### Cookie: BDUSS=xxxxxxxxx
发送浏览器储存的cookie
### User-Agent: Mozilla/5.0 xxxxxxxx
用户代理 当前发起请求的浏览器内核信息
### Accept: text/html,application/xhtml+xmlxxx
表示浏览器可以接受的数据类型
### content-length
只有post才会有的请求头表示我要提交的信息大小(字节)
### if-modified-since
只有get有,询问服务器请求的资源是否被修改

##  空行
一行空行用来分隔请求头和请求数据
## 请求主体（请求数据）
只有post方法才有请求数据