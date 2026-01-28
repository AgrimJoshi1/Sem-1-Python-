import os 
if os.path.exists('file1.txt'):
    print('file exists')
else:
    print("no")

print(os.path.isfile('Chitkara'))

#os module to work on directories
# Exists to find folder or file
# Path.isfile() to find only file
#mkdir() make a new directary or we can say make a new file
#chdir() make a change 
#os.rmdir() remove directary
#getcqwd() to tell which directary is being used
#listdr() jitna bhi sara work hai voh show hou jaye gah
