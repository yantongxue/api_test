#coding=utf-8
from util.operation_excel import Operation_excel
from data.get_data import Get_data
from base.demo import RunMain
import json
from jsonpath_rw import jsonpath,parse
from redis import *
class Deppenddent_data:
    def __init__(self,case_id):
        self.case_id=case_id
        self.ope_excel=Operation_excel()
        self.data=Get_data()

    #根据case_id获取整行数据
    def get_case_line_data(self):
        rows_data=self.ope_excel.get_row_value(self.case_id)
        return rows_data



     #根据行num执行依赖的接口
    def run_dependent(self,case_id):
        run=RunMain()
        row_num=self.ope_excel.get_row_num(case_id)
        url=self.data.get_url(row_num)
        method=self.data.get_request_method(row_num)
        request_data=self.data.get_data_for_json(row_num)
        headers=self.data.get_headers_for_json(row_num)

        res=run.run_main(url,method,request_data,headers)
        return res

    # 依赖的接口执行完之后，在依赖的接口返回数据中找到下个接口需要用的数据并且赋值给下个接口
    def get_data_for_key(self,row):
        dependent_data=self.data.get_dependent_key(row)


        #print("所有依赖的字段是%s"%dependent_data)
        #print(type(dependent_data))
        response_data=self.run_dependent(self.case_id)

        print("执行依赖接口的返回值是%s"%response_data)
        #print(type(response_data))
        json_exe=parse(dependent_data)
        madle=json_exe.find(response_data)
        print("madle是%s"%madle)
        return[math.value for math in madle][0]


    def  get_data_key(self,row,case_id):
        dependent_data = self.data.get_dependent_key(row)  # 结果是result[id]
        src = StrictRedis()
        response_data = src.get(case_id)
        response_data = response_data.decode(encoding='utf-8')

        response_data = json.loads(response_data)
        json_exe = parse(dependent_data)
        madle = json_exe.find(response_data)
        # print("madle是%s" % madle)
        depend_value = [math.value for math in madle][0]
        return depend_value





if __name__=="__main__":
    src=StrictRedis()
    case_id="case1"
    dep=Deppenddent_data(case_id)
    dep.get_data_key(12,src,case_id)




