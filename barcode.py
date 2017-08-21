## Barcode Function
## support module is before
## time module is before


def Barcode:
    "function happens when barcode is scanned"
    while end = 0:
        support.clearScreen()
        barcode = input("Scan barcode")
        if barcode == "56843291": ## Start Press
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in start.txt
        elif barcode == "06319572": ## Stop Press
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in stop.txt
        elif barcode == "03196242": ## 1st good
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in misc.txt
        elif barcode == "03195726": ## 1st dock
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in misc.txt
        elif barcode == "91358627": ## last dock
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in misc.txt
        elif barcode == "62951648": ## Ang truck
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in misc.txt
        elif barcode == "52679518": ## Brz truck
            currentTime = #format time for HH:MM 12 hour
            ## insert code to place in misc.txt
        elif barcode == "exit":
            postRun()

def preRun:
    "Pre Run Information"
    support.clearScreen()
    numInserts = input("Number of Inserts: ")
    angDriver = input("Angleton Driver: ")
    brzDriver = input("West Brazos Driver: ")
    ## insert code to write into prerun.txt

def postRun:
    "post run information"
    support.clearScreen()
    front = input("Who took papers to front? ")
    rackFill = input("Who filled the rack? ")
    rack = input("Rack pulled by: ")
    mail = input("Who did mail? ")
    twenty = input("Who put the 20 together? ")
    hospital = input("Who put the hospital together? ")
    ## Insert code to write into postrun.txt
    ## Call report generation function
