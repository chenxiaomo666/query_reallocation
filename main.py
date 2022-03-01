import time
import requests
import datetime
from bs4 import BeautifulSoup
from send_email import send_email


def main():
    time_today = datetime.date.today()
    today = datetime.date.today().isoformat()
    school_url = {
        "大连理工大学": "http://gs.dlut.edu.cn/yjszs/zcwj1.htm",
        "南京信息工程大学": "https://yjs.nuist.edu.cn/zsgz/sszs/19.htm",
        "兰州大学": "http://yz.lzu.edu.cn/tongzhigonggao/index.html",
        "重庆大学": "http://yz.cqu.edu.cn/ss_news.html",
        "山东大学": "https://www.yz.sdu.edu.cn/tzgg/25.htm",
        "郑州大学": "http://gs.zzu.edu.cn/zsgz/zxtz.htm",
        "青岛大学": "https://grad.qdu.edu.cn/infoArticleList.do?columnId=11363",
    }
    result = []
    message_list = []
    for school, url in school_url.items():
        r = requests.get(url)
        html = r.content
        html_doc = str(html, 'utf-8')  # html_doc=html.decode("utf-8","ignore")
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print(html_doc)
        suspected = []
        for link in soup.find_all('a'):
            href, title = link.get('href'), link.text
            # print(title)
            if title is None or title.strip() == "":
                continue
            suspected_words = ["复试", "调剂"] if school == "大连理工大学" else ["调剂"]
            for word in suspected_words:
                if word in title:
                    cur = [school, href, title]
                    if cur not in message_list:
                        message_list.append(cur)
                    suspected.append({
                        "href": href,
                        "title": title
                                      })
        result.append({school: suspected})
    write_lines = []
    for message in message_list:
        cur = today + ": " + ", ".join(message) + '\n'
        write_lines.append(cur)

    print(write_lines)

    title = "截止到{}调剂信息汇总".format(today)
    send_email(title, "\n".join(write_lines))


if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)   # 一小时查询一次
