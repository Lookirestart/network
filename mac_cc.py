import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interfaces", help="Interface para cambiar su MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help="Nueva MAC que queremos")
    (options, arguments) = parser.parse_args()
    if not options.interfaces:
        parser.error("[-] Por favor indicar una interface, --help para mas info")
    elif not options.new_mac:
        parser.error("[-] Por favor indicar una mac correcta, --help para mas info")
    return options


def change_mac(interfaces, new_mac):
    print("[+] Cambiando la mac de " + interfaces + " a " + new_mac)

    subprocess.call(["ifconfig", interfaces, "down"])
    subprocess.call(["ifconfig", interfaces, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interfaces, "up"])

def get_current_mac(interfaces):
    ifconfig_results = subprocess.check_output(["ifconfig", options.interfaces])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No pudimos leer la direccion MAC")



options = get_arguments()

current_mac = get_current_mac(options.interfaces)
print ("Current MAC = " + str(current_mac))

change_mac(options.interfaces,options.new_mac)

current_mac = get_current_mac(options.interfaces)
if current_mac == options.new_mac:
    print("[+] Direccion MAC cambiada a " + current_mac)
else:
    print("[-] Direccion MAC no cambiada")

