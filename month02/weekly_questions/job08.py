"""
如果字符串一的所有字符按其在字符串中的顺序出现在另外一个字符串二中，则字符串一称之为字符串二的子串。
注意，并不要求子串（字符串一）的字符必须连续出现在字符串二中。
请编写一个函数，输入两个字符串，求它们的最长公共子串，并打印出最长公共子串。
例如：输入两个字符串BDCABA 和ABCBDAB，字符串BCBA 和BDAB 都是是它们的最长公共子串，
则输出它们的长度4，并打印任意一个子串。
@author hailin
@date 2020-06-18
"""


def lcsubstr(s1, s2):
    # 生成矩阵 填充0 多生成一位防止越界
    ex = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    mymax = 0  # 求最长子串的长度
    p = 0  # 求最长子串在s1中最后一位的索引
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                # 如果字符匹配上 累加1
                ex[i + 1][j + 1] = ex[i][j] + 1
                # 如果累加后的结果比原本的max大  更新max值
                if ex[i + 1][j + 1] > mymax:
                    mymax = ex[i + 1][j + 1]
                    # 更新索引
                    p = i + 1
    for item in ex:
        print(item)
    return s1[p - mymax:p], mymax  # 返回最长子串 和长度


print(lcsubstr('BDCABA', 'ABACBDAB'))
