#  记录所有的学生列表
stu_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【学生管理系统】")
    print("")
    print("1.添加学生")
    print("2.显示全部")
    print("3.搜索学生")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_stu():
    """添加学生"""
    print("-" * 50)
    print("添加学生")
    name_str = input("请输入姓名:")
    gender_str = input("请输入性别:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ:")
    stu_num = input("请输入学号:")
    #  创建一个学生字典，保存学生的信息
    stu_dict = {"name": name_str,
                "gender": gender_str,
                "phone": phone_str,
                "qq": qq_str,
                "stu_num": stu_num}
    #  将记录学生的字典通过 append方法 添加到学生列表当中
    stu_list.append(stu_dict)
    #  print(stu_list)
    print("添加%s成功!" % name_str)


def show_all():
    """显示所有学生"""
    print("-" * 50)
    print("显示所有学生")
    #  打印表头
    for name in ["姓名", "性别", "电话", "QQ", "学号"]:
        print(name, end="\t\t")
    print(" ")

    #  打印分隔线
    print("=" * 50)
    if len(stu_list) == 0:
        print("当前系统中不存在任何学生，请使用添加功能添加")
        return
        #  遍历学生列表依次输出字典信息
    for stu_dict in stu_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t" % (stu_dict["name"], stu_dict["gender"],
                                        stu_dict["phone"], stu_dict["qq"], stu_dict["stu_num"]))


def search_stu():
    """搜索学生"""
    print("-" * 50)
    #  print("查询学生")
    find_name = input("请输入要查询的姓名:")
    for stu_dict in stu_list:
        if stu_dict["name"] == find_name:
            print("姓名\t\t性别\t\t电话\t\tQQ\t\t学号\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t" % (stu_dict["name"], stu_dict["gender"],
                                                      stu_dict["phone"], stu_dict["qq"], stu_dict["stu_num"]))
            #  利用另一个函数分装对找到学生进行的操作
            deal_stu(stu_dict)
            break
    else:
        print("抱歉,未查询到 %s" % find_name)


def deal_stu(stu_dict):
    #  print(stu_dict)

    action_str = input("请选择要执行的操作:"
                       " [1] 修改 [2] 删除 [0] 返回上级菜单 :")

    if action_str == "1":
        print("修改学生成功")
        stu_dict["name"] = input_stu_info(stu_dict["name"], "姓名(回车不修改）：")
        stu_dict["gender"] = input_stu_info(stu_dict["gender"], "性别(回车不修改）：")
        stu_dict["phone"] = input_stu_info(stu_dict["phone"], "电话(回车不修改）：")
        stu_dict["qq"] = input_stu_info(stu_dict["qq"], "QQ(回车不修改）：")
        stu_dict["stu_num"] = input_stu_info(stu_dict["stu_num"], "学号(回车不修改）：")

    elif action_str == "2":

        stu_list.remove(stu_dict)
        print("删除学生成功")


def input_stu_info(dict_value, tip_message):
    """修改学生信息的函数"""
    #  1.提示用户输入内容
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
