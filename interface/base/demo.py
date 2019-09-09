import requests
import json

class RunMain():
    #
    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)


    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return json.loads(res)
if __name__ == '__main__':
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
    data = {
        'cart': '11'
    }
    # run = RunMain()
    # run.run_main(url,'GET',data)
    # print(run.res)
    run = RunMain()
    res = run.run_main(url,'GET',data)
    print(res)

