Translate existing cheatsheets from [Cheaters](http://brettterpstra.com/2012/03/04/cheaters-customizable-cheat-sheet-system/) to navigable documentation (docset) file to use with [Dash](http://kapeli.com/dash)

![Dash open at the cheaters2docset](https://dl.dropboxusercontent.com/u/4762299/github_img/cheaters2docset/dash_cheaters.png)

---

Interestling enough, I did use the `cheaters2docset.docset` to write this README.md

---

This first release of the script essentially does:

- copy all the html file longer that 10 lines in the .docset
- add an headed and a footer (stripped fromt the index.html)
- copy the `css/` and `javascritp/` directory to the .docset
- fill the sqlite DB with cheatseets names.

You can run the `cheaters2docset.py` script, adapting all the relevant path and taking care of all the dependencies:

- multimarkdow
- Python modules:

    - sqlite3
    - glob
    - os
    - subprocess
    - BeautifulSoup (not essential, but I like prettified html code)

![Script running](https://dl.dropboxusercontent.com/u/4762299/github_img/cheaters2docset/compiling.png)

I installed everything with macports on a Mac OSX 10.7.5 

In this release I added an experimental[^fn-sample_footnote] version of the [PostgreSQL 9.0 Cheat Sheet](http://www.postgresonline.com/special_feature.php?sf_name=postgresql90_cheatsheet&amp;outputformat=html).

[^fn-sample_footnote]: **experimental**: I don't have time to properly edit this file, so use it as it is. Any help is welcome!

---

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