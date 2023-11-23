import os
import random
activity = True
location = ""
vars = {"null": "0"}
checkpoints = {"null": 0}
varCount = 0
bracketSeeking = 0

os.system("title OiScript")
os.system("mode 50, 5")
while activity:
    os.system("CLS")
    location = input("Input Location of File: ")
    if os.path.exists(location):
        activity = False
lines = open(location, "r").readlines()
for l in range(len(lines)):
    i = lines[l]
    if i[0:6] == "check ":
        checkpoints[i[6::]] = l
l = -1
os.system("CLS")
while not activity:
    while l < len(lines):
        l += 1
        i = lines[l]
        if bracketSeeking > 0:
            if "}" in i:
                bracketSeeking -= 1
            if "{" in i:
                bracketSeeking += 1
            continue
        while "%" in i:
            j = i[i.find("%") + 1::].replace("\n", "")
            while vars.get(j) is None:
                j = j[0:-1]
                if j == "":
                    break
            if j == "":
                break
            i = i.replace("%" + j, vars[j])
        while "!" in i:
            j = i[i.find("!") + 1::].replace("\n", "")
            while vars.get(j) is None:
                j = j[0:-1]
                if j == "":
                    break
            if j == "":
                break
            i = i.replace("!" + j, vars[j])
        if "%random [" in i:
            i = i.replace(i[i.find("%random"):i.find("]") + 1],
                          str(random.randint(int(i[i.find("[") + 1:i.find(",")]), int(i[i.find(",") + 1:i.find("]")]))))
        if i[0:3] == "set":
            if "=" in i:
                vars[i[4:i.find("=")]] = i[i.find("=") + 1:-1]
            elif "+" in i:
                vars[i[4:i.find("+")]] = str(int(vars[i[4:i.find("+")]]) + int(i[i.find("+") + 1:-1]))
            elif "/" in i:
                vars[i[4:i.find("/")]] = str(int(int(vars[i[4:i.find("/")]]) / int(i[i.find("/") + 1:-1])))
            elif "*" in i:
                vars[i[4:i.find("*")]] = str(int(vars[i[4:i.find("*")]]) * int(i[i.find("*") + 1:-1]))
            elif "$" in i:
                vars[i[4:i.find("$")]] = str(int(vars[i[4:i.find("$")]]) % int(i[i.find("$") + 1:-1]))
            elif "-" in i:
                vars[i[4:i.find("-")]] = str(int(vars[i[4:i.find("-")]]) - int(i[i.find("-") + 1:-1]))
        if i[0:3] == "if ":
            if "=" in i:
                if i[3:i.find("=") - 1] != i[i.find("=") + 2:-3]:
                    bracketSeeking = 1
            elif ">" in i:
                if int(i[3:i.find(">") - 1]) <= int(i[i.find(">") + 2:-3]):
                    bracketSeeking = 1
            elif "<" in i:
                if int(i[3:i.find("<") - 1]) >= int(i[i.find("<") + 2:-3]):
                    bracketSeeking = 1
            elif "$" in i:
                if i[3:i.find("$") - 1] == i[i.find("$") + 2:-3]:
                    bracketSeeking = 1
            continue
        if i[0:5] == "goto ":
            l = checkpoints[i[5::]]
            continue
        if i[0:3] == "dec":
            vars[i[4:i.find("=")]] = i[i.find("=") + 1:-1]
        if i[0:5] == "print":
            print(i[i.find('(') + 1:i.find(')')])
        if i[0:6] == "input ":
            vars[i[6:-1]] = input()
        if i[0:5] == "mode ":
            os.system(i[0:-1])
        if i[0:4] == "exit":
            break
        if i[0:3] == "cls":
            os.system("CLS")
