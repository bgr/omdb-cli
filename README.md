*NIX command line and GUI tool for retrieving OMDb movie/TV information
============================================================

### Usage:

First set up an alias for the command:

    alias omdbtool="python /path/to/omdbtool.py"

Or for the gui:

    alias omdbtool="python /path/to/omdbtool-gui.py"

Note: in order to use the gui you will need to install [Gooey][gooey]

    pip install Gooey

### Some interesting usage examples:

Show all info about the movie 'Cars'

    omdbtool -t Cars

Show all info about the series 'Firefly'

    omdbtool -t firefly --type series

Show all info about season 1 episode 1 of 'Firefly'

    omdbtool -t firefly --season 1 --episode 1

Show all info about season 1 of 'Firefly'

    omdbtool -r JSON -t firefly --season 1

Show all info about latest 'True Grit' movie

    omdbtool -t "True Grit"

Show all info about 1969 version of 'True Grit'

    omdbtool -t "True Grit" -y 1969

Show best guess for a misspelled name

    omdbtool -t "Ture git"

Print movie's rating

    omdbtool -t Cars | sed -n '/^imdbrating/{n;p;}'

Download movie's poster

    omdbtool -t Cars | wget `sed -n '/^poster/{n;p;}'`


### Additional useful features:

Include full plot summary (not available for some movies)

    omdbtool -t "True Grit" --plot full

Include additional data from Rotten Tomatoes

    omdbtool -t "True Grit" --tomatoes

Show info by IMDb id

    omdbtool -i tt0103064

Print raw JSON or XML data

    omdbtool -t Cars -r JSON

Print data formated as html

    omdbtool --format html -t cars

Print data formated as markdown

    omdbtool --format markdown -t cars



### Example to get ratings for all movies in current directory

(it will use directory and file names as movie titles)

Save following code to file `get_ratings.sh` (make sure to update the path in line 3):

    ls -1 |
    while read title; do
      res=`python /path/to/omdbtool.py -t "$title"`
      rating=`echo "$res" | sed -n '/^imdbrating/{n;p;}'`
      restitle=`echo "$res" | sed -n '/^title/{n;p;}' | sed s/*//g`
      year=`echo "$res" | sed -n '/^year/{n;p;}'`
      echo "$title  *  $restitle  *  $year  *  $rating"
    done

Then execute the saved command to fetch all the ratings: `./get_ratings.sh > ratings.txt`
(it'll take a while to retrieve all the data). Then you can open the `ratings.txt` file to see the movie ratings, or you can sort the movies by ratings to pick the best one to watch: `< ratings.txt sort -t* -k4 -r`


## Notes ##

 - works with Python 3 and Python 2.7 or earlier with argparse package installed
 - **thanks to the creator of this [great site called OMDBAPI][omdbapi]**


## License ##

This tool is licensed under [GNU Lesser GPL][lgpl] license.


[omdbapi]: http://www.omdbapi.com
[lgpl]: http://www.gnu.org/licenses/lgpl.html
[gooey]: https://github.com/chriskiehl/Gooey
