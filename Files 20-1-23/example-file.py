# f=open('test1','r') # 'r' - read the file
#print(f.read())

# for i in f:
#     print(i)
# f.close()
# print(f.read(8))
# print(f.readline())
# print(f.readline()) # used to read line by line

# f=open('test1','a') # 'a' used to append at the end of the file
# f.write('python is a oop')
# f.close()

# f = open('test1','w') # 'w'- used to write
# f.write('python is a oops')
# f.close()

# f = open('test1', 'r')
# for i in f:
#     print(i)
# f.close()

#seek
#file.seek(offset) - offset is required field - syntax

# f=open('test1','r')
# f.seek(8)
# print(f.readline())
# f.close()

#tell()
# - it returns current file position of the file
#fileobject.tell()
# f=open('test1','r')
# f.readline()
# pos=f.tell()
# f.close()
# print('position is:',pos)

# write a program to read file line by line and store it into a list?

# def file_read(fna):
#     with open(fna) as f:
#         output_list=f.readlines()
#     print(output_list)
# file_read('test1')

# copy one file's content to another file (another file automatically creates)
# from shutil import copyfile
# copyfile('test1','test2')

# str = 'cat rat mat cat pat rat cat sat cat sat'
#
# print(str)
# lst=str.split(' ')
# print(lst)
# d={}
# for i in lst:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

# count the words from the file (result: {'python': 1, 'is': 1, 'a': 1, 'oops\n': 1, 'good': 1, 'morning': 1} )
f = open('test1','r')
dic = {}
for i in f:
    var=i.split(' ')
    for j in var:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j]+= 1
print(dic)




