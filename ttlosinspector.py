import subprocess
import platform

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

        ttl_index = ping_result.find(b"TTL=")
        
        if ttl_index != -1:
            ttl = int(ping_result[ttl_index + 4:ttl_index + 7].decode())
            
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