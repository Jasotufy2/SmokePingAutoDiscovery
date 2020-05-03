# SmokePingAutoDiscovery
Automatic Device Discovery and Management for SmokePing Latency Manager

  !!Important Information!!
  The installation of this software is very ruimentary at this point but works well when set up. There are plans to develop this in the     near future.
  
  Supported OS: Linux: (Debian, Ubuntu)
  
  Preresiquites:
  - Configured Apache2 server
  - Python 2/3 installed
  - Clean Smokeping Installation (This program will delete any current configuration, data will be kept but you will need to manually find     this) - For move visit: https://oss.oetiker.ch/smokeping/doc/smokeping_install.en.html or, apt-get install smokeping
  
  Installation:
  - Download the SmokePingAutoDiscovery files, this can be done directly or with: 
    git clone https://github.com/Jasotufy2/SmokePingAutoDiscovery.git
  - Enter folder: cd /SmokePingAutoDiscovery
  - Move main file to Smokeping directory: mv manager.py /etc/smokeping/confg.d
  - Run SmokePingAutoDiscovery: python /etc/smokeping/config.d/manager.py
  
  Configure this command to run on startup to automate your Smokeping instance:
  python /etc/smokeping/config.d/manager.py
  
Thanks for using the program and supporting.
Ver 1.0
  
