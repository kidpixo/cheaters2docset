## What it does?

Translate existing cheatsheets from [Cheaters](http://brettterpstra.com/2012/03/04/cheaters-customizable-cheat-sheet-system/) to navigable documentation (docset) file to use with [Dash](http://kapeli.com/dash)

![Dash open at the cheaters2docset](https://dl.dropboxusercontent.com/u/4762299/github_img/cheaters2docset/dash_cheaters.png)

## Cheatsheet included

All cheatsheets available in Brett's [Cheaters](http://brettterpstra.com/2012/03/04/cheaters-customizable-cheat-sheet-system/)

- JSStrings
- alfred
- bashhistory
- emmet
- git-advanced
- git
- gmail
- html5
- index
- javascripts
- jira
- jquery
- keybindings
- markdown
- mmd
- patternsregex
- rst ([cheaters pull request #11](http://github.com/ttscoff/cheaters/pull/11))
- scapple
- screen
- selectors
- siri
- subl
- subl2
- tmux
- towergithtml ([cheaters pull request #10](http://github.com/ttscoff/cheaters/pull/10))
- trickster
- vim

A couple cheatsheets I did:

- postgresql90.md ([gist link](https://gist.github.com/kidpixo/5618697))
- postgis2.0.md ([gist link](https://gist.github.com/kidpixo/5698476))
- svn.md ([gist link](https://gist.github.com/kidpixo/5699219))

I'm happy to have contribution on cheatsheets translation, markdown preferred, but html is accepted too.



## How to to : Short Version

1. clone/download the repository
- add the `cheaters2docset.docset`
- enjoy it!

## How to to : Long Version

Interesting enough, I actually use the `cheaters2docset.docset` to write this README.md

This release essentially does:

- copy all the html file longer that 10 lines in the .docset ( I assume here that > 10 means actual HTML, not just reference to an image. I might be wrong!)
- add an headed and a footer (stripped fromt the index.html)
- copy the `css/` and `javascritp/` directory to the .docset
- fill the sqlite DB with cheatseets names.
    - convert the markdown cheatshet in the local cheatsheet/ directory to html
    - fill the sqlite DB with markdown-cheatsheets names.

You can run the `cheaters2docset.py` script, adapting all the path in the the python script with your Cheaters' cheatsheets path like 

    cheaters_path = /Users/YOUR_USER/cheaters/cheatsheets

 and taking care of all the dependencies:

- multimarkdow (needed to translate markdown files)

- Python modules (needed to move file,parse it and a lot of stuff) :

    - sqlite3
    - glob
    - os
    - subprocess
    - BeautifulSoup (not essential, but I like prettified html code)

![Script running](https://dl.dropboxusercontent.com/u/4762299/github_img/cheaters2docset/compiling.png)

I installed everything with macports on a Mac OSX 10.7.5 and on 10.8.2, works fine. 

In this release I added an experimental* version of the [PostgreSQL 9.0 Cheat Sheet](http://www.postgresonline.com/special_feature.php?sf_name=postgresql90_cheatsheet&amp;outputformat=html)
and [PostGIS 2.0 Basic geometry/geography](http://www.postgis.us/downloads/postgis20_cheatsheet.html).

<br/>
* **experimental**: I don't have time to properly edit this file, so use it as it is. Any help is welcome!

