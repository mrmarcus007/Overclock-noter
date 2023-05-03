import graphics, time, os, platform, json

System = ()
PCname = ()
CPUPowerLimit = ()
CPUClock = ()
Processor = ()
Gprocessor = ()
GPUpowerLimit = ()
GPUClock = ()
GPUMemoryClock = ()
BusClock = ()
RyzenADJI = ()
USBdevices = ()
TotalUSBpower = ()
TotalPower = ()
Lang = ()

def lang():
    global Lang
    os.system('cls')
    print("Please select 1 of 2 languages, Bitte Wahalen sie 1 oder 2 Sprachen")
    print("1. English \n 2. Deusche)
    Lang = input(">")

def start():
    os.system('cls')
    print(graphics.Overclock)
    print(graphics.Rever)
    time.sleep(2)
    try:
        load()
        configdisplay()
        input("press any key to go to the menu")
        Menu()
    except:
        print("This is first time setup, please wait...")
        time.sleep(2)
        time.sleep(0.5987654321)
        editor()

def load():
    global System, PCname, CPUPowerLimit, CPUClock, Processor, Gprocessor, GPUpowerLimit, GPUClock, GPUMemoryClock, BusClock, RyzenADJI, USBdevices, TotalUSBpower, TotalPower
    with open("Configuationtable.json", "r") as file:
        data = json.loads(file.read())
        System = (data["System"])
        PCname = (data["PCname"])
        CPUPowerLimit = (data["CPUPowerLimit"])
        CPUClock = (data["CPUClock"])
        Processor = (data["Processor"])
        Gprocessor = (data["Gprocessor"])
        GPUpowerLimit = (data["GPUpowerLimit"])
        GPUClock = (data["GPUClock"])
        GPUMemoryClock = (data["GPUMemoryclock"])
        BusClock = (data["BusClock"])
        RyzenADJI = (data["RyzenADJI"])
        USBdevices = (data["USBdevices"])
        TotalUSBpower = (data["TotalUSBPower"])
        TotalPower = (data["TotalPower"])

def Menu():
    if lang = 1: 
        os.system('cls')
        print("="*40, "\n", graphics.Menu, "\n", graphics.Rever, "\n", "="*40)
        print(" 1. View current configuration \n 2. Edit configuration \n 3. export configuration \n 4. exit program")
        choice = input(" user: ")
        if choice == "1":
            os.system('cls')
            configdisplay()
            input(" Press enter to continue")
            Menu()
        elif choice == "2":
            os.system('cls')
            editor()
        elif choice == "3":
            export()
        elif choice == "4":
            existstage1()
        else: 
            Menu()
    else:
        os.system('cls')
        print("="*40, "\n", graphics.MenuD, "\n", graphics.ReverD, "\n", "="*40)
        print(" 1. Aktuelle Konfiguration anzeigen \n 2. Konfiguration bearbeiten \n 3. Konfiguration exportieren \n 4. Programm beenden")
        choice = input(" Benutzer: ")
        if choice == "1":
            os.system('cls')
            configdisplay()
            input(" Press enter to continue")
            Menu()
        elif choice == "2":
            os.system('cls')
            editor()
        elif choice == "3":
            export()
        elif choice == "4":
            existstage1()
        else: 
            Menu()
        
def editor():
    my_system = platform.uname()
    os.system('cls')
    print(graphics.Warning)
    print(" You are edting data!")
    print("Don't use units")
    CPUPowerLimit = float(input("CPU Power Limit (W): "))
    CPUClock = float(input("CPU Clock (Ghz): "))
    Gprocessor = input("GPU: ")
    GPUpowerLimit = float(input("GPU power limit (W): "))
    GPUClock = float(input("GPU clock (Mhz): "))
    GPUMemoryClock = float(input("GPU memory clock (Mhz): "))
    BusClock = float(input("Bus Clock (Mhz): "))
    RyzenADJI = input("Ryzen ADJI preset (if you have one, if not leave blank): ")
    USBdevices = int(input("Amount of static USB devices: " ))
    TotalUSBpower = USBdevices * 4.5
    TotalPower = (TotalUSBpower + GPUpowerLimit + CPUPowerLimit * 1.352)
    data = {
    "PCname": my_system.node,
    "System": f"{my_system.system} {my_system.version}",
    "Processor": my_system.processor,
    "CPUPowerLimit": CPUPowerLimit,
    "CPUClock": CPUClock,
    "BusClock": BusClock,
    "Gprocessor": Gprocessor,
    "GPUpowerLimit": GPUpowerLimit,
    "GPUClock": GPUClock,
    "GPUMemoryclock": GPUMemoryClock,
    "RyzenADJI": RyzenADJI,
    "USBdevices": USBdevices,
    "TotalUSBPower": TotalUSBpower,
    "TotalPower": TotalPower
    }
    with open("Configuationtable.json", "w") as file:
        file.write(json.dumps(data))
    load()
    Menu()

def configdisplay():
    os.system("cls")
    print("="*5, "last Saved Configuation/System Information", "="*5, "\n")
    print(" System: ", System)
    print(" PC Name: ", PCname)
    print("\n Processor: ", Processor)
    print(" Processor Power Limit: ", CPUPowerLimit, "W")
    print(" Processor clock: ", CPUClock, "Ghz")
    print(" Bus clock: ", BusClock, "Mhz")
    print("\n GPU: ", Gprocessor)
    print(" GPU Power Limit: ", GPUpowerLimit, "W")
    print(" GPU Clock: ", GPUClock, "Mhz")
    print(" GPU memory clock: ", GPUMemoryClock, "Mhz")
    print("\n Ryzen ADJI, ", RyzenADJI)
    print("\n Static USB devices:", USBdevices)
    print(" Total USB power: ", TotalUSBpower)
    print("\n Totalpower: ", TotalPower)
    print(graphics.Rever)

def export():
    with open("Configuationtable.json", "r") as file:
        data = json.loads(file.read())
        with open("config_data.txt", "w") as file:
            file.write("="*40 + " last Saved Configuation/System Information " + "="*40 + "\n")
            file.write(" System: " + data["System"] + "\n")
            file.write(" PC Name: " + data["PCname"] + "\n")
            file.write("\n Processor: " + data["Processor"] + "\n")
            file.write(" Processor Power Limit: " + data["CPUPowerLimit"] + "W" + "\n")
            file.write(" Processor clock: " + str(data["CPUClock"]) + "Ghz" + "\n")
            file.write(" Bus clock: " + str(data["BusClock"]) + "Mhz" + "\n")
            file.write("\n GPU: " + data["Gprocessor"] + "\n")
            file.write(" GPU Power Limit: " + str(data["GPUpowerLimit"]) + "W" + "\n")
            file.write(" GPU Clock: " + str(data["GPUClock"]) + "Mhz" + "\n")
            file.write(" GPU Memory clock: " + str(data["GPUMemoryclock"]) + "Mhz" + "\n")
            file.write("\n Ryzen ADJI: " + data["RyzenADJI"] + "\n")
            file.write("\n Static USB devices: " + str(data["USBdevices"]) + "\n")
            file.write(" Total USB power: " + str(data["TotalUSBPower"]) + "W" + "\n")
            file.write(" Total Power: " + str(data["TotalPower"]) + "W" + "\n")
            file.write(" \n Overclock Manager, Version: 2.0.1")
    print(" Data exported to config")
    input(" Press enter to continue")
    Menu()

def existstage1():
    os.system('cls')
    print(graphics.Warning)
    print(" Are you sure you want to exit? Y/N")
    b = input(" user: ")
    if b == "Y" or b == "y":
        exitstage2()
    if b == "N" or b == "n":
        Menu()
    else:
        existstage1()

def exitstage2():
    t = 10
    while t > 0:
        if t >= 5:
            os.system('cls')
            print(graphics.Overclock)
            print(graphics.Rever, ", By Marcus Allison" )
            print("\n Closing program in", t)
            time.sleep(1)
            t = t - 1
        elif t == 1:
            os.system('cls')
            print(graphics.Bye)
            print(graphics.Rever, ", By Marcus Allison" )
            print("\n Terminated program")
            os._exit(1)
        elif t <= 5:
            os.system('cls')
            print(graphics.Bye)
            print(graphics.Rever, ", By Marcus Allison" )
            print("\n Closing program in", t)
            time.sleep(1)
            t = t - 1

start()
