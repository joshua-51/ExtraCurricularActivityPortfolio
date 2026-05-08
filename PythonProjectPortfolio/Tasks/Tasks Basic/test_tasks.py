from tasks import addTask
from tasks import readTasks
from tasks import checkTime

def testingAddTask():
    assert addTask("Do Math Homework") == True
    assert addTask("12") == True
    assert addTask("       do work       ") == True
    assert addTask("      Do mAtH HOMEworK    ") == True

def testingCheckTime():
    assert checkTime("3:30") == "3 hrs 30 mins"
    assert checkTime("3:00") == "3 hrs 0 mins"
    assert checkTime("34")   == "34 mins"
    assert checkTime("1")    == "1 min"
    assert checkTime("70")   == "1 hrs 10 mins"
    assert checkTime("1:60") == "2 hrs"

def testingReadTasks():
    assert readTasks() == True