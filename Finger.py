import struct as st
import serial as ser
import time,sys
import PyQt5
from PyQt5 import QtWidgets
import requests
head=[0xef01,0x00000000,0x01]
from FingerPrint import FingerPrint
class Finger:
    def __init__(self,port,ttl,location,posid,amount):
        self.location = location
        self.posid = posid
        self.amount = amount
        self.f=FingerPrint(port,ttl)
    def enroll(self):
        input("Put Finger:")
        self.f.getimg()
        self.f.genchar(1)
        r=self.f.search()
        if(r!=-1):
           print("Finger Already Taken at:"+str(r))
           sys.exit()
        input("Put Finger Again:")
        self.f.getimg()
        self.f.genchar(2)
        y=self.f.regmodel()
        if y:
          fid=input("Enter ID (0-254):")
          self.f.store(fid)
        else:
            app = QtWidgets.QApplication([])

            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!')

            app.exec_()
    def match(self):
        #input("Want to search:")
        self.f.getimg()
        self.f.genchar(1)
       
        r=self.f.searchapi(self.location,self.posid,self.amount)
        if(r!=-1):
            return str(r)
        elif (r == -1):
            return str(-1)
        else :
            return str(-1)
            # print("Finger Found at:"+str(r))
    def delete(self,fid,n):
        # fid=input("Enter Start Address")
        # n=input("Enter No of Fingerprints")
        self.f.delete(fid,n)
    def empty(self):
        self.f.empty()

        

