proc_pid_net(5)							      File Formats Manual						       proc_pid_net(5)

NAME
       /proc/pid/net/, /proc/net/ - network layer information

DESCRIPTION
       /proc/pid/net/ (since Linux 2.6.25)
	      See the description of /proc/net.

       /proc/net/
	      This  directory contains various files and subdirectories containing information about the networking layer.  The files contain ASCII structures
	      and are, therefore, readable with cat(1).	 However, the standard netstat(8) suite provides much cleaner access to these files.

	      With the advent of network namespaces, various information relating to the network stack	is  virtualized	 (see  network_namespaces(7)).	 Thus,
	      since Linux 2.6.25, /proc/net is a symbolic link to the directory /proc/self/net, which contains the same files and directories as listed below.
	      However, these files and directories now expose information for the network namespace of which the process is a member.

       /proc/net/arp
	      This holds an ASCII readable dump of the kernel ARP table used for address resolutions.  It will show both dynamically learned and preprogrammed
	      ARP entries.  The format is:

		  IP address	 HW type   Flags     HW address		 Mask	Device
		  192.168.0.50	 0x1	   0x2	     00:50:BF:25:68:F3	 *	eth0
		  192.168.0.250	 0x1	   0xc	     00:00:00:00:00:00	 *	eth0

	      Here  "IP address" is the IPv4 address of the machine and the "HW type" is the hardware type of the address from RFC 826.	 The flags are the in‐
	      ternal flags of the ARP structure (as defined in /usr/include/linux/if_arp.h) and the "HW address" is the data link layer mapping	 for  that  IP
	      address if it is known.

       /proc/net/dev
	      The  dev	pseudo-file  contains network device status information.  This gives the number of received and sent packets, the number of errors and
	      collisions and other basic statistics.  These are used by the ifconfig(8) program to report device status.  The format is:

	      Inter-|	Receive						       |  Transmit
	       face |bytes    packets errs drop fifo frame compressed multicast|bytes	 packets errs drop fifo colls carrier compressed
		  lo: 2776770	11307	 0    0	   0	 0	    0	      0	 2776770   11307    0	 0    0	    0	    0	       0
		eth0: 1215645	 2751	 0    0	   0	 0	    0	      0	 1782404    4324    0	 0    0	  427	    0	       0
		ppp0: 1622270	 5552	 1    0	   0	 0	    0	      0	  354130    5669    0	 0    0	    0	    0	       0
		tap0:	 7714	   81	 0    0	   0	 0	    0	      0	    7714      81    0	 0    0	    0	    0	       0

       /proc/net/dev_mcast
	      Defined in /usr/src/linux/net/core/dev_mcast.c:

		  indx interface_name  dmi_u dmi_g dmi_address
		  2    eth0	       1     0	   01005e000001
		  3    eth1	       1     0	   01005e000001
		  4    eth2	       1     0	   01005e000001

       /proc/net/igmp
	      Internet Group Management Protocol.  Defined in /usr/src/linux/net/core/igmp.c.

       /proc/net/rarp
	      This file uses the same format as the arp file and contains the current reverse mapping database used to provide rarp(8) reverse address	lookup
	      services.	 If RARP is not configured into the kernel, this file will not be present.

       /proc/net/raw
	      Holds  a	dump of the RAW socket table.  Much of the information is not of use apart from debugging.  The "sl" value is the kernel hash slot for
	      the socket, the "local_address" is the local address and protocol number pair.  "St" is the internal status of the socket.  The  "tx_queue"  and
	      "rx_queue" are the outgoing and incoming data queue in terms of kernel memory usage.  The "tr", "tm->when", and "rexmits" fields are not used by
	      RAW.  The "uid" field holds the effective UID of the creator of the socket.

       /proc/net/snmp
	      This file holds the ASCII data needed for the IP, ICMP, TCP, and UDP management information bases for an SNMP agent.

       /proc/net/tcp
	      Holds  a	dump of the TCP socket table.  Much of the information is not of use apart from debugging.  The "sl" value is the kernel hash slot for
	      the socket, the "local_address" is the local address and port number pair.  The "rem_address" is the remote address and  port  number  pair  (if
	      connected).  "St" is the internal status of the socket.  The "tx_queue" and "rx_queue" are the outgoing and incoming data queue in terms of ker‐
	      nel  memory  usage.  The "tr", "tm->when", and "rexmits" fields hold internal information of the kernel socket state and are useful only for de‐
	      bugging.	The "uid" field holds the effective UID of the creator of the socket.

       /proc/net/udp
	      Holds a dump of the UDP socket table.  Much of the information is not of use apart from debugging.  The "sl" value is the kernel hash  slot  for
	      the  socket,  the	 "local_address"  is the local address and port number pair.  The "rem_address" is the remote address and port number pair (if
	      connected).  "St" is the internal status of the socket.  The "tx_queue" and "rx_queue" are the outgoing and incoming data queue in terms of ker‐
	      nel memory usage.	 The "tr", "tm->when", and "rexmits" fields are not used by UDP.  The "uid" field holds the effective UID of  the  creator  of
	      the socket.  The format is:

	      sl  local_address rem_address   st tx_queue rx_queue tr rexmits  tm->when uid
	       1: 01642C89:0201 0C642C89:03FF 01 00000000:00000001 01:000071BA 00000000 0
	       1: 00000000:0801 00000000:0000 0A 00000000:00000000 00:00000000 6F000100 0
	       1: 00000000:0201 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0

       /proc/net/unix
	      Lists the UNIX domain sockets present within the system and their status.	 The format is:

	      Num RefCount Protocol Flags    Type St Inode Path
	       0: 00000002 00000000 00000000 0001 03	42
	       1: 00000001 00000000 00010000 0001 01  1948 /dev/printer

	      The fields are as follows:

	      Num:	the kernel table slot number.

	      RefCount: the number of users of the socket.

	      Protocol: currently always 0.

	      Flags:	the internal kernel flags holding the status of the socket.

	      Type:	the  socket  type.   For  SOCK_STREAM sockets, this is 0001; for SOCK_DGRAM sockets, it is 0002; and for SOCK_SEQPACKET sockets, it is
			0005.

	      St:	the internal state of the socket.

	      Inode:	the inode number of the socket.

	      Path:	the bound pathname (if any) of the socket.  Sockets in the abstract namespace are included in the list, and are shown with a Path that
			commences with the character '@'.

       /proc/net/netfilter/nfnetlink_queue
	      This file contains information about netfilter user-space queueing, if used.  Each line represents a queue.  Queues  that	 have  not  been  sub‐
	      scribed to by user space are not shown.

		     1	 4207	  0  2 65535	 0     0	0  1
		    (1)	  (2)	 (3)(4)	 (5)	(6)   (7)      (8)

	      The fields in each line are:

	      (1)  The	ID of the queue.  This matches what is specified in the --queue-num or --queue-balance options to the iptables(8) NFQUEUE target.  See
		   iptables-extensions(8) for more information.

	      (2)  The netlink port ID subscribed to the queue.

	      (3)  The number of packets currently queued and waiting to be processed by the application.

	      (4)  The copy mode of the queue.	It is either 1 (metadata only) or 2 (also copy payload data to user space).

	      (5)  Copy range; that is, how many bytes of packet payload should be copied to user space at most.

	      (6)  queue dropped.  Number of packets that had to be dropped by the kernel because too many packets are already waiting for user space to  send
		   back the mandatory accept/drop verdicts.

	      (7)  queue  user	dropped.   Number of packets that were dropped within the netlink subsystem.  Such drops usually happen when the corresponding
		   socket buffer is full; that is, user space is not able to read messages fast enough.

	      (8)  sequence number.  Every queued packet is associated with a (32-bit) monotonically increasing sequence number.  This shows  the  ID  of  the
		   most recent packet queued.

	      The last number exists only for compatibility reasons and is always 1.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_pid_net(5)
