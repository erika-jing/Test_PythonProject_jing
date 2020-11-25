'''
原有存款1000元，发工资之后存款变为2000元
定义模块
1. money.py saved_money = 1000
2. 定义发工资方法send_money，用来增加收入计算
3. 定义工资查询方法 select_money 用来展示工资数额
4. 定义一个start.py 启动文件展示最终存款金额
'''


saved_money = 1000

def send_money():
    send_money = 1000
    global saved_money
    print(f"发工资前，有存款{saved_money}元")
    saved_money = saved_money + send_money

def select_money():
    print(f"发了工资后，存款一共有{saved_money}元")

if __name__ == '__main__':
    send_money()
    select_money()

