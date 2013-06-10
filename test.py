import sqlite3 as lite
import glob
import os
import subprocess
import BeautifulSoup
import shutil

base_path = os.path.dirname(os.path.abspath(__file__))+'/TextWrangler2docset.docset/Contents/Resources'

# absolute path for interactive use
# base_path = '/Users/damo_ma/Downloads/github_cloned/TextWrangler2docset/TextWrangler2docset.docset/Contents/Resources'

source_dir = '/Applications/TextWrangler.app/Contents/Resources/TextWrangler Help/'

doc_path =  base_path+'/Documents/'
db_path  =  base_path+'/docSet.dsidx'

shutil.rmtree(doc_path)

print(source_dir,doc_path)
shutil.copytree(source_dir, doc_path) 

###########################
# document to erase
###########################

deletelist = glob.glob(doc_path+'*_side*')+glob.glob(doc_path+'*index_*')

for f in deletelist:
    if os.path.isfile(f):
       os.remove(f)

# 2 directory level down listed
filelist = glob.glob(doc_path+'*.htm*')+glob.glob(doc_path+'*/*.htm*')

#connect to the sqlite db
con = lite.connect(db_path)
cur = con.cursor()    
#erase all
cur.execute('DELETE FROM searchIndex')

#insert the file in the filelist and beautify the html file
for file in filelist:
    name = os.path.split(file)[1].split('.')[0]
    #get the soup ready...
    soup = BeautifulSoup.BeautifulSoup(open(file))
    if len(soup.findAll('frame')) == 0 :
        #skipping the source code
        title = soup.title.string
        print 'FILENAME : '+file#+os.path.split(file)[1]
        print "Title : "+title.title(),"  |  Filename  : "+name
        cur.execute("INSERT INTO searchIndex (path,type,name) VALUES (?,'Guide',?)",(file,name))
    else :
        os.remove(file)
 
#delete the directories entry
cur.execute('DELETE FROM searchIndex WHERE name LIKE "%\%"')

#commit the DB changes
con.commit()