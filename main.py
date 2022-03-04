import time
import requests
import datetime
from config import Config
from urllib import parse
from bs4 import BeautifulSoup
from send_email import send_email


def find_new(message_list, cur_new_add, now):
    message_list.extend(cur_new_add)
    write_lines = ["{}新增————————————————————————————————————————————".format(now)]
    for new_add in cur_new_add:
        cur = now + ": " + ", ".join(new_add) + '\n'
        write_lines.append(cur)

    file_name = "result.txt"

    with open(file_name, 'a', encoding='utf-8') as f:
        f.writelines(write_lines)

    title = "截止到{}新增调剂信息汇总".format(now)
    message = "\n".join(write_lines)
    print("{}->本次新增\n{}".format(now, message))
    send_email(title, contain=message, file_name=file_name)


def main(message_list):
    time_today = datetime.datetime.now()
    year, month, day, hour, minute = time_today.year, time_today.month, time_today.day, time_today.hour, time_today.minute
    now = "{}-{}-{}:{}:{}".format(year, month, day, hour, minute)

    # "大学名字":"发布调剂信息页面"
    school_url = Config.school_url

    cur_new_add = []
    for school, url in school_url.items():
        r = requests.get(url)
        html = r.content
        html_doc = str(html, 'utf-8')  # html_doc=html.decode("utf-8","ignore")
        soup = BeautifulSoup(html_doc, 'html.parser')
        for link in soup.find_all('a'):
            href, title = link.get('href'), link.text
            if title is None or title.strip() == "":
                continue
            if href[:4] != 'http':  # 代表是相对路径，要转为绝对路径
                href = parse.urljoin(url, href)
            suspected_words = ["复试", "调剂"] if school == "大连理工大学" else ["调剂"]
            for word in suspected_words:
                if word in title:
                    cur = [school, href, title]
                    if cur not in message_list:
                        cur_new_add.append(cur)
    if cur_new_add:
        find_new(message_list, cur_new_add, now)
    else:
        print("{}->本次没新增调剂信息".format(now))


if __name__ == "__main__":
    message_list = []
    while True:
        main(message_list)
        time.sleep(3600)  # 一小时查询一次 3600
