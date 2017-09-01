#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python $DIR/generate-repos.py

for p in $(cat "$DIR/gitrepos"); \
      do git clone $p; done
