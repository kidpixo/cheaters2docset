import sqlite3 as lite
import glob
import BeautifulSoup
import tidylib

# import urllib
# import os

#document to erase
# deletelist =[ "./Documents/all-dirs.html","./Documents/all-files.html","./Documents/idldoc-index.html","./Documents/index.html","./Documents/search.html","./Documents/categories.html","./Documents/dir-files.html" ,"./Documents/libdata.js"]+glob.glob('./Documents/*/dir-overview.html')
# for f in deletelist:
#     os.remove(f)

# os.rename("./Documents/dir-overview.html", "./Documents/index.html")

# html in cheaters directory listed
filelist = glob.glob('/Users/damo_ma/Downloads/github_rep/cheaters/cheatsheets/*.html')

# #connect to the sqlite db
# con = lite.connect('./cheaters2docset/Contents/Resources/docSet.dsidx')
# cur = con.cursor()    
# #erase all
# cur.execute('DELETE FROM searchIndex')

#insert the file in the filelist and beautify the html file
for file in filelist:
    #get the soup ready...
    soup = BeautifulSoup.BeautifulSoup(open(file))
    #skipping the source code
    
    print title.title(),file.lstrip('./Documents/')
    #insert in the DB    
    cur.execute("INSERT INTO searchIndex (path,type,name) VALUES (?,'func',?)",(file.lstrip('./Documents/'),title.title()),verbose=1)
    
# #delete the directories entry
# cur.execute('DELETE FROM searchIndex WHERE name LIKE "%\%"')
# 
# #commit the DB changes
# con.commit()