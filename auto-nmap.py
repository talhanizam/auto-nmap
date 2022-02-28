import nmap3
from colorama import Fore, init
import json

init(autoreset=True)

nmap = nmap3.Nmap()
nmapscan = nmap3.NmapScanTechniques()


def top_port_scan(target) :
    results_top_port_scan = nmap.scan_top_ports(target)
    print(Fore.CYAN + json.dumps(results_top_port_scan , indent=4 , sort_keys=True))

def os_detection(target) :
    results_os_detection = nmap.nmap_os_detection(target);
    print(Fore.CYAN + json.dumps(results_os_detection , indent=4 , sort_keys=True)) #MUST BE ROOT

def ver_detection(target):
    results_version_detection = nmap.nmap_version_detection(target)
    print(Fore.CYAN + json.dumps(results_version_detection , indent=4 , sort_keys=True)) #MUST BE ROOT

def tcp_scan(target):
    results_tcp_scan = nmapscan.nmap_tcp_scan(target)
    print(Fore.CYAN + json.dumps(results_tcp_scan , indent=4 , sort_keys=True))

def udp_scan(target):
    results_udp_scan = nmapscan.nmap_udp_scan(target)
    print(Fore.CYAN + json.dumps(results_udp_scan , indent=4 , sort_keys=True))

print(Fore.MAGENTA + """
////////////////////////////////////////
/                                      /
/                                      /
/              AUTO-NMAP               /
/                                      /
/                                      /
////////////////////////////////////////
""")

target = input(Fore.GREEN + "[+] Enter the target you want to scan : ")

ch = int(input(Fore.YELLOW + """
    CHOOSE FROM THE FOLLOWING SCAN OPTIONS
    [1] COMMON PORT SCAN
    [2] TCP SCAN ( -Ss )
    [3] UDP SCAN ( -Su )
    [4] OS DETECTION ( -O )
    [5] VERSION DETECTION ( -Sv ) : """))

if ch==1:
    top_port_scan(target)
elif ch==2:
    tcp_scan(target)
elif ch==3:
    udp_scan(target)
elif ch==4:
    os_detection(target)
elif ch==5:
    ver_detection(target)
else:
    print(Fore.RED + "INVALID OPTION")
