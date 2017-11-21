# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:17:12 2017

@author: Quentin
"""
import re


file_name = "test"
file_path= "./data/"

file_object = open(file_path+file_name+"_injuries.txt", 'r')

lines = file_object.readlines()
regex = re.compile(r"[0-9]+ ([a-zA-Z]+-[a-zA-Z]+\[[0-9+]\];)*")

for line in lines:
    if regex.match(line) is not None:
        print(line)
        starting_frame = re.findall("([0-9]+) ", line)
        ids = re.findall("([a-zA-Z]+-[a-zA-Z]+)", line)
        values = re.findall("\[([0-9]+)\];", line)
        starting_frame = int(starting_frame[0])
        print(starting_frame)
        for i in range(0, len(values)):
            print(ids[i])
            print(values[i])
    else:
        print("error")
        
        

correspondance_table_pfnn = {}
correspondance_table_pfnn["Hips-LHipJoint"] = 0
correspondance_table_pfnn["LHipJoint-LeftUpLeg"] = 1
correspondance_table_pfnn["LeftUpLeg-LeftLeg"] = 2
correspondance_table_pfnn["LeftLeg-LeftFoot"] = 3
correspondance_table_pfnn["LeftFoot-LeftToeBase"] = 4

correspondance_table_pfnn["Hips-RHipJoint"] = 5
correspondance_table_pfnn["RHipJoint-RightUpLeg"] = 6
correspondance_table_pfnn["RightUpLeg-RightLeg"] = 7
correspondance_table_pfnn["RightLeg-RightFoot"] = 8
correspondance_table_pfnn["RightFoot-RightToeBase"] = 9

correspondance_table_pfnn["Hips-LowerBack"] = 10
correspondance_table_pfnn["LowerBack-Spine"] = 11
correspondance_table_pfnn["Spine-Spine1"] = 12
correspondance_table_pfnn["Spine1-Neck"] = 13
correspondance_table_pfnn["Neck-Neck1"] = 14
correspondance_table_pfnn["Neck1-Head"] = 15

correspondance_table_pfnn["Spine1-LeftShoulder"] = 16
correspondance_table_pfnn["LeftShoulder-LeftArm"] = 17
correspondance_table_pfnn["LeftArm-LeftForeArm"] = 18
correspondance_table_pfnn["LeftForeArm-LeftHand"] = 19
correspondance_table_pfnn["LeftHand-LeftFingerBase"] = 20
correspondance_table_pfnn["LeftFingerBase-LeftHandIndex1"] = 21
correspondance_table_pfnn["LeftHand-LThumb"] = 22

correspondance_table_pfnn["Spine1-RightShoulder"] = 23
correspondance_table_pfnn["RightShoulder-RightArm"] = 24
correspondance_table_pfnn["RightArm-RightForeArm"] = 25
correspondance_table_pfnn["RightForeArm-RightHand"] = 26
correspondance_table_pfnn["RightHand-RightFingerBase"] = 27
correspondance_table_pfnn["RightFingerBase-RightHandIndex1"] = 28
correspondance_table_pfnn["RightHand-RThumb"] = 29
