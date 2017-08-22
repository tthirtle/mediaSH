# Mailroom Press Reports
#Version 0.1 a
#Barcode Edition
import time
from yattag import Doc
doc, tag, text = Doc().tagtext()
import support
import shutil

NEWLINE = "\n"
def barcode():
    "function happens when barcode is scanned"
    end = 0
    angTime = "time"
    brzTime = "time"
    while end == 0:
        support.clearScreen()
        barcode = input("Scan barcode: ")
        if barcode == "56843291": ## Start Press
            currentTime = time.strftime("%I:%M %p")
            start = open("start.txt",'a')
            start.write(currentTime)
            start.write(NEWLINE)
            start.close()
        elif barcode == "06319572": ## Stop Press
            currentTime = time.strftime("%I:%M %p")
            stop = open("stop.txt",'a')
            stop.write(currentTime)
            stop.write(NEWLINE)
            stop.close()
        elif barcode == "03196242": ## 1st good
            currentTime = time.strftime("%I:%M %p")
            misc = open("misc.txt",'a')
            misc.write(currentTime)
            misc.write(NEWLINE)
            misc.close()
        elif barcode == "03195726": ## 1st dock
            currentTime = time.strftime("%I:%M %p")
            misc = open("misc.txt",'a')
            misc.write(currentTime)
            misc.write(NEWLINE)
            misc.close()
        elif barcode == "91358627": ## last dock
            currentTime = time.strftime("%I:%M %p")
            misc = open("misc.txt",'a')
            misc.write(angTime)
            misc.write(NEWLINE)
            misc.write(brzTime)
            misc.write(NEWLINE)
            misc.write(currentTime)
            misc.close()
        elif barcode == "62951648": ## Ang truck
            currentTime = time.strftime("%I:%M %p")
            angTime = currentTime
        elif barcode == "52679518": ## Brz truck
            currentTime = time.strftime("%I:%M %p")
            brzTime = currentTime
        elif barcode == "exit":
            end = 1
            postRun()

def preRun():
    "Pre Run Information"
    support.clearScreen()
    numInserts = input("Number of Inserts: ")

    prerun = open("prerun.txt","w")
    prerun.write(numInserts)
    prerun.write(NEWLINE)

    prerun.close()
    return

def postRun():
    "post run information"
    support.clearScreen()
    angDriver = input("Angleton Driver (blank = none): ")
    if angDriver == "":
        angDriver = "none"
    brzDriver = input("West Brazos Driver (blank = none): ")
    if brzDriver == "":
        brzDriver = "none"
    front = input("Who took papers to front? ")
    rackFill = input("Who filled the rack? ")
    rack = input("Rack pulled by: ")
    mail = input("Who did mail? ")
    twenty = input("Who put the 20 together? ")
    hospital = input("Who put the hospital together? ")
    postrun = open("postrun.txt","w")
    postrun.write(angDriver)
    postrun.write(NEWLINE)
    postrun.write(brzDriver)
    postrun.write(NEWLINE)
    postrun.write(front)
    postrun.write(NEWLINE)
    postrun.write(rackFill)
    postrun.write(NEWLINE)
    postrun.write(rack)
    postrun.write(NEWLINE)
    postrun.write(mail)
    postrun.write(NEWLINE)
    postrun.write(hospital)
    postrun.write(NEWLINE)
    postrun.write(twenty)
    postrun.write(NEWLINE)
    postrun.close()
    reports()
    return

def reports():
    "Final Report Generation"
    shutil.copyfile("template.html","report.html")
    html = open("report.html",'a')
    start = open("start.txt",'r')
    stop = open("stop.txt",'r')
    misc = open("misc.txt",'r')
    prerun = open("prerun.txt",'r')
    postrun = open("postrun.txt",'r')
    miscLines = misc.readlines()
    startLines = start.readlines()
    stopLines = stop.readlines()
    preLines = prerun.readlines()
    postLines = postrun.readlines()

    date = (time.strftime("%D",time.localtime()))
    dateStr = "<p>" + "Date: " + date + "</p>"+ NEWLINE
    html.write(dateStr)
    numInserts = "<p>" + "Total Number of inserts: " + preLines[0]+ "</p>"+ NEWLINE
    html.write(numInserts)
    html.close()
    html = open("report.html",'a')
    html.write("<table border =\"1\">\n")
    for index in range(len(startLines)):
        html.write("<tr>")
        startTime = "Start: " + startLines[index].strip()
        stopTime = "Stop: " + stopLines[index].strip()    
        html.write("<td>")
        html.write(startTime)
        html.write("</td>")
        html.write("<td>")
        html.write(stopTime)
        html.write("</td>\n")
        html.write("</tr>")
    html.write("</table>")
    html.close()
    html = open("report.html",'a')
    firstGood = "<p>" + "First good Papers: " + miscLines[0].strip() + "</p>"+ NEWLINE
    html.write(firstGood)
    endRun = "<p>" + "End of press run: " + stopLines[index].strip()+ "</p>"+ NEWLINE
    html.write(endRun)
    with tag('p'):
        text("Truck Completion Times")
        
    angleton = "Angleton\Liverpool Completion: " + miscLines[2].strip() + "Driver: " + postrun[0].strip()
    wBrazos = "Brazoria\West Columbia Completion: " + miscLines[3].strip() + "Driver: " + postrun[1].strip()
    with tag('p'):
        text(angleton)
    
    with tag('p'):
        text(wBrazos)
    
    problems = input("Problems: ")
    firstDock = "First On Dock: " + miscLines[1].strip()
    lastDock = "Last On Dock: " + miscLines[4].strip()
    with tag('p'):
        text(firstDock)
    
    with tag('p'):
        text(lastDock)
    
    with tag('p'):
        text(problems)
    
    
    front = "Taken up front by: " + postLines[2].strip()
    twenty = "Twenty put together by: " + postLines[5].strip()
    hospital = "Hospital put together by: " + postLines[7].strip()
    rackFill = "Rack outside Filled by: " + postLines[6].strip()
    rackPull = "Rack pulled by: " + postLines[4].strip()
    mail = "Mail completed by: " + postLines[5].strip()
    with tag('p'):
        text(front)
    
    with tag('p'):
        text(twenty)
    
    with tag('p'):
        text(hospital)
    
    with tag('p'):
        text(rackFill)
    
    with tag('p'):
        text(rackPull)
    
    with tag('p'):
        text(mail)
    html.write((doc.getvalue()))
    html.write("</body>")
    html.write(NEWLINE)
    html.write("</html>")
    html.close()
    return
preRun()
barcode()
