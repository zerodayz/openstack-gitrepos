#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

find $DIR -type d -depth 1 -exec git --git-dir={}/.git --work-tree=$PWD/{} pull \;
