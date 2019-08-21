#!/bin/bash

# Check tools availability
command -v jhead >/dev/null 2>&1 || { echo "Please install jhead"; exit 1; }

# Rename photo from the exif timestamp
jhead -n%y%m%d-%H%M%S $@
