#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

from pyfingerprint.pyfingerprint import PyFingerprint


## Deletes a finger from sensor
##


## Tries to initialize the sensor
positionNumber = 0


def del1(positionNumber):
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        
        exit(1)
    
    
## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
##    del1(positionNumber)
## Tries to delete the template of the finger
    try:
        
        

        if ( f.deleteTemplate(positionNumber) == True ):
            print('Template deleted!')
            positionNumber = positionNumber + 1
            del1(positionNumber)
    

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
    
del1(positionNumber)
