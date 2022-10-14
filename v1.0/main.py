import platform
from time import sleep
import subprocess

import wmi

print("PaintLow V1.0 CLI Edition(WINDOWS ONLY)")
print("-------------------------\n"
      "Options:\n"
      "1) About\n"
      "2) Start Sharing Info\n"
      "3) Hardware Tester")
option = input("Select One: ")


def minimalmode():
    print("Dumping Info...\n------------------")
    print(f"OS={platform.system()} {platform.release()}\n"
          f"PROCESSOR={platform.processor()}\n"
          f"ADVANCEDDUMP={platform.uname()}\n"
          f"ARCHITECTURE={platform.architecture()}")


def systemdump():
    print("Dumping Info...\n------------------")
    id1 = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in id1:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        print(i[2:-2])


def averagemode():
    c = wmi.WMI()
    sinfo = c.Win32_ComputerSystem()[0]
    print("Dumping Info...\n------------------")
    print("OS=" + platform.system() + " " + platform.release() + " FULL VERSION=" + platform.version())
    print("ARCHITECTURE=" + sinfo.SystemType)
    print("PROCESSORS=" + str(sinfo.NumberOfProcessors))
    print("MACHINE=" + platform.machine())
    print("PROCESSOR=" + platform.processor())
    print("NODE=" + platform.node())
    print("MANUFACTURER=" + sinfo.Manufacturer)


def infoshare():
    print("Select Mode:")
    print("1) Minimal Mode\n"
          "2) Average Mode\n"
          "3) Full System Data")
    infoshareoption = input("Select One: ")
    if infoshareoption == "1":
        minimalmode()
        print("----------------------\n"
              "Share This Info With The Person!")
        input("Press Enter To Close Terminal...")
    elif infoshareoption == "2":
        averagemode()
        print("----------------------\n"
              "Share This Info With The Person!")
        input("Press Enter To Close Terminal...")
    elif infoshareoption == "3":
        systemdump()
        print("----------------------\n"
              "Share This Info With The Person!")
        input("Press Enter To Close Terminal...")
    else:
        print("Not A Valid Option!")
        input("Press Enter To Close Terminal...")
        exit(1)


def about():
    print("----------------------\n"
          "--PAINTLOW WIN-ONLY V1.0--\n"
          "PaintLow Is A Non-Profit Project\n"
          "Made By PS. Prattay Sarkar For His Hobby.\n"
          "PaintLow Is Supposed To Be Used For Sharing System Info\n"
          "With Other Users\\Tech Enthusiasts\n"
          "So You Have An Easy Time To Give Them Debugging Info.\n"
          "PaintLow Comes With Diffrect Modes Thar Are:\n"
          "1) Minimal Data\n"
          "2) Average Data\n"
          "3) Full System Data\n"
          "Please Note That These Tools Don't Collect IPs, User Passwords, Etc.\n"
          "So Use This To Your Risk!\n"
          "----------------------")
    input("Press Enter To Close Terminal...")


if option == "1":
    print("-----------------------")
    about()
elif option == "2":
    print("-----------------------")
    infoshare()
elif option == "3":
    print("-----------------------")
    print("Sorry, But This Option Is Only For DEVs!")
    input("Press Enter To Close Terminal...")
    exit(1)
else:
    print("Invalid Option!")
    sleep(1)
    exit(1)
