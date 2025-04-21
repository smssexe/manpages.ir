PBFIFO(8)								     Linux								     PBFIFO(8)

NAME
       pfifo - Packet limited First In, First Out queue

       bfifo - Byte limited First In, First Out queue

SYNOPSIS
       tc qdisc ... add pfifo [ limit packets ]

       tc qdisc ... add bfifo [ limit bytes ]

DESCRIPTION
       The  pfifo and bfifo qdiscs are unadorned First In, First Out queues. They are the simplest queues possible and therefore have no overhead.  pfifo con‐
       strains the queue size as measured in packets.  bfifo does so as measured in bytes.

       Like all non-default qdiscs, they maintain statistics. This might be a reason to prefer pfifo or bfifo over the default.

ALGORITHM
       A list of packets is maintained, when a packet is enqueued it gets inserted at the tail of a list. When a packet needs to be sent out to	 the  network,
       it is taken from the head of the list.

       If the list is too long, no further packets are allowed on. This is called 'tail drop'.

PARAMETERS
       limit  Maximum  queue  size. Specified in bytes for bfifo, in packets for pfifo. For pfifo, defaults to the interface txqueuelen, as specified with if‐
	      config(8) or ip(8).  The range for this parameter is [0, UINT32_MAX].

	      For bfifo, it defaults to the txqueuelen multiplied by the interface MTU.	 The range for this parameter is [0, UINT32_MAX] bytes.

	      Note: The link layer header was considered when counting packets length.

OUTPUT
       The output of tc -s qdisc ls contains the limit, either in packets or in bytes, and the number of bytes	and  packets  actually	sent.  An  unsent  and
       dropped packet only appears between braces and is not counted as 'Sent'.

       In  this	 example,  the	queue length is 100 packets, 45894 bytes were sent over 681 packets.  No packets were dropped, and as the pfifo queue does not
       slow down packets, there were also no overlimits:

       # tc -s qdisc ls dev eth0
       qdisc pfifo 8001: dev eth0 limit 100p
	Sent 45894 bytes 681 pkts (dropped 0, overlimits 0)

       If a backlog occurs, this is displayed as well.

SEE ALSO
       tc(8)

AUTHORS
       Alexey N. Kuznetsov, <kuznet@ms2.inr.ac.ru>

       This manpage maintained by bert hubert <ahu@ds9a.nl>

iproute2								10 January 2002								     PBFIFO(8)
