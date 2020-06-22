list01 = ["北京", ["上海", "深圳"]]
list02 = list01
list03 = list01[:]
list03[0] = "北京03"
list03[1][1] = "深圳03"
print("list01:", list01)  # ?
list02[0] = "北京02"
list02[1][1] = "深圳02"
print("list02:", list02)  # ?
