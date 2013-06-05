import sqlite3 as lite
import glob
import os
import subprocess
import BeautifulSoup

# import tidylib
# import urllib

###################################
# CUSTOMIZE THIS PATH : POINT IT TO 
# THE DIRECTORY CONTAINING cheaters

cheaters_path = '../cheaters/' # accepts relative path

#
#
###################################                 
doc_path =  os.path.dirname(os.path.abspath(__file__))+'/cheaters2docset.docset/Contents/Resources/Documents/'
db_path  =  os.path.dirname(os.path.abspath(__file__))+'/cheaters2docset.docset/Contents/Resources/docSet.dsidx'

head_first ='<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">'

def htmltitle(title):
    return '<title>'+title+'</title>'

head_second='<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<link rel="stylesheet" href="css/cheaters.css">\n</head>\n<body class="normal">\n<script src="javascripts/jquery.min.js"></script>\n<script src="javascripts/smooth_scrolling.lopash.js"></script>\n<script src="javascripts/highlight.pack.js"></script>'

foot ='<script>hljs.initHighlightingOnLoad();</script>\n</body>\n</html>'

# create an index from the github README.md - requires multimarkdown installed!
b = os.system('multimarkdown '+cheaters_path+'README.md > '+doc_path+'index.html')

###################################                 
# copy the CSS
b = os.system('cp -R '+cheaters_path+'css/ '+doc_path+'css/')
# backup original css file
b = os.system('cp -R '+doc_path+'css/cheaters.css '+doc_path+'css/cheaters_back.css ')
# copy custom css files
b = os.system('cp css/* '+doc_path+'css/ ')

###################################                 
#copy the local javascript directory
b = os.system('cp -R javascripts/ '+doc_path+'javascripts/')


###################################                 
# file length check using subprocess and `wc -l`
def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

# html in cheaters directory listed
filelist = glob.glob(cheaters_path+'cheatsheets/*.html')

#connect to the sqlite db
con = lite.connect(db_path)
cur = con.cursor()    
#erase all
cur.execute('DELETE FROM searchIndex')

#insert the file in the filelist and beautify the html file
for file in filelist:
    if file_len(file) > 10 :
        filename_ext = os.path.basename(file)
        filename=os.path.splitext(filename_ext)[0]
        soup = BeautifulSoup.BeautifulSoup(open(file))
        #re-write the html prettifyied file
        f = open(doc_path+filename_ext, "w")
        f.write(head_first)
        f.write(htmltitle(filename))
        f.write(head_second)
        f.write(soup.prettify())
        f.write(foot)
        f.close()
        cur.execute("INSERT INTO searchIndex (path,type,name) VALUES (?,'Guide',?)",(filename_ext,filename))
        print 'written > '+filename

# Markdown files in local cheatsheets/ directory
filelist_local = glob.glob(os.path.dirname(os.path.abspath(__file__))+'/cheatsheets/*.md')

#insert the file in the filelist and beautify the html file
for file in filelist_local:
    filename_ext = os.path.basename(file)
    filename=os.path.splitext(filename_ext)[0]
    b = os.system('multimarkdown '+file+' > '+doc_path+filename+'.html')
    cur.execute("INSERT INTO searchIndex (path,type,name) VALUES (?,'Guide',?)",(filename+'.html',filename))
    print 'converted MD file > '+filename

#commit the DB changes
con.commit()
#close the DB
con.close()

b = os.system("tar --exclude='.DS_Store' -czf cheaters2docset.tgz cheaters2docset.docset")
print 'compress to '+os.path.dirname(os.path.abspath(__file__))+'/cheaters2docset.tgz'
