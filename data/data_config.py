#coding=utf-8
class global_var:
    #固定的列
    Id=0
    name=1
    url=2
    run=3
    request_way=4
    header=5
    case_depend=6
    data_depend=7
    filed_depend=8
    random_data=9
    data=10
    expect=11
    resule=12
    result_write=13
    data_twodepend=14
    data_twodepend_value=15
#获取caseid
def get_id():
    return global_var.Id
def get_url():
    return global_var.url
def get_run():
    return global_var.run
def get_run_way():
    return global_var.request_way
def get_header():
    return global_var.header


def get_data():
    return global_var.data
def get_expect():
    return global_var.expect
def get_resule():
    return global_var.resule
def get_data_dependent():
    return global_var.data_depend

def get_twodata_dependent():
    return global_var.data_twodepend


def get_twodata_dependent_value():
    return global_var.data_twodepend_value
def get_case_dependent():
    return global_var.case_depend
def get_file_dependent():
    return global_var.filed_depend
def get_result_write():
     return global_var.result_write

def get_random_data():
    return global_var.random_data




