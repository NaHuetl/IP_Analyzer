from colorama import Fore, Back, Style
import requests
import time
import getpass

try:
    banner = Fore.BLUE + """
     ___ ____       _                _
    |_ _|  _ \     / \   _ __   __ _| |_   _ _______ _ __ 
     | || |_) |   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
     | ||  __/   / ___ \| | | | (_| | | |_| |/ /  __/ |   
    |___|_|     /_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                        |___/              
        
    ░█▀█░█░█░█▀▀░█▀▀░█▀▀
    ░█▀▀░░█░░▀▀█░█▀▀░█░░
    ░▀░░░░▀░░▀▀▀░▀▀▀░▀▀▀
    """ + Style.RESET_ALL


    print(banner)
    time.sleep(2)
    print("""
        This script connect with the AbuseIPDB's API.
        You must load the IPs requested in a .txt file
        within the IP_Analyzer script path, after that you will
        need insert one APIKEY for make the request.
        (Note: You can obtain an APIKEY, loging free in the AbuseIP website.)
        """)
    time.sleep(2)

    url = "https://api.abuseipdb.com/api/v2/check"

    ip_list=[]

    api_key = getpass.getpass("Insert your AbuseIPDB account's APIKEY : ")

    print("\nStarting requests...\n")
    time.sleep(2)

    # Readin IP_list.txt
    
    with open("ip_list.txt", "r") as ip_file:
        for ip in ip_file:
            ip_list.append(ip.strip())
            
    with open("report.txt", "w") as report_file:
        for ip in ip_list:
            informacion = {
            "ipAddress" : ip,
            "maxAgeInDays" : "90"
            }

            api = {
            "Key" : api_key,
            "Accept" : "application/json"
            }
        
            respuesta = requests.get(url, headers=api, params=informacion, timeout=10)
        
            respuesta_json = respuesta.json()
        
            # Extraemos los datos relevantes
            ip = respuesta_json["data"]["ipAddress"]
            reports = respuesta_json["data"]["totalReports"]
            ipV = respuesta_json["data"]["ipVersion"]
            dns = respuesta_json["data"]["domain"]
            # abuseConfidence = respuesta_json["data"]["abuseConfidenceScor"]
            last_report_day = respuesta_json["data"]["lastReportedAt"]
        
            report_file.write(f"""
                        Querying for IP: {ip}
                        Reported {reports} times.
                        ipVersion: {ipV} .
                        Domain Name {dns}
                        Last report day: {last_report_day}
                """)
            print("Querying for IP: " + Back.BLUE + f"{ip}" + Style.RESET_ALL)
            print("Reported times: "+ Back.RED + f"{reports}"  + Style.RESET_ALL)
            print("ipVersion: " + Fore.YELLOW  + f"{ipV}" + Style.RESET_ALL)
            print("Domain Name: " + Fore.GREEN + f"{dns}" + Style.RESET_ALL)
            print("Last report day: \n" + Fore.RED + f"{last_report_day} \n" + Style.RESET_ALL)
        
    
    time.sleep(2)
    print("Report finished.\n-\n-\n-")
    
    
except KeyError:
    print("\nInvalid APYKEY. Please restar the script and insert a valid KEY.\n-\n-\n-")
except KeyboardInterrupt:
    print("The script was stoped (KeyboardInterrupt)")
    
    
    
    