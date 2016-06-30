"""AlayaNotes

Usage:
  main.py [run]
  main.py initdb
"""
from docopt import docopt
from alayatodo import app, db
from alayatodo.models import initdb

if __name__ == '__main__':
    args = docopt(__doc__)
    if args['initdb']:
        initdb()
    else:
        app.run(use_reloader=True)
