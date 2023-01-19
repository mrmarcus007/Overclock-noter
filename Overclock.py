import graphics, time, os, platform, json

def start():
    os.system('cls')
    print(graphics.Overclock)
    print(graphics.Rever)
    time.sleep(2)
    try:
        print(configdisplay())
        time.sleep(5)
        Menu()
    except:
        print("This is first time setup, please wait...")
        time.sleep(5)
        editor()

def Menu():
    os.system('cls')
    print(graphics.Menu)
    print(" 1. View current configuration \n 2. Edit configuration \n 3. exit program")
    choice = input(" user: ")
    if choice == "1":
        os.system('cls')
        print(configdisplay())
        input(" Press enter to continue")
        Menu()
    elif choice == "2":
        os.system('cls')
        editor()
    elif choice == "3":
        existstage1()
    else: 
        Menu()
        
def editor():
    my_system = platform.uname()
    os.system('cls')
    print(graphics.Warning)
    print(" You are edting data!")
    print("Don't use units")
    CPUPowerLimit = str(input("CPU Power Limit (W): "))
    CPUClock = float(input("CPU Clock (Ghz): "))
    Gprocessor = input("GPU: ")
    GPUpowerLimit = float(input("GPU power limit (W): "))
    GPUClock = float(input("GPU clock (Mhz): "))
    GPUMemoryClock = float(input("GPU memory clock (Mhz): "))
    BusClock = float(input("Bus Clock (Mhz): "))
    RyzenADJI = input("Ryzen ADJI preset (if you have one, if not leave blank): ")
    USBdevices = int(input("Amount of static USB devices: " ))
    TotalUSBpower = float(USBdevices * 4.5)
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
    "TotalUSBPower": TotalUSBpower
    }
    with open("Configuationtable.json", "w") as file:
        file.write(json.dumps(data))
    Menu()

def configdisplay():
    with open("Configuationtable.json", "r") as file:
        data = json.loads(file.read())
        print("="*40, "last Saved Configuation/System Information", "="*40, "\n")
        print(" System: ", data["System"])
        print(" PC Name: ", data["PCname"])
        print("\n Processor: ", data["Processor"])
        print(" Processor Power Limit: ", data["CPUPowerLimit"], "W")
        print(" Processor clock: ", data["CPUClock"], "Ghz")
        print(" Bus clock: ", data["BusClock"], "Mhz")
        print("\n GPU: ", data["Gprocessor"])
        print(" GPU Power Limit: ", data["GPUpowerLimit"], "W")
        print(" GPU Clock: ", data["GPUClock"], "Mhz")
        print("\n Ryzen ADJI, ", data["RyzenADJI"])
        print("\n USB devices", data["USBdevices"])
        print(" Total usb power", data["TotalUSBPower"])
        return graphics.Rever

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
    t = 5
    while t > 0:
        os.system('cls')
        print(graphics.Bye)
        print(graphics.Rever, ", By Marcus Allison" )
        print("\n Closing program in", t)
        time.sleep(1)
        t = t - 1
        if t == 1:
            os.system('cls')
            print(graphics.Bye)
            print(graphics.Rever, ", By Marcus Allison" )
            print("\n Terminated program")
            os._exit(1)
    
start()