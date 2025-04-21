PFIFO_FAST(8)								     Linux								 PFIFO_FAST(8)

NAME
       pfifo_fast - three-band first in, first out queue

DESCRIPTION
       pfifo_fast is the default qdisc of each interface.

       Whenever	 an  interface	is  created,  the  pfifo_fast  qdisc  is  automatically used as a queue. If another qdisc is attached, it preempts the default
       pfifo_fast, which automatically returns to function when an existing qdisc is detached.

       In this sense this qdisc is magic, and unlike other qdiscs.

ALGORITHM
       The algorithm is very similar to that of the classful tc-prio(8) qdisc.	pfifo_fast is like three tc-pfifo(8) queues side by side, where packets can be
       enqueued in any of the three bands based on their Type of Service bits or assigned priority.

       Not all three bands are dequeued simultaneously - as long as lower bands have traffic, higher bands are never dequeued. This can be used to  prioritize
       interactive traffic or penalize 'lowest cost' traffic.

       Each  band  can	be  txqueuelen	packets	 long, as configured with ifconfig(8) or ip(8).	 Additional packets coming in are not enqueued but are instead
       dropped.

       See tc-prio(8) for complete details on how TOS bits are translated into bands.

PARAMETERS
       txqueuelen
	      The length of the three bands depends on the interface txqueuelen, as specified with ifconfig(8) or ip(8).

BUGS
       Does not maintain statistics and does not show up in tc qdisc ls. This is because it is the automatic default in the absence of a configured qdisc.

SEE ALSO
       tc(8)

AUTHORS
       Alexey N. Kuznetsov, <kuznet@ms2.inr.ac.ru>

       This manpage maintained by bert hubert <ahu@ds9a.nl>

iproute2								10 January 2002								 PFIFO_FAST(8)
