# http 响应报文结构

## 响应行(状态行)
HTTP/1.1 200 OK
协议/版本 响应状态码 对响应状态的描述
 
## 响应头
Bdpagetype: 2
Bdqid: 0xb9fbd81200016bd5
Cache-Control: private
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html;charset=utf-8
Date: Thu, 26 Mar 2020 11:16:22 GMT
Expires: Thu, 26 Mar 2020 11:16:22 GMT
Server: BWS/1.1
Set-Cookie: BDSVRTM=64; path=/
Set-Cookie: BD_HOME=1; path=/
Set-Cookie: H_PS_PSSID=1431_31118_21106_31186_30823_31086_26350_22160; path=/; domain=.baidu.com
Strict-Transport-Security: max-age=172800
Traceid: 1585221382259777409013401542687992146901
X-Ua-Compatible: IE=Edge,chrome=1
Transfer-Encoding: chunked

server 服务器版本
last-modified 最后修改时间
date 响应时间
content-length 响应主体大小 （字节）
content-type 响应类型
location 重定向 浏览器马上转跳
refresh 刷新

## 空行
同请求报文
## 响应主体(数据)
响应的数据