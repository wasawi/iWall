#!/usr/bin/python
import sys, httplib, re, time

projector='blestveggproj.ime.ntnu.no'
port=80
toggleUrl='/custom/01'
infoUrl='/info_data.htm'
sleepTime=30
retries=10

newState=sys.argv[1].lower()

def GetState():
    try:
        conn=httplib.HTTPConnection(projector,port,timeout=30)
        conn.request('GET',infoUrl)
        resp=conn.getresponse()
        if resp.status==200:
            data = resp.read()
            status=re.search('info_status_value[^[]*\[[^]]*(standby|power on|power saving)',data,re.I|re.S)
            if status:
                return status.group(1).lower()
        return ""
    except Exception.e:
        print "OOPS! Exception in GetState:", e.message
        return ""

def ToggleState():
    try:
        conn=httplib.HTTPConnection(projector,port,timeout=30)
        conn.request('GET',toggleUrl)
        resp=conn.getresponse()
        if resp.status==204:
            return 1
        return 0
    except Exception, e:
        print "OOPS! Exception in ToggleState:", e.message
        return 0

for i in range(0,retries):
    print "Time:", time.asctime()
    oldState=GetState()
    if not oldState:
        print "Unable to read status."
        sys.stdout.flush()
        time.sleep(sleepTime)
        continue
    print "State is:", oldState
    if oldState == newState:
        print "Correct state:", newState
        sys.exit(0)
    if ToggleState():
        print "Toggled power."
    else:
        print "OOPS! Error toggling power."
    sys.stdout.flush()
    time.sleep(sleepTime)
