datas=datatwo=""
with open ('file1.txt') as fn:
    datas=fn.read()
with open('file2.txt') as fn:
    datatwo=fn.read()
datas+="\n"
datas+=datatwo
with open('file3.txt','w') as fp:
    fp.write(datas)
