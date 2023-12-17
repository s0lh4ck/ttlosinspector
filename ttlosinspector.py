import subprocess
import platform
import re

print(""" #Created by
         ###                                     
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
            ping_result = subprocess.check_output(["ping", "-n", "1", ip_address])
        elif operating_system == "linux":
            ping_result = subprocess.check_output(["ping", "-c", "1", ip_address])
        else:
            print(f"Unsupported operating system: {operating_system}")
            return

        ttl_match = re.search(r"TTL=(\d+)", ping_result.decode('latin-1'))
        
        if ttl_match:
            ttl = int(ttl_match.group(1))
            
            if 0 < ttl <= 64:
                print(f"Detected operating system: Linux")
            elif 64 < ttl <= 128:
                print(f"Detected operating system: Windows")
            else:
                print(f"Failed to determine operating system with TTL: {ttl}")
        else:
            print("TTL not found in ping response.")
        
     

    except subprocess.CalledProcessError as e:
        print(f"Error executing ping: {e}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")
    detect_operating_system(ip_address)
