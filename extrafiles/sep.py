lst = eval(open("CH", "r", encoding="UTF-8").read())
pre = "None"
nxt = "None"
for i in range(1, len(lst) - 1):
    pre = lst[i - 1]
    nxt = lst[i + 1]
    with open(f"{lst[i]}.md", "r", encoding="UTF-8") as f:
        file = f.readlines()
    file.insert(1, "\n")
    file.insert(1, "\n")
    file[2] = f"[上一章：{pre}](<{pre}.md>)\n"
    file.append("\n")
    file.append(f"[下一章：{nxt}](<{nxt}.md>)\n")
    with open(f"{lst[i]}.md", "w", encoding="UTF-8") as f:
        for i in file:
            f.write(i)
