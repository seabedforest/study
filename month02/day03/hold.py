"""
空洞文件
"""
# f = open("file.txt",'wb')
# f.write(b"begin")
# f.seek(1024,2)
# f.write(b'end')
# f.close()
f = open("file.txt",'ab')
print(f.tell())
s=f.seek(-200,2)
f.write("frist,two,three,four,five".encode())
f.close()