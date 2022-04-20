# This is going to be my playground for tutorials

#demo = open('C:/Users/agya_/Documents/AWS/LearnToCloud/Python/newpyfile.txt', 'r')
#demo.write('Text added using the append command')
#print(demo.read())

'''
#write string into file

with open('C:/Users/agya_/Documents/AWS/LearnToCloud/Python/demofile.txt','w') as f:
        data = 'i want to append this to the text file'
        f.write(data)
'''

'''
#read contents of file

with open('C:/Users/agya_/Documents/AWS/LearnToCloud/Python/demofile.txt','r') as x:
        reader = x.read()
print(reader)
'''

'''

#open and read file with variable assignment & read()

f = open('C:/Users/agya_/Documents/AWS/LearnToCloud/Python/demofile.txt','r')
print(f.readline())
print(f.readline())

'''


'''
#list files/sub directories with a for loop

entries = os.scandir('C:/Users/agya_/Documents/AWS/LearnToCloud/')
for entry in entries:
                print(entry)
'''

'''
#list files/sub directories with loops & .name
import os
with os.scandir('C:/Users/agya_/Documents/AWS/LearnToCloud/') as entries:
        for entry in entries:
                print(entry.name)

'''

print(range(16))