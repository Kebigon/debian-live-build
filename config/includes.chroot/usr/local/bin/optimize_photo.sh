#!/bin/bash

# 12441600 pixels corresponds to a 8 by 12 inches photo printed at 360ppi

mogrify                               \
	-sampling-factor 4:2:0        \
	-auto-orient                  \
	-strip                        \
	-resize '12441600@>'          \
	-quality 85                   \
	-interlace JPEG               \
	-define jpeg:dct-method=float \
	-colorspace sRGB              \
	$@
