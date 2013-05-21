Translate existing cheatsheets from [Cheaters](http://brettterpstra.com/2012/03/04/cheaters-customizable-cheat-sheet-system/) to navigable documentation (docset) file to use with [Dash](http://kapeli.com/dash)

Still writing the code, the idea is:

1. Feed the python script with your Cheaters' cheatsheets path like `/Users/YOUR_USER/cheaters/cheatsheets`

- The script takes existing html files and put them in the sqlite DB (docSet.dsidx)
- (optional) The script translates all the Markdown files to html (with YOUR css!!) and put them in the sqlite DB (docSet.dsidx)
- Install the resulting docset in Dash
    - rename the directory as `cheaters2docset.docset`
    - move it to `/Users/YOUR_USER/Library/Application Support/Dash/DocSets`
- Invoke Dash and search in the box to select a language + space + search in the language sheet
- Enjoy.


All the non-text cheatsheets (html,md,mmd and so on) will be ignored for now: if you have better idea, I'm listening.