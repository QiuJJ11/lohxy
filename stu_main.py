import stu_tools

while True:

    # 显示功能菜单
    stu_tools.show_menu()

    action_str = input("请选择希望执行的操作:")
    print("你选择的操作是[%s]" % action_str)
    if action_str in ["1", "2", "3"]:

        #  pass为占位符，只是完善程序结构
        if action_str == "1":
            stu_tools.new_stu()
        elif action_str == "2":
            stu_tools.show_all()
        elif action_str == "3":
            stu_tools.search_stu()

    elif action_str == "0":
        print("欢迎再次使用学生管理系统")
        break
    else:
        print("您输入的不正确，请重新输入")
