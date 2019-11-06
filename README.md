# getRobot  
get info send Email  

IR论坛搜索分析：  
1.请求得到网站初始信息
2.保存初始cookies
3.分析获取初始HTML中formhash值
4.'https://d.cleverqq.cn/search.php?formhash=' + formhash + '&srchtxt=' + 搜索内容（URL编码(GBK)） + '&searchsubmit=yes&orderby=dateline'
5.然后带初始cookies请求
