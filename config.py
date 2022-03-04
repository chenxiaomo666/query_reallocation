class Config:
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = '1*********3'
    # 密码(部分邮箱为授权码)
    mail_pass = 'B*********G'
    # 邮件发送方邮箱地址
    sender = '13*********3@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ["m******2@163.com", "2******9@qq.com"]

    # "大学名字":"发布调剂信息页面"
    school_url = {
        "大连理工大学": "http://gs.dlut.edu.cn/yjszs/zcwj1.htm",
        "南京信息工程大学": "https://yjs.nuist.edu.cn/zsgz/sszs/19.htm",
        "兰州大学": "http://yz.lzu.edu.cn/tongzhigonggao/index.html",
        "重庆大学": "http://yz.cqu.edu.cn/ss_news.html",
        "山东大学": "https://www.yz.sdu.edu.cn/tzgg/25.htm",
        "郑州大学": "http://gs.zzu.edu.cn/zsgz/zxtz.htm",
        "青岛大学": "https://grad.qdu.edu.cn/infoArticleList.do?columnId=11363",
    }