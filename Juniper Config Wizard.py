#!/usr/bin/python3


print("Juniper Configuration Wizard")


hostname = input("What is the hostname of the device? ")
loopback_ip = input("What is the router ID/Loopback IP? ")
autonomous_system_number = input("What is your autonomous system number? ")
core_interfaces = input("What are your core facing interfaces? ")
router_type = input("Is this a P router PE router or RR? ")

while True:
    # Ask the user what IGP will be running in the core
    igp = input("What IGP will be running in the core? ISIS or OSPF: ")

    # Normilize the input
    igp = igp.strip().lower()

    # Input validation
    if igp in ["isis", "ospf"]:
        break
    else:
        print("Invalid selection. Please enter ISIS or OSPF")

# Set the file to save configuration to
filename = "juniper_config.conf"

# Write the Hostname Config
with open(filename, "w") as file:
    file.write(f"set system host-name {hostname}\n")

    # Write the router ID Config
    file.write(f"set routing-options router-id {loopback_ip}\n")

    # Write Autonomous system number
    file.write(f"set routing-options autonomous-system {autonomous_system_number}\n")

    # Write the Loopback IP Config
    file.write(f"set interfaces lo0.0 family inet address {loopback_ip}\n")

    # Set IGP on the loopback interface
    if igp == "isis":
        file.write(f"set protocols isis interface lo0.0 passive\n")
    else:
        file.write(f"set protocols ospf area 0 interface lo0.0 passive\n")

    file.write(f"set protocols mpls interfaces all\n")
    file.write(f"set protocols ldp interfaces all\n")

    
    
    



print(f"Configuration file created {filename}")


