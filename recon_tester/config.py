important_ports = [
    20,  # FTP (Data)
    21,  # FTP (Control)
    22,  # SSH
    23,  # Telnet
    25,  # SMTP
    53,  # DNS
    67,  # DHCP (Server)
    68,  # DHCP (Client)
    80,  # HTTP
    110, # POP3
    123, # NTP
    137, # NetBIOS Name Service
    138, # NetBIOS Datagram Service
    139, # NetBIOS Session Service
    143, # IMAP
    161, # SNMP
    162, # SNMP Trap
    179, # BGP
    389, # LDAP
    443, # HTTPS
    445, # SMB/CIFS
    465, # SMTP over SSL
    514, # Syslog
    587, # SMTP over TLS
    993, # IMAP over SSL
    995, # POP3 over SSL
    1080,# SOCKS Proxy
    1194,# OpenVPN
    1433,# Microsoft SQL Server
    1521,# Oracle Database
    3306,# MySQL
    3389,# Remote Desktop Protocol (RDP)
    5432,# PostgreSQL
    5900,# VNC
    6379,# Redis
    8080,# HTTP Alternate
    8443,# HTTPS Alternate
    9200,# Elasticsearch
    27017 # MongoDB
]

important_ports_dict = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB/CIFS",
    465: "SMTP over SSL",
    514: "Syslog",
    587: "SMTP over TLS",
    993: "IMAP over SSL",
    995: "POP3 over SSL",
    1080: "SOCKS Proxy",
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    3306: "MySQL",
    3389: "Remote Desktop Protocol (RDP)",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate",
    9200: "Elasticsearch",
    27017: "MongoDB"
}