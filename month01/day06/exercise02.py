"""
 将下列英文语句按照单词进行翻转.
To have a government that is of people by people for people

people for people by people of is that government a have To
"""
str01 = "To have a government that is of people by people for people"
list_str01 = str01.split(" ")
print(' '.join(list_str01[::-1]))