import time

def dispaly_time(func):
    def wrapper(*args):
        #  传入多个参数
        t1 =time.time()
        func(*args)
        t2 =time.time()
        print("Total time :%.4f" %(t2-t1))
    return wrapper
    """
    函数名是指代的函数代码所在的空间，函数名加括号，指代的是函数往外传递的数据，
    而return就是往外传递数据的工具，如果函数名（）没有接收到return出来的数据，
    那么“函数名（）”除了执行命令外，什么也不是，函数往外传递的数据就丢失了。
    """

@dispaly_time
def Print():
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")



Print()