# 가위바위보
def solution(rsp):
    rsp_dic = {"2": "0", "0": "5", "5": "2"}
    return "".join([rsp_dic.get(i) for i in rsp])


print(solution("2"))
print(solution("205"))