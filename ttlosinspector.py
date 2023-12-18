import subprocess
import platform
import re

print(""" #Created by:
         ###                 #                    
 ####   #   #  #      #    # #    #   ####  #    # 
#      #     # #      #    # #    #  #    # #   #  
 ####  #     # #      ###### #    #  #      ####   
     # #     # #      #    # ####### #      #  #   
#    #  #   #  #      #    #      #  #    # #   #  
 ####    ###   ###### #    #      #   ####  #    # 
      """)

def detect_operating_system(ip_address):
    operating_system = platform.system().lower()

    try:
        if operating_system == "windows":
            ping_result = subprocess.check_output(["ping", "-n", "1", ip_address], text=True, stderr=subprocess.STDOUT)
        elif operating_system == "linux":
            ping_result = subprocess.check_output(["ping", "-c", "1", ip_address], text=True, stderr=subprocess.STDOUT)
        else:
            print(f"Unsupported operating system: {operating_system}")
            return

        ttl_match = re.search(r"ttl=(\d+)|time=(\d+)", ping_result, re.IGNORECASE)

        if ttl_match:
            ttl_value = next((group for group in ttl_match.groups() if group is not None), None)
            ttl = int(ttl_value)

            if 0 < ttl <= 64:
                detected_os = "Linux"
                print(f"Detected operating system: {detected_os}")
            elif 64 < ttl <= 128:
                detected_os = "Windows"
                print(f"Detected operating system: {detected_os}")
            else:
                print(f"Failed to determine operating system with TTL: {ttl}")
        else:
            print("TTL not found in ping response.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing ping: {e}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")
    detect_operating_system(ip_address)
