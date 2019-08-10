# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

"""MattVsJapan Anki Reset Ease script

See: https://www.youtube.com/user/MATTvsJapan

Description:
    Some people (including me) found the updated red-pill ease values weren't
    getting pushed from desktop to AnkiWeb without forcing a one-way sync so
    this version of the script can remove the need to check "Settings >
    Network > On next sync..." every time. Enable this in the config below.

    Alternatively, just use it to sync automatically before and after ease
    reset to save a few clicks or keystrokes per day :)

Usage:
    1. Sync your other devices with AnkiWeb
    2. Run this script from Tools -> Reset Ease...
    3. If the force_after config option is set below, click "Upload to
       AnkiWeb" on Anki's sync dialog (your other devices can download on 
       next sync)

Config option combinations (set them below):

1. Normal sync before and after reset
    * Set sync_before_reset and sync_after_reset to True

2. Force sync in one direction after reset
    * Set sync_after_reset and force_after to True
    * Might as well set sync_before_reset to True as well

3. Seen the reset ease dialog enough times?
    Set skip_reset_notification to True

4. Same as the original script (no sync)
    * Set all four options to False
"""


######################################################################
# Configuration
######################################################################

sync_before_reset = False
sync_after_reset = True
force_after = True
skip_reset_notification = False

######################################################################
# End configuration
######################################################################


ezFactor = 2500
ezFactor2 = ezFactor/10

def ResetEase():
    # sync before resetting ease if enabled
    if sync_before_reset:
        mw.onSync()

    # reset ease
    mw.col.db.execute("update cards set factor = ?", ezFactor)
    # show a message box
    if not skip_reset_notification:
        showInfo("Ease has been reset to " + str(ezFactor2) + "%.")

    # sync after resetting ease if enabled
    if sync_after_reset:
        # force a one-way sync if enabled
        if force_after:
            mw.col.scm += 1
            mw.col.setMod()
        mw.onSync()


# format menu item based on configuration
menu_label = 'Reset Ease{}{}'.format(
        ' + Sync Before' if sync_before_reset else '',
        (' + {}Sync After' if sync_after_reset else '').format(
            'Force ' if force_after else ''))

# create a new menu item
action = QAction(menu_label, mw)
# set it to call testFunction when it's clicked
action.triggered.connect(ResetEase)
# and add it to the tools menu
mw.form.menuTools.addAction(action)

