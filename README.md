To translate an existing IDLdoc (<http://idldoc.idldev.com/>) documentation follow this steps: 

1. build the directories structure as described in <http://kapeli.com/docsets/> or use the empty `IDLdoc` structure here. 
2. copy your documentation in `IDLdoc/Contents/Resources/Documents/ `
3. run the `IDLdoc_docset_creation.py` in the `IDLdoc/Contents/Resources/` directory 
4. Change the `IDLdoc` name to `IDLdoc.docset`
5. Create `~/Library/Application Support/Dash/DocSets/IDLdoc/` and put yout docset there.

Optional : 
4.1 change the `IDLdoc/icon.png` 
4.2 adjust the `IDLdoc/Contents/nfo.plist` to change the docset name,shortcuts etc, then change all the name (IDLdoc to YourDoc_whatever).

The python code does the following: 
- scans only 2 level deep in the Documents folder 
- deletes some files (`all-dirs.html`,`all-files.html` etc) 
- sets as start page the `dir-overview.html` changing it to `index.html`
- gets the title from each html page 
- modifies the html erasing the top banner 
- writes all in the sqlite DB `docSet.dsidx` 

In order to run properly you need to have the sqlite3,urllib,BeautifulSoup and glob modules along your python distribution. 
