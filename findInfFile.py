import os
import re
import sys


def search_folders(search_term):
    rex = re.compile(r'.4005.')
    for root,dirs,files in os.walk("C:\\"):
        for file in files:
            if file.endswith(".inf"):
                try:
                    thefile = open(os.path.join(root,file),"r")
                    abc = thefile.read()
                    thefile.close()
                    result = rex.search(abc)
                    if result:
                                print(os.path.join(root,file))
                except OSError as err:
                         print("OS error: {0}".format(err))
                except (OSError, IOError) as e:
                         print(e.rrno)
                         print("Can't find the file")
                except:
                         print("eror")


search_folders('4005')


