"""
    Debug 调试
        目的:让程序中断,审查变量取值(Debugger面板的Variables),
                      查看执行流程
        步骤:
            1. 加入断点 -- 在可能出错的地方
            2. 开始调试 -- Debug
            3. 执行一步 -- F8
              .....
            4. 关闭终端 ctrl + Shift + F4
"""
sex = input("请输入性别:")
if sex == "男":
    print("您好，先生")
else:
    print("您好，女士")
