#!/bin/bash

find . -maxdepth 1 -type d -print -exec git --git-dir={}/.git --work-tree=$PWD/{} pull \;
