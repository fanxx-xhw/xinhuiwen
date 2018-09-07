import os
from lib.path import WEBPICTUREPATH
import requests,yagmail


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEBPICTUREPATH)

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: WEBPICTUREPATH + file, self.filelist)))

    def huoqucity(self):

        r = requests.get(url='https://api.map.baidu.com/location/ip', params={'ak': 'C4GDE49PkTFGwenusdAoMgLdeeKoxwYQ'})
        result = r.json()
        city = result['content']['address_detail']['city']
        res = city.split('市')[0]
        return res
    def baiduAK(self):
        ak = 'C4GDE49PkTFGwenusdAoMgLdeeKoxwYQ'
        return ak

    def send_email(self,to,cc,subject,contents,attachments):
        username = '13051552536@163.com'
        passwd = '1q2w3e4r'
        mail = yagmail.SMTP(user=username,
                            password=passwd,
                            host='smtp.163.com',
                            # port=25
                            )
        mail.send(
            to=to,
            cc=cc,
            subject=subject,
            contents = contents,
            attachments=attachments
        )
        print('send successfully')

T = Tool()
# print(T.huoqucity())
