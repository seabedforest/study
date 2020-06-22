"""
    5. 斐波那契数列：从第三项开始,每一项都等于前两项之和。
        在终端中获取长度,创建斐波那契数列。
        演示：
            请输入斐波那契数列长度：8
            [1, 1, 2, 3, 5, 8, 13, 21]
"""
#斐波那契数列初始化
sequence =[1,1]
lenght = int(input("请输入斐波那契数列的长度: "))
if lenght == 1:
    print([1])
else:
    for __ in range(lenght-2):
        sequence.append(sequence[-1] + sequence[-2])
    print(sequence)
