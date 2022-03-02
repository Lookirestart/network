import subprocess

def change_monitor(interface):
    print("[+] Cambiando a modo monitor " + interface)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["airmon-ng", "check", "kill"])
    subprocess.call(["iwconfig", interface, "mode", "monitor"])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["iwconfig"])


interface = raw_input("interface: ")
change_monitor(interface)
