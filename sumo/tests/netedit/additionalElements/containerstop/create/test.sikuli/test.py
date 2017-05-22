#!/usr/bin/env python
"""
@file    test.py
@author  Pablo Alvarez Lopez
@date    2016-11-25
@version $Id$

python script used by sikulix for testing netedit

SUMO, Simulation of Urban MObility; see http://sumo.dlr.de/
Copyright (C) 2009-2017 DLR/TS, Germany

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""
# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# go to additional mode
netedit.additionalMode()

# select containerStop
netedit.changeAdditional("containerStop")

# set name
netedit.modifyAdditionalDefaultValue(2, "containerStop")

# Add three extra lines
netedit.modifyStoppingPlaceLines(4, 3)

# fill extra lines
netedit.fillStoppingPlaceLines(3, 4)

# remove last line (line 4)
netedit.modifyStoppingPlaceLines(8, 1)

# create containerStop in mode "reference left"
netedit.leftClick(match, 250, 250)

# change reference to right
netedit.modifyAdditionalDefaultValue(9, "reference right")

# create containerStop in mode "reference right"
netedit.leftClick(match, 240, 250)

# change reference to center
netedit.modifyAdditionalDefaultValue(9, "reference center")

# create containerStop in mode "reference center"
netedit.leftClick(match, 425, 250)

# return to mode "reference left"
netedit.modifyAdditionalDefaultValue(9, "reference left")

# Change length
netedit.modifyAdditionalDefaultValue(11, "30")

# try to create a containerStop in mode "reference left" (Warning)
netedit.leftClick(match, 500, 250)

# change reference to right
netedit.modifyAdditionalDefaultValue(9, "reference right")

# try containerStop in mode "reference right" (Warning)
netedit.leftClick(match, 110, 250)

# enable force position
netedit.modifyAdditionalDefaultBoolValue(12)

# change reference to "reference left"
netedit.modifyAdditionalDefaultValue(9, "reference left")

# create a containerStop in mode "reference left" forcing poisition
netedit.leftClick(match, 500, 250)

# change reference to "reference right"
netedit.modifyAdditionalDefaultValue(9, "reference right")

# create a containerStop in mode "reference right" forcing position
netedit.leftClick(match, 110, 250)

# Check undo redo
netedit.undo(match, 5)
netedit.redo(match, 5)

# save additionals
netedit.saveAdditionals()

# save newtork
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
