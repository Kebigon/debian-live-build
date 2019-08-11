#!/bin/bash

# Convert scan to vector PDF:
# - $1 is the PNM (PBM, PGM, PPM) or BMP input image
# - $2 is the PDF output file

mkbitmap -x -t 0.63 -s 2 -o tmp63.bmp $1
potrace -b pdf -o $2 tmp63.bmp
