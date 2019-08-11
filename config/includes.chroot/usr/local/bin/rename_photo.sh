#!/bin/bash

# Rename photo from the exif timestamp
jhead -n%y%m%d-%H%M%S $@
