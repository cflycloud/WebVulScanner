# README

基于 `python 3.8.0`

使用`pip install -r requirements.txt`安装依赖

修改config.config.py里的config.ini的绝对路径，并且在config.ini里编辑你的项目绝对路径

需要手动安装`wkhtmltopdf`应用 否则无法使用导出PDF文件功能

如果没有文件夹:
**手动建立文件夹：在main下建立log和pdf文件夹，在log里建立xss、csrf、phish等文件夹, phish下建立target和out文件夹**

```python
self.table_data=
[
    [item_data0],
    [item_data1],
    ...,
    [item_dataN]
]
# 检测单元的子项
item_dataN =
[
    ['web0','description0','level0'],
    ...,
    ['webN','descriptionN','levelN']
]

example:
    # xss检测
    item_xss =
    [
        ['http://127.0.0.1','Your Description:XXXXX','7'],
        ['http://127.0.2.1','Your Description:XXXXX','9'],
        ['http://127.0.1.1','Your Description:XXXXX','8'],
        ['http://192.0.9.1','Your Description:XXXXX','7'],
        ...,
        ['http://192.0.9.1','Your Description:XXXXX','7']
    ]
```

你需要把你的`item_data`组装成上述模式，否则无法嵌入项目的数据显示功能



`XSS`漏洞检测：

```python
# xss 反射型
# GET
http://localhost:8080/pikachu/vul/xss/xss_reflected_get.php
# POST
http://localhost:8080/pikachu/vul/xss/xsspost/post_login.php?username=admin&password=123456&submit=submit

# xss DOM型
http://localhost:8080/pikachu/vul/xss/xss_dom.php
http://localhost:8080/pikachu/vul/xss/xss_dom_x.php
http://localhost:8080/dvwa/vulnerabilities/xss_d/?default=Spanish
        
# xss 存储型
http://localhost:8080/pikachu/vul/xss/xss_stored.php
http://localhost:8080/dvwa/vulnerabilities/xss_s/
        
# xss 盲打
http://localhost:8080/pikachu/vul/xss/xssblind/xss_blind.php

# xss 带参
# xss 过滤
http://localhost:8080/pikachu/vul/xss/xss_01.php?message=1111111&submit=submit
# xss js输出
http://localhost:8080/pikachu/vul/xss/xss_04.php?message=kobe&submit=submit
```



`Phish`思路

```python
# 查询总站
https://phishtank.org

# 存活的钓鱼链接
url_list = [
        'http://myvirgin-mobile-login.com/',# 手机购买表单 需要事先人机验证
        'http://myvirgin-mobile-login.com/profile.php', # 手机购买个人信息 需要事先人机验证
        'https://freefireevent2023.github.io/spin/', # 登录ID表单
        'https://systemcesure.buzz/portalserver/bancanetempresarial/index/public/', # 伪造公司介绍面
        'http://192.168.43.135/',# 本机kali的twitter 登录界面
        'https://dkruvnfjf.weebly.com/',# 随时会挂 所以需要实验
        'https://psyopclaim.space/' # ape币 猿币交易
    ]

# 字典列表
keywords = ['登录', '邮箱', '钱包', '密码', '注册', '电话号码', ..., '助词']
```



`A.` 文字识别

自动化工具`selenium`后台打开网页截屏

你需要一个助推器 `chrome_driver.exe` [下载](http://chromedriver.storage.googleapis.com/index.html) 根据自己的浏览器版本下载并加入环境变量

截屏内容放入`ocr`识别模型, 得到文字列表`word_list`

根据敏感词字典匹配文字，计算占比

`B.` 分析源码

自动化工具向浏览器获取网址源码

探测是否存在表单或者跳转链接

`C.` 根据规则判定钓鱼危险等级

不想写了 以后再说



`solution1`:

右键在树状列表添加数据出现空对象bug

首先点击`开始扫描` 然后不输入任何数据 

会提示`请输入正确的网址！`点击`yes` 

出现网站根目录之后 再右键`添加数据`就可以随便写入数据

`solution2`:

当勾选多个检测项目之后界面卡死

首先定好你要检测的项目 比如xss注入 / 钓鱼网站

树状列表勾选网址若干 再勾选项目 **必须先勾选网址再勾选检测项目,否则结果为空**

等待第一次的检测结果写入表格

之后取消刚刚勾选的网址 取消刚刚的项目勾选

进行下一次项目检测 先勾选网址若干 再勾选检测项目

...此后反复

`solution3`:

图片查看无图片 / 钓鱼检测界面卡死

首先你必须用钓鱼网站检测之后才能生成ocr识别图片

直接点`图片查看`会出现图片数据为空的提示

钓鱼网站检测需要~~~科学~~~和==谷歌浏览器、谷歌浏览器的助推器==

因为我的钓鱼测试网站都是国外的站点

🤣🤣👇👇👇👇👇👇👇👇👇🤣🤣
🤣👉🤣👇👇👇👇👇👇👇🤣👈🤣
🤣👉👉🤣👇👇👇👇👇🤣👈👈🤣
🤣👉👉👉🤣👇👇👇🤣👈👈👈🤣
🤣👉👉👉👉🤣👇🤣👈👈👈👈🤣
🤣👉👉👉👉👉🤡👈👈👈👈👈🤣
🤣👉👉👉👉🤣👆🤣👈👈👈👈🤣
🤣👉👉👉🤣👆👆👆🤣👈👈👈🤣
🤣👉👉🤣👆👆👆👆👆🤣👈👈🤣
🤣👉🤣👆👆👆👆👆👆👆🤣👈🤣
🤣🤣👆👆👆👆👆👆👆👆👆🤣🤣

