Translate existing cheatsheets from [Cheaters](http://brettterpstra.com/2012/03/04/cheaters-customizable-cheat-sheet-system/) to navigable documentation (docset) file to use with [Dash](http://kapeli.com/dash)

Still writing the code, the idea is:

1. Feed the python script with your Cheaters' cheatsheets path like `/Users/YOUR_USER/cheaters/cheatsheets`
2. The script take existing html file and put them in the sqlite DB (docSet.dsidx)
3. (optional) the script translate all the Markdown file to html and put them in the sqlite DB (docSet.dsidx)
4. Once installed in Dash, search in the box to select a language + space + search in the language sheet


All the non-text cheatsheets  (html,md,mmd and so on) will be ignored.