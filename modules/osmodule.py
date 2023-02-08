"""
os module : file handling purpose
used for create directory, remove directory,

platform module: use for which os we are using.

sys: system specification

math: mathematical

random :
"""
import os

#os.mkdir('D:\sample_test') - # cannot make directory in c drive
#os.rmdir('')
#os.chdir(r'C:\Users\Luminar\mypythonpro')
os.chdir(r'C:\Users\sha\Videos\sample_test')
print(os.getcwd())
#print(os.getcwd(''))



"""
chdir - changing the current work directory
import os
os.chdir("d:\\temdir")

getcwd- os model using which we can confirm if the current working directory has been changed or not.

"""