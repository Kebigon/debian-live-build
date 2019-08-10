# Credit goes to https://eshapard.github.io/
#
from __future__ import division
from anki.hooks import addHook
from aqt import mw
from aqt.utils import tooltip
#from aqt.utils import showInfo
import math

def easeAdjustFunc():        
    

    #Set new card ease factor
    mw.reviewer.card.factor = 2500

addHook('showQuestion', easeAdjustFunc)
addHook('showAnswer', easeAdjustFunc)