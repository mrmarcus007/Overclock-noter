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
lang = None

def lang():
    global lang
    os.system('cls')
    print("Please select 1 of 2 languages, Bitte Wahalen sie 1 oder 2 Sprachen")
    print("1. English \n2. Deusche")
    lang = input(">")

def start():
    os.system('cls')
    print(graphics.Overclock)
    print(graphics.Rever)
    time.sleep(2)
    try:
        print("Ladt... Loading...")
        load()
        if lang == "1":
            configdisplay()
            input("press enter to go to the menu")
            Menu()
        elif lang == "2":
            configdisplay()
            input("Drücken Sie die Eingabetaste, um zum Menü zu gelangen")
            Menu()
    except:
        print("This is first time setup, please wait...")
        time.sleep(0.5987654321)
        lang()
        editor()

def load():
    global System, PCname, CPUPowerLimit, CPUClock, Processor, Gprocessor, GPUpowerLimit, GPUClock, GPUMemoryClock, BusClock, RyzenADJI, USBdevices, TotalUSBpower, TotalPower, lang
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
        lang = (data["lang"])

def Menu():
    os.system('cls')
    if lang == "1": 
        print("="*40, "\n", graphics.Menu, "\n", graphics.Rever, "\n", "="*40)
        print(" 1. View current configuration \n 2. Edit configuration \n 3. export configuration \n 4. exit program")
        choice = input(" user: ")
        if choice == "1":
            os.system('cls')
            configdisplay()
            input(" Press any-key to continue")
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
    elif lang == "2":
        print("="*40, "\n", graphics.Menu, "\n", graphics.Rever, "\n", "="*40)
        print(" 1. Aktuelle Konfiguration anzeigen \n 2. Konfiguration bearbeiten \n 3. Konfiguration exportieren \n 4. Programm beenden")
        choice = input(" Benutzer: ")
        if choice == "1":
            os.system('cls')
            configdisplay()
            input(" Drücken Sie eine beliebige Taste, um fortzufahren")
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
        lang()
        Menu()
        
def editor():
    global lang
    if lang == "1":
        filename = "Configuationtable.txt"
        with open(filename, "w") as file:
                file.write("Configuration Table\n")
                file.write("-------------------\n")
                file.write("PC Name: {}\n".format(data["PCname"]))
                file.write("System: {}\n".format(data["System"]))
                file.write("Processor: {}\n".format(data["Processor"]))
                file.write("CPU Power Limit (W): {}\n".format(data["CPUPowerLimit"]))
                file.write("CPU Clock (GHz): {}\n".format(data["CPUClock"]))
                file.write("Bus Clock (MHz): {}\n".format(data["BusClock"]))
                file.write("GPU: {}\n".format(data["Gprocessor"]))
                file.write("GPU Power Limit (W): {}\n".format(data["GPUpowerLimit"]))
                file.write("GPU Clock (MHz): {}\n".format(data["GPUClock"]))
                file.write("GPU Memory Clock (MHz): {}\n".format(data["GPUMemoryclock"]))
                file.write("Ryzen ADJI Preset: {}\n".format(data["RyzenADJI"]))
                file.write("USB Devices: {}\n".format(data["USBdevices"]))
                file.write("Total USB Power (W): {}\n".format(data["TotalUSBPower"]))
                file.write("Total Power (W): {}\n".format(data["TotalPower"]))
                print("Values exported to {}.".format(filename))
    elif lang == "2":
        filename = "Konfigurationstabelle.txt"
        with open(filename, "w") as file:
                file.write("Konfigurationstabelle\n")
                file.write("---------------------\n")
                file.write("PC-Name: {}\n".format(data["PCname"]))
                file.write("System: {}\n".format(data["System"]))
                file.write("Prozessor: {}\n".format(data["Processor"]))
                file.write("Prozessorleistungsgrenze (W): {}\n".format(data["CPUPowerLimit"]))
                file.write("Prozessoruhr (GHz): {}\n".format(data["CPUClock"]))
                file.write("Busuhr (MHz): {}\n".format(data["BusClock"]))
                file.write("GPU: {}\n".format(data["Gprocessor"]))
                file.write("GPU-Leistungsbegrenzung (W): {}\n".format(data["GPUpowerLimit"]))
                file.write("GPU-Takt (MHz): {}\n".format(data["GPUClock"]))
                file.write("GPU-Speichertakt (MHz): {}\n".format(data["GPUMemoryclock"]))
                file.write("Ryzen ADJI voreingestellt: {}\n".format(data["RyzenADJI"]))
                file.write("Statische USB-Geräte: {}\n".format(data["USBdevices"]))
                file.write("Gesamtleistung USB (W): {}\n".format(data["TotalUSBPower"]))
                file.write("Gesamtleistung (W): {}\n".format(data["TotalPower"]))
                print("Werte in {} exportiert.".format(filename))
    else:
        error = '1'
        function = '4'
        errorhandler(error, function)


def configdisplay():
    if lang == "1":
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
    elif lang == "2":
        os.system("cls")
        print("="*5, "zuletzt gespeicherte Konfigurations-/Systeminformationen", "="*5, "\n")
        print(" System: ", System)
        print(" PC Name: ", PCname)
        print("\n Prozessor: ", Processor)
        print(" Prozessorleistungsgrenze: ", CPUPowerLimit, "W")
        print(" Prozessoruhr: ", CPUClock, "Ghz")
        print(" Busuhr: ", BusClock, "Mhz")
        print("\n GPU: ", Gprocessor)
        print(" GPU-Leistungsbegrenzung: ", GPUpowerLimit, "W")
        print(" GPU-Takt: ", GPUClock, "Mhz")
        print(" GPU-Speichertakt: ", GPUMemoryClock, "Mhz")
        print("\n Ryzen ADJI, ", RyzenADJI)
        print("\n Statische USB-Geräte:", USBdevices)
        print(" Totale USB-Leistung: ", TotalUSBpower)
        print("\n Totale Kraft: ", TotalPower)
        print(graphics.Rever)
    else:
        error = ('1')
        funchtion = ('5')
        errorhandler(error, funchtion)

def export():
    if lang == "1":
        with open("Configuationtable.json", "r") as file:
            data = json.loads(file.read())
            with open("config_data.txt", "w") as file:
                file.write("="*5 + " last Saved Configuation/System Information " + "="*5 + "\n")
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
                file.write(graphics.rever)
        print(" Data exported to config")
        input(" Press enter to continue")
        Menu()
    elif lang == "2":
         with open("Configuationtable.json", "r") as file:
            data = json.loads(file.read())
            with open("config_data.txt", "w") as file:
                file.write("="*5 + "zuletzt gespeicherte Konfigurations-/Systeminformatione" + "="* + "\n")
                file.write(" System: " + data["System"] + "\n")
                file.write(" PC Name: " + data["PCname"] + "\n")
                file.write("\n Proezsor: " + data["Processor"] + "\n")
                file.write(" Prozessorleistungsgrenze: " + float(data["CPUPowerLimit"] + "W" + "\n"))
                file.write(" Prozessoruhr: " + str(data["CPUClock"]) + "Ghz" + "\n")
                file.write(" Busuhr: " + str(data["BusClock"]) + "Mhz" + "\n")
                file.write("\n GPU: " + data["Gprocessor"] + "\n")
                file.write(" GPU-Leistungsbegrenzung: " + str(data["GPUpowerLimit"]) + "W" + "\n")
                file.write(" GPU-Takt: " + str(data["GPUClock"]) + "Mhz" + "\n")
                file.write(" GPU-Speichertakt: " + str(data["GPUMemoryclock"]) + "Mhz" + "\n")
                file.write("\n Ryzen ADJI: " + data["RyzenADJI"] + "\n")
                file.write("\n Statische USB-Geräte: " + str(data["USBdevices"]) + "\n")
                file.write(" Totale USB-Leistung: " + str(data["TotalUSBPower"]) + "W" + "\n")
                file.write(" Totale Kraft: " + str(data["TotalPower"]) + "W" + "\n")
                file.write(graphics.rever)
            print(" Daten exportiert nach config")
            input(" Drücken Sie die Eingabetaste, um fortzufahren")
            Menu()
    else:
        error = ('1')
        funchtion = ('6')
        errorhandler(error, funchtion)

def errorhandler(error, funchtion):
     options = {
        '1': start,
        '2': load,
        '3': Menu,
        '4': editor,
        '5': configdisplay,
        '6': export,
        '7': existstage1,
        '8': existstage1,
        '9': load,
        '10': exit,
    }
     if error == "1":
        print(" A language baised error has occured \n Ein sprachbasierter Fehler ist aufgetreten")
        time.sleep(1.5987654321)
        lang()
        if funchtion in options:
            options[funchtion]()

def existstage1():
    if lang == 1:
        os.system('cls')
        print(graphics.Warning)
        print(" Are you sure you want to exit? Y/N")
        b.higher = input(" user: ")
        if b == "Y":
            exitstage2()
        if b == "N":
            Menu()
        else:
            existstage1()
    elif lang == "2":
        os.system('cls')
        print(graphics.Warning)
        print(" Sie sind sicher, dass Sie beenden wollen? J/N")
        b.higher = input(" user: ")
        if b == "J":
            exitstage2()
        if b == "N":
            Menu()
        else:
            existstage1()
    else:
        error = ('1')
        funchtion = ('7')
        errorhandler(error, funchtion)


def exitstage2():
    t = 10
    if lang == 1:
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
    elif lang == 2:
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

