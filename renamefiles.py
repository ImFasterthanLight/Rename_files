import os
import re
def listToString(s):

    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))



removal = ['Audio','Eng','BD','HEVC','Sub','Dual','720p','1080p','480p']

os.chdir(os.path.dirname(os.path.abspath(__file__)))
paths=os.getcwd()
print(paths)
entries = os.listdir(paths)

for entry in entries:
        res = re.findall(r'\[.*?\]', entry)
        removal.extend(res)
        print(removal)
        removal = list(set(removal))

for entry in entries:
        entry1=entry.split( )
        if len(entry1)!=1:
            entry1 = [ele for ele in entry1 if ele not in removal]

        lastrename=listToString(entry1)
        print(lastrename)
        os.rename(entry, lastrename )
