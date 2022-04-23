import os
import sys
import netifaces
import pyshark
import sqlite3
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from dictionary import dictionary
from PyQt5 import QtWidgets


class Sniffer:
    def __init__(self):
        super().__init__()
        self.CheckRoot()
        self.con = sqlite3.connect('CMShark.db', check_same_thread=False)
        self.blacklist = self.ReadBlacklist()
        self.inModel = pickle.load(
            open("./models/netflow-dataset-in-model.sav", 'rb'))
        self.outModel = pickle.load(
            open("./models/netflow-dataset-out-model.sav", 'rb'))

        self.maxCount = 100

        self.ipDictionary = dictionary(self.maxCount)
        self.detected = []

    def CheckRoot(self):
        if not os.geteuid() == 0:
            sys.exit("sorry, can\'t sniff. this script must be run as root!")

    def GetMyIp(self):
        return netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]["addr"]

    def GetInterfaces(self):
        return netifaces.interfaces

    def SetInterface(self, interface):
        self.interface = interface
        self.myIp = self.GetMyIp()

    def IsPacketMine(self, ipLayer):
        if ipLayer.src == self.myIp:
            return [1, ipLayer.dst]
        elif ipLayer.dst == self.myIp:
            return [0, ipLayer.src]
        else:
            return False

    def Sniff(self, detectionTable, scanUrl, scanPayload, scanMLM):

        capture = pyshark.LiveCapture(interface=self.interface)
        for packet in capture.sniff_continuously():

            if hasattr(packet, "ip"):
                # on this line we check if packet belong to this PC, if we want to use system for whole PCs on the current network we can remove this  condition.
                if self.IsPacketMine(packet.ip):
                    flowDirection, otherIp = self.IsPacketMine(packet.ip)

                    if self.IsForbiddenIps(otherIp):
                        # print(otherIp, "is blackliseted")
                        self.AddDetected(otherIp, "url scanner",
                                         "ip blacklisted", detectionTable, "100%")

                    payload = self.GetPayload(packet)
                    if payload != None:
                        blackword = self.HasForbiddenWord(payload)
                        if blackword != None:
                            # print(otherIp, "has a blacklisetd word", blackword)
                            reason = "has a blacklisetd word " + blackword
                            self.AddDetected(
                                otherIp, "payload scanner", reason, detectionTable, "100%")

                    # print(packet)
                    predictedType = 0
                    if self.inModel.predict([[packet.__len__()]])[0] == "cryptojacking":
                        predictedType = 1

                    condition = self.ipDictionary.SetProbability(
                        otherIp, predictedType)

                    if condition > (self.maxCount/2):
                        self.AddDetected(otherIp, "ML scanner", "suspicious packet size", detectionTable, str(
                            (condition*100)/self.maxCount))

    def AddDetectedRecored(self, detectionTable, processName, detectedBy, certainty, info):
        currentRow = detectionTable.rowCount()
        detectionTable.insertRow(currentRow)
        detectionTable.setItem(
            currentRow, 0, QtWidgets.QTableWidgetItem(processName))
        detectionTable.setItem(
            currentRow, 1, QtWidgets.QTableWidgetItem(detectedBy))
        detectionTable.setItem(
            currentRow, 2, QtWidgets.QTableWidgetItem(certainty))
        detectionTable.setItem(currentRow, 3, QtWidgets.QTableWidgetItem(info))

    def IsForbiddenIps(self, ip):
        myCursor = self.con.cursor()
        myCursor.execute(
            'SELECT COUNT(nsblackword_id) FROM nsblacklist WHERE nsblackword_word="'+ip+'"')
        blacklistedCount = myCursor.fetchone()
        myCursor.close()
        if blacklistedCount[0] == 0:
            return False
        else:
            return True

    def ReadBlacklist(self):
        blacklist = []
        myCursor = self.con.cursor()
        myCursor.execute(
            "SELECT blackword_word FROM blacklist WHERE blackword_is_on=1")
        for blackword in myCursor.fetchall():
            blacklist.append(blackword[0])
        myCursor.close()
        return blacklist

    def GetPayload(self, packet):
        if hasattr(packet, "tcp"):
            if hasattr(packet.tcp, "payload"):
                return self.ByteStringToString(packet.tcp.payload)
        elif hasattr(packet, "udp"):
            if hasattr(packet.udp, "payload"):
                return self.ByteStringToString(packet.udp.payload)
        else:
            return None

    def ByteStringToString(self, byteString):
        readableString = ""
        for byteCode in byteString.split(":"):
            readableString += chr(int(byteCode, 16))

        return readableString

    def HasForbiddenWord(self, payload):
        for blackword in self.blacklist:
            if payload.find(blackword) >= 0:
                return blackword
        return None

    def AddDetected(self, ip, treatType, reason, detectionTable, certainty):
        for row in self.detected:
            if row[0] == ip and row[1] == treatType:
                return
        self.detected.append([ip, treatType, reason])
        self.AddDetectedRecored(
            detectionTable, ip, treatType, certainty, reason)
