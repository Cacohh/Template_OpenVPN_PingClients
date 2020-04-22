# Template OpenVPN Ping Clients

Template for monitoring ping availability and latency of connected clients using fping tool. The project uses python 3 scripts, although seems to work well with the version 2.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development, testing and production purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to run the scripts and commands. (Consult the documentation of your system to install dependencies if is not already installed on in your system.)

```
sed
egrep
grep
cut
fping
```
Your OpenVPN deployment need to have a status log file to obtain the informations needed. Add the following line in your openvpn server config file. Example: (Default in linux: /etc/openvpn/server.conf )
```
status /var/log/openvpn-status.log
```
and given the rith permissions for the zabbix user could read the status file. Example:
```
chmod 644 /var/log/openvpn-status.log
```
### Installing

Clone the repository to your machine, and enter in it. After, create a "scripts" folder in your zabbix-agent configuration folder. Example: (Default in linux: /etc/zabbix/. Change accordingly with your OS default.)

```
mkdir /etc/zabbix/scripts
```

Then, copy the scripts to te folder. Example:

```
cp ./Template_OpenVPN_PingClients/scripts/* /etc/zabbix/scripts
```
Copy the userparameters files to the zabbix_agentd.d folder. Example:

```
cp ./Template_OpenVPN_PingClients/userparameter_* /etc/zabbix/zabbix_agentd.d/
```
Restart the zabbix-agent in your system. Example: (Debian like systems.) 

```
/etc/init.d/zabbix-agent restart
```

After that, import the template file "template_OpenVPN_PingClients.xml" in your zabbix server frontend, and see your recent data coming.


## Details about Deployment

The discovery item parameters can be configured in script file itself and in the respective fields. Adjust accordingly with your system and preferences. 

The Zabbix template has 3 items in the two userparameters file. Details about below:
// userparameter_discovery_openvpn_clients.conf
* openvpn.discoveryClients - Discover client common name and internal ip for pings tests in the status log file. Edit the script "discovery_openvpn_clients.py"
, in the "scripts" folder. The file has the fields that could be changed, and comments to help you.
//userparameter_ping.conf
* PingCheck[<IP>] - Return if the specified ip given as argument is available thought ICMP ping request.
* PingLatency[<IP>] - Return the latency in "ms" of the specified ip given as argument, accordlying with the ICMP request and reply test.

## Comments of the Author

This project was developed and tested until now in PFSense 2.4.4-RELEASE-p3. Some details is omitted, like the different path for zabbix config files, and the "Include" parameter for the userparameters
files in "zabbix_agentd.conf" file. Although steps here is written with PFSense, FreeBSD and Debian like systems in mind, probably work in others unix like systems, with the appropriate workarounds and adjusts.

Let me know if you have some problem, or the workarounds and improvements that you made in your environment!

## Built With

* [Zabbix 4.2](https://www.zabbix.com/documentation/4.2/manual) - The IT monitoring tool 
* [Python 3](https://www.python.org/) - A nice language to programming

## Authors

* **Caio Jorge** -  [Cacohh](https://github.com/Cacohh/)