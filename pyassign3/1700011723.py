"""wcount.py: count words from an Internet file.

__author__ = "Jiao Yuchen"
__pkuid__  = "1700011723"
__email__  = "1700011723@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    lst1 = lines.split()
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    for i in lst1:
        i = i.lower()
        i0 = ''
        for a in i:
            if ord(a) < 97 or ord(a) > 122:
                i0 = i0
            else:
                i0 = i0 + a
        lst2.append(i0)
    st = set(lst2)
    for i in st:
        lst3.append((lst2.count(i),i))
    for (k,v) in lst3:
        lst4.append(k)
        lst4 = sorted(lst4)
        lst4 = lst4[-topn:]
    for i in lst4:
        for (k,v) in lst3:
            if i == k:
                lst5 = [(k,v)] + lst5
    for (k,v) in lst5[:topn]:
        print(v.ljust(12)+str(k))
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
