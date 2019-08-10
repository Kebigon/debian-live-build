# -*- coding: utf-8 -*-

# inspired by
# https://ankiweb.net/shared/info/1996229983

# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from aqt.reviewer import Reviewer
from aqt import mw

remap = {2:  [None, 1, 2, 2, 2],    # - nil     Again   Good   Good    Good  -  default 2-buttons: 1 = Again, 2 = Good, 3=None, 4=None
         3:  [None, 1, 2, 2, 2],    # nil     Again   Good   Good    Good - def 3-buttons: 1 = Again, 2 = Good, 3 = Easy, 4=None
         4:  [None, 1, 3, 3, 3]}    # 0=nil/none   Again Good Good Good - def 4-buttons: 1 = Again, 2 = Hard, 3 = Good, 4 = Easy

def myAnswerButtonList(self):
    l = ((1, _("Fail")),)

    cnt = self.mw.col.sched.answerButtons(self.card)

    btn_label = 'Pass'

    if cnt == 2 or cnt == 3: #i believe i did this right: we want ease 2 = good if 2 or 3 buttons
	    return l + ((2, "<div class='btn-i-ease btn-i-good'>" + btn_label + "</div>"),)
    elif cnt == 4: # b/c we want ease 3 = good in this version
        return l + ((3, "<div class='btn-i-ease btn-i-good'>" + btn_label + "</div>"),)
        
def AKR_answerCard(self, ease):
    cnt = mw.col.sched.answerButtons(mw.reviewer.card)  # Get button count

    try:
        ease = remap[cnt][ease]
    except (KeyError, IndexError):
        pass

    __oldFunc(self, ease)

__oldFunc = Reviewer._answerCard
Reviewer._answerCard =  AKR_answerCard
Reviewer._answerButtonList = myAnswerButtonList