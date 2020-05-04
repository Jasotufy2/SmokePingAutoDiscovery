import os, re, subprocess, time, random

def getSubnets():
    output = str(subprocess.check_output("ifconfig", shell=True))
    lines = output.split("\n")
    current_addresses = []
    for i in range(len(lines)):
        if lines[i][0:13] == "        inet ":
            split_text = lines[i].split("inet ")
            final_text = split_text[1].split(" ")
	    if final_text[0] == "127.0.0.1":
		continue
	    else:
            	current_addresses.append(final_text[0])
    return current_addresses

def networkScanner(current_networks):
	devices = []
	for i in range(len(current_networks)):
		if str(current_networks[i]) == "10.0.75.1" or str(current_networks[i]) == "192.168.56.1" or str(current_networks[i]) == "192.168.164.193" or str(current_networks[i]) == "127.0.0.1":
			continue
		else:
			devices = devices + nmapScan(current_networks[i])
	return devices

def nmapScan(network):
	network_devices = []
	device_name = []
	network_address = network.rsplit('.', 1)
	scan = "nmap -sP -n " + network_address[0] +".1-255"
	output = str(subprocess.check_output(scan, shell=True))
	lines = output.split("\n")
	for i in range(len(lines)):
		if lines[i][:6] == "Nmap s":
			if lines[i][21:] == network:
				continue
			else:
				network_devices.append(lines[i][21:])
		if lines[i][:3] == "MAC":
			mac_address = lines[i].split(': ', 1)
			final_address = str(mac_address[1]).split(' ' , 1)
			device_name.append(final_address[0])
	final_device_details = [device_name, network_devices]
	return final_device_details

def sortInformtation(current_networks, current_devices):
	address_range = current_networks
	device_info = current_devices
	count = 0
	final_list = []
	counter = 1
	while counter < int(len(device_info)):
		final_list.append([address_range[count].rsplit(".", 1)[0]])
		for i in range(len(device_info[counter])):
			final_list[count].append(str(device_info[counter][i] + "-" + device_info[counter-1][i]))
		counter = counter + 2
		count = count + 1

	return final_list

def smokepingTargets(current_networks, current_devices):
	sortedInfo = sortInformtation(current_networks, current_devices)
	base_contents = """*** Targets ***

probe = FPing

menu = Top
title = Network Latency Grapher
remark = Welcome to the SmokePing website of xxx Company. \\
	    Here you will learn all about the latency of our network.\n\n"""

	menu_contents = """\n\n+ {0}0

menu = {1}
title = {1}.0-255 Network\n"""

	device_contents = """\n\n++ {0}

menu = {1}
title = {1} - {2}
host = {2}\n"""

	file1 = open("Targets", "w")
	file1.writelines(base_contents)
	memory = []
	for i in range(len(sortedInfo)):
		for x in range(len(sortedInfo[i])):
			if x == 0:
				file1.writelines(menu_contents.format(sortedInfo[i][x].replace(".", ""), sortedInfo[i][x]))
			else:
				ip_address = sortedInfo[i][x].split("-")[0]
				mac_address = sortedInfo[i][x].split("-")[1]
				if mac_address in memory:
					print("Dupilcate.")
					continue
				file1.writelines(device_contents.format(mac_address.replace(":", ""), mac_address, ip_address))
				memory.append(mac_address)
	file1.close()
	print("File has been written.")


def main():
	while True:
		current_devices = []
		current_networks = getSubnets()
		current_devices = networkScanner(current_networks)
		smokepingTargets(current_networks, current_devices)
		os.system("sudo service smokeping reload")
		time.sleep(120)#900 (15m)

main()
