#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import pandas as pd
import sys
import time as tm
import datetime
import os
from pathlib import Path
i=0
now=datetime.datetime.now()
time=now.time()
wdate=now.date()
day=wdate.day
month=wdate.month
year=wdate.year
date=str(day)+str(month)+str(year)
print(date)
print(time)
today=wdate.day
filename = r"hostel.csv"
print(today)
if(time.hour>=7 and time.hour<11):
    filet=Path('temptiffin'+str(today)+'.csv')
    if (filet.is_file()==False):
        pd.read_csv(filename).to_csv(r'temptiffin'+str(today)+'.csv',index=False)
    df1=pd.read_csv('temptiffin'+str(today)+'.csv')
elif(time.hour>=12 and time.hour<=15):
    filel=Path('templunch'+str(today)+'.csv')
    if (filel.is_file()==False):
        pd.read_csv(filename).to_csv(r'templunch'+str(today)+'.csv',index=False)
    df2=pd.read_csv('templunch'+str(today)+'.csv')
elif(time.hour>=19  and time.hour<22):
    filed=Path('tempdinner'+str(today)+'.csv')
    print("syktmh")
    if (filed.is_file()==False):
        print("done")
        pd.read_csv(filename).to_csv(r'tempdinner'+str(today)+'.csv',index=False)
    df3=pd.read_csv('tempdinner'+str(today)+'.csv')
## Search for a finger
##

## Tries to initialize the sensor
while(True):
        print("if")
        g=open('text','r')
        bit=g.read()
        if(bit=="0"):
            print("yes")
            try:
                    
                f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

                if ( f.verifyPassword() == False ):
                    raise ValueError('The given fingerprint sensor password is wrong!')

            except Exception as e:
                print('The fingerprint sensor could not be initialized!')
                print('Exception message: ' + str(e))

            ## Gets some sensor information
                print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

            ## Tries to search the finger and calculate hash
            try:
                print('Waiting for finger...')

            ## Wait that finger is read
                while ( f.readImage() == False ):
                    if(bit=="0"):
                        print("hehe")
                        break
                    pass

                ## Converts read image to characteristics and stores it in charbuffer 1
                f.convertImage(0x01)

                ## Searchs template
                result = f.searchTemplate()

                positionNumber = result[0]
                accuracyScore = result[1]

                if ( positionNumber == -1 ):
                    print('No match found!')
                    
                else:
                    print('Found template at position #' +str(positionNumber)) 
                    print('The accuracy score is: ' + str(accuracyScore))
                    if(time.hour>=7 and time.hour<11):
                        print("entered 1")
                        if(((df1.fingerid==positionNumber).any())==True):
                            print("entered 2")
                            df=pd.read_csv('tiffin.csv')
                            if date not in df.columns:
                                print("also")
                                df.set_value(0,date,str(positionNumber))
                                os.system('lpr -o fit-to-page /home/pi/Desktop/python3-fingerprint/examples/application/breakfast')
                                df.to_csv("tiffin.csv",encoding="utf-8",index=False)
                                print("successful")
                            print("eneter")
                            if(((df[date] == positionNumber).any())==False):
                                print("tiffin success")
                                x=df[date].count()
                                print(x)
                                print("success")
                                print(df)
                               ## df.loc[x,wdate] = str(positionNumber)
                                print('sucess')
                                df.set_value(int(x),date,str(positionNumber))
                                os.system('lpr -o fit-to-page /home/pi/Desktop/new \n')
                                print('done')
                                os.system('lpr -o fit-to-page /home/pi/Desktop/python3-fingerprint/examples/application/breakfast ')
                                tm.sleep(1)
                                pos=str(positionNumber)
                                val=df1.query('fingerid not in @pos')
                                print(df)
                                df.to_csv('tiffin.csv',encoding="utf-8",index=False)
                                val.to_csv('temptiffin'+str(today)+'.csv',encoding="utf-8",index=False)
                            else:
                                print("already claimed")

                    elif(time.hour>=12 and time.hour<15):
                        print('lunch success')
                        dft=pd.read_csv("analysis.csv")
                        if date not in dft.columns:
                                print("yeah")
                                try:
                                    df=pd.read_csv("tiffin.csv")
                                    count=df[date].count()
                                except:
                                    count=0
                                print("1")
                                dft.set_value(0,date,str(count))
                                print("2")
                                dft.to_csv("analysis.csv",encoding="utf-8",index=False)
                                os.remove('temptiffin'+str(today)+'.csv')
                                print("3")
##TEST                                
                        if(((df2.fingerid == positionNumber).any())==True):
                            print("qg")
                            df=pd.read_csv('lunch.csv')
                            print("entered")
                            if date not in df.columns:
                                print("also")
                                df.set_value(0,date,str(positionNumber))
                                os.system('lpr -o fit-to-page /home/pi/Desktop/python3-fingerprint/examples/application/lunch')
                                df.to_csv("lunch.csv",encoding="utf-8",index=False)
                                print("successful")
                            elif(((df[date] == positionNumber).any())==False):
                                print("success")
                                x=df[date].count()
                                print("success")
                                print(df)
                                ##df.loc[x,'date'] = str(positionNumber)
                                df.set_value(int(x),date,str(positionNumber))
                                print(df)
                                print('Lunch granted')
                                os.system('lpr -o fit-to-page /home/pi/Desktop/python3-fingerprint/examples/application/lunch')
                                tm.sleep(1)
                                pos=str(positionNumber)
                                val=df2.query('fingerid not in @pos')
                                print(df)
                                dft=pd.read_csv("analysis.csv")
                                count=df[date].count()
                                dft.set_value(1,date,str(count))
                                dft.to_csv("analysis.csv",encoding="utf-8",index=False)
                                df.to_csv('lunch.csv',encoding="utf-8",index=False)
                                val.to_csv('templunch'+str(today)+'.csv',encoding="utf-8",index=False)
                            else:
                                print("already claimed")
                                
                                
                        

                    elif(time.hour>=19 and time.hour<22):
                        print('dinner success')
                        dft=pd.read_csv("analysis.csv")
                        print("htde")
                        print(date)
                        
                        if date in dft.columns:
                            print("egsd")
                           
                            try:
                                df=pd.read_csv("lunch.csv")
                                print("1")
                                count=df[date].count()
                            except:
                                count=0
                            dft.set_value(1,date,str(count))
                            dft.to_csv("analysis.csv",encoding="utf-8",index=False)
                        if(((df3.fingerid == positionNumber).any())==True):
                            print("SBF")
                            df=pd.read_csv('dinner.csv')
                            if date not in df.columns:
                                print("also")
                                x=df.shape[0]
                                print(x)
                                df.set_value(0,date,str(positionNumber))
                                os.system('lpr -o fit-to-page /home/pi/Desktop/python3-fingerprint/examples/application/dinner')
                                df.to_csv("dinner.csv",encoding="utf-8",index=False)
                                print("successful")
                            elif(((df[date] == positionNumber).any())==False):
                                print("success")
                                x=df[date].count()
                                print(x)
                                print("success")
                                print(df)
                                ##df.loc[x,'fingerid'] = str(positionNumber)
                                print('sucess')
                                df.set_value(int(x),date,positionNumber)
                                print(df)
                                
                                os.system('lpr -o fit-to-page /home/pi/Desktop/new \n')
                                print('done')
                                os.system('lpr -o fit-to-page /home/pi/Desktop/python3-fingerprint/examples/application/dinner')
                                df.to_csv('dinner.csv',encoding="utf-8",index=False)
                                pos=str(positionNumber)
                                val=df3.query('fingerid not in @pos')
                                print(df)
                                dft=pd.read_csv("analysis.csv")
                                count=df[date].count()
                                dft.set_value(2,date,str(count))
                                dft.to_csv("analysis.csv",encoding="utf-8",index=False)
                                val.to_csv('tempdinner'+str(today)+'.csv',encoding="utf-8",index=False)
                            else:
                                print("already claimed")
                        
                    
                    

                ## OPTIONAL stuff
                ##

                ## Loads the found template to charbuffer 1
                f.loadTemplate(positionNumber, 0x01)

                ## Downloads the characteristics of template loaded in charbuffer 1
                characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

                ## Hashes characteristics of template
                print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())


            except Exception as e:
                print('Operation failed!')
                print('Exception message: ' + str(e))
                print(positionNumber)
    ##            os._exit(0)

        elif(bit=='1'):
            print("sensor in use")
    
