# bgp_check.py
from netmiko import ConnectHandler
import json

# Define the network device parameters
cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'YourSecurePassword123',
    'secret': 'YourEnablePassword',
}

def run_validation():
    print(f"Connecting to {cisco_router['host']}...")
    
    # Establish SSH connection
    with ConnectHandler(**cisco_router) as net_connect:
        net_connect.enable()
        
        # Execute the verification command
        print("Gathering BGP routing state...")
        bgp_output = net_connect.send_command("show ip bgp summary")
        
        # Save output to a text file for post-change comparison
        filename = f"bgp_status_{cisco_router['host']}.txt"
        with open(filename, "w") as file:
            file.write(bgp_output)
            
    print(f"✅ Validation complete. Output saved to {filename}")

if __name__ == "__main__":
    run_validation()
