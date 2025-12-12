
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, STOPPED, FINISHED)
import numpy as np
from numpy.random import random, randint, normal, shuffle
import os
import sys


_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

expName = 'strooptest' 
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit() 

expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName


filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None, # 
    savePickle=True, saveWideText=True,
    dataFileName=filename)

win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, monitor='testMonitor', color=[0,0,0], colorSpace='hsv', # hsv 색 공간 사용
    blendMode='avg', useFBO=True)


expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

endExpNow = False
globalClock = core.Clock()
routineTimer = core.CountdownTimer()

instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text=u'Remember you choose the color of the letters, ignoring the word:\n\nred -> left\nblue -> right\ngreen -> down\nyellow -> up', # 실험 지침
    font=u'Arial',
    pos=(0, 0), height=0.1, color=u'white', colorSpace='hsv', # hsv 색 공간
    depth=0.0);

continueRoutine = True
key = event.BuilderKeyResponse()
instructionsComponents = [instrText, key]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

while continueRoutine:
    if instrText.status == NOT_STARTED:
        instrText.setAutoDraw(True)

    if key.status == NOT_STARTED:
        key.status = STARTED
        event.clearEvents(eventType='keyboard')
    if key.status == STARTED:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:
            key.keys = theseKeys[-1]
            key.rt = key.clock.getTime()
            continueRoutine = False

    if continueRoutine:
        win.flip()
    else:
        break

instrText.setAutoDraw(False)
thisExp.nextEntry()
routineTimer.reset()

trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'), 
    seed=None, name='trials')
thisExp.addLoop(trials)

trialClock = core.Clock()
target = visual.TextStim(win=win, name='target',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, color=1.0, colorSpace='hsv', opacity=1, 
    depth=0.0);

for thisTrial in trials:
    currentLoop = trials
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    continueRoutine = True
    routineTimer.add(2.200000)
    target.setColor(colour, colorSpace='hsv')
    target.setText(word)
    response = event.BuilderKeyResponse()
    trialComponents = [target, response]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    while continueRoutine and routineTimer.getTime() > 0:
        t = trialClock.getTime()
        
        if t >= 0.5 and target.status == NOT_STARTED:
            target.setAutoDraw(True)
        frameRemains = 0.5 + 1.5 - win.monitorFramePeriod * 0.75 
        if target.status == STARTED and t >= frameRemains:
            target.setAutoDraw(False)

        if t >= 0.5 and response.status == NOT_STARTED:
            response.status = STARTED
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.5 + 1.7 - win.monitorFramePeriod * 0.75 
        if response.status == STARTED and t >= frameRemains:
            response.status = STOPPED

        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'down']) 
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                response.keys = theseKeys[-1]
                response.rt = response.clock.getTime()

                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                continueRoutine = False 

        if continueRoutine:
            win.flip()

    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if response.keys in ['', [], None]:
        response.keys=None
        if str(corrAns).lower() == 'none':
           response.corr = 1
        else:
           response.corr = 0

    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:
        trials.addData('response.rt', response.rt)
    thisExp.nextEntry()

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()