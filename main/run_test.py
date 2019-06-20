import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append("D:\jenkins")
from data.get_data import Get_data
from base.demo import RunMain
from util.commen import CommonUtil
from util.send_mail import SendMail
from redis import *
import json
from jsonpath_rw import jsonpath,parse



class Run_Test():
    def __init__(self):
        self.data=Get_data()
        self.run=RunMain()
        self.com_utl=CommonUtil()
        self.send=SendMail()




    def go_on_run(self):
        pass_count=[]
        fail_count=[]
        cow_count=self.data.get_base_lines()

        for i in range(1,cow_count):
            case=self.data.get_caseid(i)
            url=self.data.get_url(i)
            method=self.data.get_request_method(i)

            data=self.data.get_data_for_json(i)

            headers = self.data.get_headers_for_json(i)

            expect=self.data.get_expect_data(i)

            is_run=self.data.get_is_run(i)
            #depent_case=self.data.is_depend(i)

            depent_cases=self.data.get_depend_for_json(i)
            g_params=[]




            if is_run=="yes":
                if depent_cases != None:


                    #老师的方法解决依赖

                    # self.depend_data = Deppenddent_data(depent_case)
                    # depend_response_data = self.depend_data.get_data_for_key(i)

                    #自己根据redis解决依赖
                    if method == "post":
                        for d_case in  depent_cases:
                            depent_case=d_case['case']
                            dependent_data=d_case['value']
                            depent_key=d_case['key']
                            # dependent_data = self.data.get_dependent_key(i)  # 结果是result[id]
                            # print("dependent_data是%s" % dependent_data)
                            # print(type(dependent_data))
                            src = StrictRedis()
                            response_data = src.get(depent_case)
                            response_data = response_data.decode(encoding='utf-8')
                            response_data = json.loads(response_data)

                            json_exe = parse(dependent_data)
                            madle = json_exe.find(response_data)

                            # print("madle是%s" % madle)
                            depend_value = [math.value for math in madle][0]
                            data[depent_key] = depend_value
                    else:
                        for g_case in depent_cases:
                            depent_case=g_case['case']
                            dependent_data=g_case['value']


                            src = StrictRedis()
                            response_data = src.get(depent_case)
                            response_data = response_data.decode(encoding='utf-8')
                            response_data = json.loads(response_data)

                            json_exe = parse(dependent_data)
                            madle = json_exe.find(response_data)
                            depend_value = [math.value for math in madle][0]
                            print("可变的数据是%s"%depend_value)
                            g_params.append(depend_value)
                        print(g_params)
                        tup=tuple(g_params)
                        if len(tup)==1:
                            url=url.format(tup[0])
                        else:
                            url=url.format(tup)
                            print("url是%s"%url)


                res=self.run.run_main(url,method,data,headers)
                result=json.dumps(res)




                src = StrictRedis()

                src.set(case,result)

                res=json.loads(result)
                print(res)

                if self.com_utl.is_contain(expect,res):
                    self.data.write_value(i,"pass")
                    pass_count.append(i)
                else:
                    res=str(res)
                    self.data.write_value(i, res)
                    fail_count.append(i)

        #self.send.send_main(pass_count,fail_count)






if __name__=="__main__":
    run=Run_Test()
    run.go_on_run()