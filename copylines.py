from distutils.unixccompiler import UnixCCompiler
from pickle import TRUE
import re

strSrc1 = "exp_alive_supervision"
strSrc2 = "hc_alive"
strSrc3 = "scp"

strRepl_1 = '(exp_alive_supervision)'
strRepl_2 = '(hc_alive)'
strRepl_3 = '(scp)'

uiCopyTimes = 100

print("start copy")

fdRead = open("D:\document\python\copylines\model.json", "r")
fdWrite = open("D:\document\python\copylines\dst.json", "w+")

strfind = ''
strWrite = ''
uiCount = 0
uiInnerIndex = 1
uiOuterIndex = 1
strTemp  = ''
result = 0
src = ''
uiInto = 0

while uiCopyTimes > 0:

    for line in fdRead.readlines():
        #关键字检测
        if re.search(strRepl_1, line):
            strFind = re.search(strRepl_1, line)
            uiInto = 1
        elif re.search(strRepl_2, line):
            strFind = re.search(strRepl_2, line)
            uiInto = 1
        elif re.search(strRepl_3, line):
            strFind = re.search(strRepl_3, line)
            uiInto = 1
        else:
            fdWrite.write(line)
        #关键字更改
        if uiInto:
            strTemp = strFind.group() + str(uiInnerIndex) + '_' + str(uiOuterIndex)
            strWrite = re.sub(strFind.group(), strTemp, line)
            uiCount += 1

            if uiCount % 15 == 0:
                uiInnerIndex += 1
                uiOuterIndex = 0
            if uiCount % 3 == 0:
                uiOuterIndex += 1
            fdWrite.write(strWrite)
            uiInto = 0

    fdWrite.write('\n')
    fdRead.seek(0)
    uiCopyTimes -= 1
    print(uiCopyTimes, end = "\t")

fdWrite.close()
fdRead.close()