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

    imdbtool -t "Ture git"
    
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
    

### Example to get ratings for all movies in current directory (it will use directory and file names as movie titles):

Save following code to file `get_ratings.sh` (make sure to update the path in line 3):

    ls -1 | 
    while read title; do
      res=`python /path/to/imdbtool.py -t "$title"`
      rating=`echo "$res" | sed -n '/imdbrating/{n;p;}'`
      restitle=`echo "$res" | sed -n '/title/{n;p;}'`
      echo "$title  *  $restitle  *  $rating"
    done

Then execute the saved command to fetch all the ratings: `./get_ratings.sh > ratings.txt`
(it'll take a while to retrieve all the data). Then you can open the `ratings.txt` file to see the movie ratings, or you can sort the movies by ratings to pick the best one to watch: `< ratings.txt sort -t* -k3 -r`
    
    
Notes
=====
 - requires Python 2.7+ (or earlier with installed argparse package)
 - for using it on Windows with Cygwin (which currently comes with Python 2.6) check out [this guide][cyg27]
 - **thanks to creator of this [great unofficial IMDb API][imdbapi]**
 
I was aware of [this existing tool][fetcher] but unfortunately it was broken at the time I tried it. My implementation relies on the third-party API that handles up to 2 million queries a day, so it's safe to assume that it's author will be keeping it up to date. If you find this tool useful make sure to [donate][imdbapi] to the API author.


[imdbapi]: http://www.imdbapi.com
[cyg27]: http://www.tux.org/~mayer/cygwin/python/index.html
[fetcher]: http://www.mutexes.org/imdb-movie-fetcher/