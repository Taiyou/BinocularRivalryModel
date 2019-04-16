#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Tue Jan 30 11:45:59 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'PseudoRivalry'  # from the Builder filename that created this script
# expInfo = {'participant':'', 'session':'001'}
# dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
# if dlg.OK == False:
#     core.quit()  # user pressed cancel
expInfo = {}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['audioDevice'] = u'Bult-in Output'

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
# filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=False)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(2560, 1440), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "choice"
choiceClock = core.Clock()
prompt = visual.TextStim(win=win, name='prompt',
    text=u'Enter a code',
    font=u'Arial',
    pos=(-0.9, 0.95), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "calib"
calibClock = core.Clock()
imageCalib = visual.ImageStim(
    win=win, name='imageCalib',
    image=u'src/Calibration.png', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rivalry"
rivalryClock = core.Clock()
imageRivalry = visual.ImageStim(
    win=win, name='imageRivalry',
    image=u'src/Gabor_Standard_Rivalry.png', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "pseudo"
pseudoClock = core.Clock()
moviePseudo1 = visual.MovieStim3(
    win=win, name='moviePseudo',
    noAudio = True,
    filename=u'src/8state_trand_noise_1.mp4',
    ori=0, pos=(0, 0), opacity=1,
    size=(1.8, 1.8),
    depth=0.0,
    units='norm',
    )
moviePseudo2 = visual.MovieStim3(
    win=win, name='moviePseudo',
    noAudio = True,
    filename=u'src/8state_trand_noise_2.mp4',
    ori=0, pos=(0, 0), opacity=1,
    size=(1.8, 1.8),
    depth=0.0,
    units='norm',
    )
moviePseudo3 = visual.MovieStim3(
    win=win, name='moviePseudo',
    noAudio = True,
    filename=u'src/8state_trand_noise_3.mp4',
    ori=0, pos=(0, 0), opacity=1,
    size=(1.8, 1.8),
    depth=0.0,
    units='norm',
    )
moviePseudo4 = visual.MovieStim3(
    win=win, name='moviePseudo',
    noAudio = True,
    filename=u'src/8state_trand_noise_4.mp4',
    ori=0, pos=(0, 0), opacity=1,
    size=(1.8, 1.8),
    depth=0.0,
    units='norm',
    )
moviePseudo5 = visual.MovieStim3(
    win=win, name='moviePseudo',
    noAudio = True,
    filename=u'src/8state_trand_noise_5.mp4',
    ori=0, pos=(0, 0), opacity=1,
    size=(1.8, 1.8),
    depth=0.0,
    units='norm',
    )

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# set up handler to look after randomisation of conditions etc
trial_loop = data.TrialHandler(nReps=9999, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_loop')
thisExp.addLoop(trial_loop)  # add the loop to the experiment
thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
if thisTrial_loop != None:
    for paramName in thisTrial_loop.keys():
        exec(paramName + '= thisTrial_loop.' + paramName)


#
# Trial loop
#
for thisTrial_loop in trial_loop:
    currentLoop = trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop.keys():
            exec(paramName + '= thisTrial_loop.' + paramName)

    # ------Prepare to start Routine "choice"-------
    t = 0
    choiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_choice = event.BuilderKeyResponse()
    # keep track of which components have finished
    choiceComponents = [key_choice, prompt]
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "choice"-------
    while continueRoutine:
        # get current time
        t = choiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *key_choice* updates
        if t >= 0.0 and key_choice.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_choice.tStart = t
            key_choice.frameNStart = frameN  # exact frame index
            key_choice.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_choice.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_choice.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'r', '1', '2', '3', '4', '5'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_choice.keys = theseKeys[-1]  # just the last key pressed
                key_choice.rt = key_choice.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # *prompt* updates
        if t >= 0.0 and prompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            prompt.tStart = t
            prompt.frameNStart = frameN  # exact frame index
            prompt.setAutoDraw(True)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_choice.keys in ['', [], None]:  # No response was made
        key_choice.keys=None
    trial_loop.addData('key_choice.keys',key_choice.keys)
    if key_choice.keys != None:  # we had a response
        trial_loop.addData('key_choice.rt', key_choice.rt)
    # the Routine "choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()


    #
    # Calibration
    #
    if key_choice.keys == 'c':
        # ------Prepare to start Routine "calib"-------
        t = 0
        calibClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        calibComponents = [imageCalib]
        for thisComponent in calibComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "calib"-------
        while continueRoutine:
            # get current time
            t = calibClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *imageCalib* updates
            if t >= 0.0 and imageCalib.status == NOT_STARTED:
                # keep track of start time/frame for later
                imageCalib.tStart = t
                imageCalib.frameNStart = frameN  # exact frame index
                imageCalib.setAutoDraw(True)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in calibComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for forced trial end
            if event.getKeys(keyList="space"):
                continueRoutine = False
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "calib"-------
        for thisComponent in calibComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "calib" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()


    #
    # Rivalry
    #
    if key_choice.keys == 'r':
        # ------Prepare to start Routine "rivalry"-------
        t = 0
        rivalryClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        rivalryComponents = [imageRivalry]
        for thisComponent in rivalryComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "rivalry"-------
        while continueRoutine:
            # get current time
            t = rivalryClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *imageRivalry* updates
            if t >= 0.0 and imageRivalry.status == NOT_STARTED:
                # keep track of start time/frame for later
                imageRivalry.tStart = t
                imageRivalry.frameNStart = frameN  # exact frame index
                imageRivalry.setAutoDraw(True)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rivalryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for forced trial end
            if event.getKeys(keyList="space"):
                continueRoutine = False
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "rivalry"-------
        for thisComponent in rivalryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "rivalry" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()


    #
    # Movie loop
    #
    if key_choice.keys.isdigit():
        
        # Get a chosen movie object
        moviePseudo = eval("moviePseudo" + key_choice.keys)
        
        # ------Prepare to start Routine "pseudo"-------
        t = 0
        pseudoClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        pseudoComponents = [moviePseudo]
        for thisComponent in pseudoComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "pseudo"-------
        while continueRoutine:
            # get current time
            t = pseudoClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *moviePseudo* updates
            if t >= 0.0 and moviePseudo.status == NOT_STARTED:
                # keep track of start time/frame for later
                moviePseudo.tStart = t
                moviePseudo.frameNStart = frameN  # exact frame index
                moviePseudo.setAutoDraw(True)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pseudoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for forced trial end
            if event.getKeys(keyList="space"):
                continueRoutine = False
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # Replay
            if moviePseudo.getCurrentFrameTime() >= moviePseudo.duration-.05:
                moviePseudo.seek(0.01) #'seek' and 'play' have interesting interactions w/r/t audio. 
                moviePseudo.draw() # Comment this out to blank between loops.

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "pseudo"-------
        for thisComponent in pseudoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "pseudo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    thisExp.nextEntry()


# these shouldn't be strictly necessary (should auto-save)
# thisExp.saveAsWideText(filename+'.csv')
# thisExp.saveAsPickle(filename)
# logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
