# Linux

> Run man command first.
>
> -- <cite>a friend of mine</cite>

### find 

The `find` command is used to locate files and directories. 
Also you can run some specific commands for the find results.
I will show some common examples one by one that should be helpful. 

```
find .
```

This is the simplest usage of the command.
You get all the files and directories under the currect direcotry. 

```
find . -type f
```

You get all the files under the current directory. The directories are excluded from the results.
`-type` specifies the type of the files to be located. To search for regular files, supply `-type f`. For directories, `type -d`.

```
find . -type f -name '*.png'
```
You get all png files under the current directory. `-name` specifies the file name pattern.
To do a case-insensitive search, use `-iname` instead. 


```
find . -type f -name '*.log' -mtime +3 -exec rm {} \;
```

Search for .log files that are older than 3 days and remove them.
`-mtime` specifies a condition on file timestamps. And `-exec` specifies the shell command to be executed.

This looks a bit tricky, but would be useful in IT operations. You can clean out-of-date log files on a server.
Also it's a good idea to set up a cron job to clean the logs.

Watch out! Please note this kind of file operation can never be undone. Some Linux commands entail some risks.

### wc

Counts up bytes, words and newlines. 

```
cat foobar.txt | wc -l
```

This counts the number of lines of foobar.txt.


### tar

Though I've been using Linux OS for many years, I still google how to use tar. 


|extention   |compress                 |decompress           |note                                                   |
|------------|-----------------------  |---------------------|-------------------------------------------------------|
|`.tar`      |tar cvf foo.tar foo      |tar xvf foo.tar      |tar contains uncompressed bytes of the archived files. |
|`.tar.bz2`  |tar cvjf foo.tar.bz2 foo |tar xvjf foo.tar.bz2 |bzip2                                                  |
|`.tar.gz`   |tar cvzf foo.tar.gz foo  |tar xvzf foo.tar.gz  |gzip                                                   |

Each option expalined:
- c: Create an archive
- v: show the progress Verbosely
- f: File name of the archive
- x: eXtract files from an archive
