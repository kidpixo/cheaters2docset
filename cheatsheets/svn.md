Title:  Subversion Cheatsheet
CSS : css/cheaters.css

# Subversion Cheatsheet

[Permalink to Subversion Cheatsheet](http://www.cheatography.com/davechild/cheat-sheets/subversion/)
<br/>


|     Subversion Resources    ||
|  :----------  |  :---------- |
|Homepage | [http://subversion.apache.org/](http://subversion.apache.org/)|
|SVN Book | [http://svnbook.red-bean.com/](http://svnbook.red-bean.com/)|

|     Subversion Components   ||
|  :----------  |  :---------- |
| svn | Command line program |
| svnversion | Revision of working copy |
| svnlook | Inspect repository |
| svnadmin | Repository administration |
| svndumpfilter | Filter repository stream |
| mod_dav_svn | Apache module |
| svnserve | SVN server (SVN protocol) |
| svnsync | Mirror repository |

| Subversion Protocols ||
|  :----------  |  :---------- |
| file:// | Local machine |
| http:// | HTTP (Apache) |
| https:// | HTTPS (SSL) |
| svn:// | SVN (svnserve) |
| svn%2Bssh:// | SVN over SSH |

| Subversion Help ||
|  :----------  |  :---------- |
|$ svn help||
| $ svn help import Show help for "import" command
| The $ symbol is used to denote commands to be typed. ||

| Subversion Repository Administration ||
|  :----------  |  :---------- |
|$ svnadmin create "/path/to/repository"| Create new repository |
|$ svnadmin setlog "/path" -r 7 message.txt | Change log message for revision 7 to contents of file message.txt |
| $ svnadmin dump "/path/to/repository" &gt; filename | Dump repository to file (backup) |
| $ svnadmin load "/path/to/repository" &lt; filename | Load repository from file (restore) |

| Subversion Property Commands ||
|  :----------  |  :---------- |
| $ svn proplist "/path" | List properties |
| $ svn propset PROP VAL "/path" | Set PROP to VAL for path. |
| $ svn propget PROP "/path" | Get value of PROP |
| $ svn propedit PROP "/path" | Edit PROP |
| $ svn propdel PROP "/path" | Delete PROP |


| Subversion Checkout Working Copy ||
|  :----------  |  :---------- |
| $ svn checkout "/path/to/repository" | Checkout working copy into current folder |
| $ svn checkout "/path/to/repository" "/path/to/folder" | Checkout working copy into target folder |

| Subversion Update Working Copy ||
|  :----------  |  :---------- |
| $ svn update "/path" | Update path |
| $ svn update -r9 "/path" | Update path to revision 9 |


| Subversion Add Files and Folders ||
|  :----------  |  :---------- |
| $ svn add * | Add all items, recursively |
| $ svn add itemname | Add itemname (if folder, adds recursively) |
| $ svn add * --force | Force recursion into versioned directories |

| Subversion Commit Changes ||
|  :----------  |  :---------- |
| $ svn commit "/path" | Commit changes to path |
| $ svn commit -m "Message" "/path" | Commit with log message |
| $ svn commit -N "/path" | Commit without recursion |
| $ svn import "/path/to/folder" "/path" | Import and commit local folder |


| Subversion Deleting, Copying and Moving ||
|  :----------  |  :---------- |
| $ svn delete "/path" | Delete path |
| $ svn -m "Delete message" delete "/path" | Delete with log message |
| $ svn copy "/source" "/target" | Copy source to target |
| $ svn move "/source" "/target" | Move source to target |

| Subversion Logs and Blame ||
|  :----------  |  :---------- |
| $ svn log "/path" | Show log messages for path |
| $ svn blame "/path" | Show commits for path |

| Subversion Revert Changes ||
|  :----------  |  :---------- |
| $ svn revert "/path" | Revert changes to path |
| $ svn revert -R "/path" | Revert changes recursively |

| Subversion Differences Between Files |
|  :----------  | 
|$ svn diff "/path/file"|
|$ svn diff "/path/file@2" "/path/file@7"|
|$ svn diff -r 2:7 "/path/folder"|

| Subversion Merge Changes ||
|  :----------  |  :---------- |
| $ svn merge -r2:7 "item" "/path" | Apply diff between revisions 2 and 7 of "item" to path |
| $ svn merge "url1" "url2" "/path" | Apply diff between "url1" and "url2" to path |


| Subversion Miscellaneous Commands ||
|  :----------  |  :---------- |
| $ svn resolve "/path" | Resolve conflict |
| $ svn cleanup "/path" | Remove locks and complete operations |
| $ svn lock "/path" | Lock path |
| $ svn unlock "/path" | Unlock path |
| $ svn status "/path" | Get path status |
| $ svn cat "/path" | View file contents |


| Subversion Item and Property Statuses ||
|  :----------  |  :---------- |
||No modifications (blank)|
| A | Addition |
| D | Deletion |
| M | Modified |
| R | Item replaced |
| C | In conflict |
| X | Externals definition |
| I | Ignored |
| ? | Not in repository |
| ! | Item missing |
| ~ | Object type changed |


| Subversion Argument Shortcuts ||
|  :----------  |  :---------- |
| -m "Message" | \--message |
| -q | \--quiet |
| -v | \--verbose |
| -r | \--revision |
| -c | \--change |
| -t | \--transaction |
| -R | \--recursive |
| -N |\--non-recursive  |
