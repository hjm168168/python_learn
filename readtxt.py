f0 = open('a.txt')
b0 = [i for i in f0.readlines() if len(i.strip("\r\n")) != 0]#每个元素是一行

c0 = [i.split() for i in b0]#把每行按 空格 切割

f = open('b.txt')
b= [i for i in f.readlines() if len(i.strip("\r\n")) != 0]#每个元素是一行
c = [i.split() for i in b]#把每行按 空格 切割

j_num=len(b0)
i_num=len(c0[1])
print i_num;#
print j_num#行

print len(b)



cmp_result=file("cmp_result.txt","a+")

#print c[0]







for i in range(j_num):
    if (c0[i][0]==c[i][0]  and c[i][4]==c0[i][4]):
        pass
    else:
        if(c[i][2]=="stacking"):
            cmp_result.write(c[i][0])
            print c[i][0],int(c0[i][4])-int(c[i][4])
            cmp_result.write(" ")
            cmp_result.write("\n")  
cmp_result.close()

















