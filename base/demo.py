#coding=utf-8
import requests
import json
import gzip
import re


class RunMain:
    #def __init__(self,url,method,data=None,cookies=None):
        #self.res=self.run_main(url=url,method=method,data=data,cookies=cookies)


    def send_post(self,url,data,headers=None):
        res=requests.post(url=url,data=data,headers=headers,verify=False)

        try:
            result=json.loads(res.content.decode())

        except Exception:
            result=res.content.decode()
        # print (gzip.decompress(res).decode("utf-8"))
        return result



    def send_get(self,url,data=None,headers=None):
        res=requests.get(url=url,headers=headers,verify=False)

        try:
            result = json.loads(res.content.decode())

        except Exception:
            result = res.content.decode()

        return result



    def run_main(self,url,method,data=None,headers=None):
        res=None
        if method=="post":
            res=self.send_post(url=url,data=data,headers=headers)
        else:
            res=self.send_get(url=url,data=data,headers=headers)
        return res


if __name__=="__main__":
    run=RunMain()
    # url="http://bbsclick.10jqka.com.cn/inc?"
    # # method="get"
    data={
        "pid": "913865",
        "state": "1",

    }

    headers={
        "User-Agent": "iPhoneTargetType/hexinPro/10.10.30 (Royal Flush) innerversion/I037.08.289 build/10.10.31 hxtheme/1 hxFont/normal Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304",
        "cookie":"PHPSESSID=oqbs88gg5gpc8ngp75tkhm5a27; Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333=1560234283; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1560234283; hxmPid=share_sns_lungu_ht_tz-293; Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333=1560474518; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1560474518; v=AoqtI3Q14825BG9hzfLI4QDg23svew77AP6CeRTiNutoiCQt_Ate5dCP0ovn; user=MDrNrLuoy7PQocWjOjpOb25lOjUwMDo2NDIzODU4NTo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxLDQwOzIsMSw0MDszLDEsNDA7NSwxLDQwOzgsMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEsNDA6NzM6Ojo1NDEyMjM5NToxNTYwODQwNjY2Ojo6MTIzNDUxMDY4MDoyMjczMzQ6MDoxMDJmZGIxODcyMjE0MzVjZjk1M2U0MGYwNDBlZDY5NzA6ZGVmYXVsdF8yOjA%3D; userid=54122395; u_name=%CD%AC%BB%A8%CB%B3%D0%A1%C5%A3; escapename=%25u540c%25u82b1%25u987a%25u5c0f%25u725b; ticket=ed0d6220377d13a5b39f5c28d9dcb8f4"}
    # res=run.send_get(url=url,data=data,headers=headers)
    # print(res)
    url="http://t.10jqka.com.cn/m/stock/addHotComment/"

    res=run.run_main(url=url,data=data,headers=headers,method="post")
    print(res)
