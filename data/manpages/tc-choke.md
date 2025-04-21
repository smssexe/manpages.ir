TC(8)									     Linux									 TC(8)

NAME
       choke - choose and keep scheduler

SYNOPSIS
       tc qdisc ... choke limit packets min packets max packets avpkt bytes burst packets [ ecn ] [ bandwidth rate ] probability chance

DESCRIPTION
       CHOKe  (CHOose and Keep for responsive flows, CHOose and Kill for unresponsive flows) is a classless qdisc designed to both identify and penalize flows
       that monopolize the queue. CHOKe is a variation of RED, and the configuration is similar to RED.

ALGORITHM
       Once the queue hits a certain average length, a random packet is drawn from the queue. If both the to-be-queued and the drawn packet belong to the same
       flow, both packets are dropped. Otherwise, if the queue length is still below the maximum length, the new packet has a  configurable  chance  of	 being
       marked  (which  may  mean  dropped).   If the queue length exceeds max, the new packet will always be marked (or dropped).  If the queue length exceeds
       limit, the new packet is always dropped.

       The marking probability computation is the same as used by the RED qdisc.

PARAMETERS
       The parameters are the same as for RED, except that RED uses bytes whereas choke counts packets. See tc-red(8) for a description.

SOURCE
       o      R. Pan, B. Prabhakar, and K. Psounis, "CHOKe, A Stateless Active Queue Management Scheme for Approximating Fair Bandwidth Allocation", IEEE  IN‐
	      FOCOM, 2000.

       o      A. Tang, J. Wang, S. Low, "Understanding CHOKe: Throughput and Spatial Characteristics", IEEE/ACM Transactions on Networking, 2004

SEE ALSO
       tc(8), tc-red(8)

AUTHOR
       sched_choke was contributed by Stephen Hemminger.

iproute2								  August 2011									 TC(8)
