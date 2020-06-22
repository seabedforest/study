for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print(f"{i}x{j}={i * j}", end="\t")
    print()

for i in range(9, 0, -1):
    for k in range(1, 10 - i):
        print(end="        ")
    for j in range(i, 0, -1):
        print(f"{i}x{j}={i * j}", end="\t")
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}x{j}={i * j}", end="\t")
    print()

for i in range(1, 10):
    for k in range(1, 10 - i):
        print(end="        ")  # 此处为8个字节
    for j in range(1, i + 1):
        print(f"{j}×{i} = {i * j}", end="        ")  # 此处为8个字节
    print(" ")
print("\n")

for i in range(1, 10):
    for k in range(1, i):
        print(end="        ")  # 此处8个空格
    for j in range(i, 10):
        print(f"{j}×{i} = {i * j}", end="        ")  # 此处8个空格
    print(" ")
print("\n")
