*NIX command line tool for retrieving IMDb movie information
============================================================

### Usage:

First set up an alias for the command:

    alias imdbtool="python /path/to/imdbtool.py"

### Some interesting usage examples:

Show all info about movie 'Cars'

    imdbtool -t Cars

Show all info about latest 'True Grit' movie

    imdbtool -t "True Grit"
    
Show all info about 1969 version of 'True Grit'

    imdbtool -t "True Grit" -y 1969
    
Show best guess for a misspelled name

    imdbtool -t "Ture Git"
    
Print movie's rating

    imdbtool -t Cars | sed -n '/imdbrating/{n;p;}'
    
Download movie's poster

    imdbtool -t Cars | wget `sed -n '/poster/{n;p;}'`

    
### Additional useful features:

Include full plot summary (not available for some movies)

    imdbtool -t "True Grit" --plot full
    
Include additional data from Rotten Tomatoes

    imdbtool -t "True Grit" --tomatoes

Show info by IMDb id

    imdbtool -i tt0103064
    
Print raw JSON or XML data

    imdbtool -t Cars -r JSON
    
    
Notes
=====
 - requires Python 2.7+ (or earlier with installed argparse package)
 - for using it on Windows with Cygwin (which currently comes with Python 2.6) check out [this guide][cyg27]
 - **thanks to creator of this [great unofficial IMDb API][imdbapi]**
 
I was aware of [this existing tool][fetcher] but unfortunately it was broken at the time I tried it. My implementation relies on the third-party API that handles up to 2 million queries a day, so it's safe to assume that it's author will be keeping it up to date. If you find this tool useful make sure to [donate][imdbapi] to the API author.


[imdbapi]: http://www.imdbapi.com
[cyg27]: http://www.tux.org/~mayer/cygwin/python/index.html
[fetcher]: http://www.mutexes.org/imdb-movie-fetcher/