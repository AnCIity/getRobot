from pyquery import PyQuery as pq
import requests
import time





class IR:
    def __init__(self):
        pass

    # 将时间转化为时间戳 十位
    @staticmethod
    def timeTotamp(str_time):
        time_array = time.strptime(str_time, "%Y-%m-%d %H:%M")
        # 转换为时间戳
        time_stamp = int(time.mktime(time_array))  # 转化为int类型
        return time_stamp

    def getInfo(self):
		# 初始请求
        response = requests.get('https://d.cleverqq.cn/search.php?mod=forum', timeout=10)
        response.encoding = 'utf-8'
		# 保存cookies
        cookies = response.cookies
		#解析出formhash值
        doc = pq(response.text)
        item = doc('form.searchform input')
        formhash = item.attr('value')
		#拼接URL并请求
        irserchUrl = 'https://d.cleverqq.cn/search.php?formhash=' + formhash + '&srchtxt=%B6%A8%D6%C6&searchsubmit=yes&orderby=dateline'
        response = requests.get(irserchUrl, cookies=cookies)
		# 开始解析数据
        doc = pq(response.text)
        items = doc('.pbw').items()

        itemsList = []
        for item in items:
            l_title = item.find('h3 a').text().replace("\n", "")

            ps = item.find('p').items()
            plist = []
            for p in ps:
                plist.append(p.text())
            l_content = plist[1]
            l_time = item.find('span').html()

            l_Dict = {'title': l_title, 'content': l_content, 'time': l_time}
            itemsList.append(l_Dict)

        for itemList in itemsList:
            print(self.timeTotamp(itemList['time']))




