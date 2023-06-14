INPUT1 = ["INT", "INT", "BOOL", "SHORT", "LONG"]
INPUT2 = ["INT", "SHORT", "FLOAT", "INT", "BOOL"]
INPUT3 = ["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]
INPUT4 = [
    "BOOL",
    "LONG",
    "SHORT",
    "LONG",
    "BOOL",
    "LONG",
    "BOOL",
    "LONG",
    "SHORT",
    "LONG",
    "LONG",
]

answer = []
m = ""


def addFullMemory(answer):
    global m
    m = "########"
    answer.append(m)
    m = ""


def solution(arr):
    global m
    for data in arr:
        if data == "INT":
            if len(m) != 0:
                m = m + ((8 - len(m)) * ".")
                answer.append(m)
                addFullMemory(answer)
            else:
                addFullMemory(answer)
        elif data == "LONG":
            if len(m) != 0:
                m = m + ((8 - len(m)) * ".")
                answer.append(m)
                addFullMemory(answer)
                addFullMemory(answer)
            else:
                addFullMemory(answer)
                addFullMemory(answer)
        elif data == "BOOL":
            m += "#"
            if len(m) == 8:
                answer.append(m)
                m = ""
        elif data == "SHORT":
            n, mod = divmod(8 - len(m), 2)
            if n > 0:
                m += mod * "." + "##"
            else:
                m += (8 - len(m)) * "."
                answer.append(m)
                m = "##"
        elif data == "FLOAT":
            n, mod = divmod(8 - len(m), 4)
            if n > 0:
                m += mod * "." + "####"
            else:
                m += (8 - len(m)) * "."
                answer.append(m)
                m = "####"

    if len(m) != 0:
        m += (8 - len(m)) * "."
        answer.append(m)

    if len(answer) > 16:
        return "HALT"
    else:
        return ",".join(map(str, answer))


print(solution(INPUT4))
