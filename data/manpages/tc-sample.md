Packet sample action in tc(8)						     Linux						 Packet sample action in tc(8)

NAME
       sample - packet sampling tc action

SYNOPSIS
       tc ... action sample rate RATE group GROUP [ trunc SIZE ] [ index INDEX ]

       tc ... action sample index INDEX

DESCRIPTION
       The sample action allows sampling packets matching classifier.

       The  packets  are chosen randomly according to the rate parameter, and are sampled using the psample generic netlink channel. The user can also specify
       packet truncation to save user-kernel traffic. Each sample includes some informative metadata about the original packet, which is  sent	using  netlink
       attributes, alongside the original packet data.

       The  user  can  either  specify the sample action parameters as presented in the first form above, or use an existing sample action using its index, as
       presented in the second form.

SAMPLED PACKETS METADATA FIELDS
       The metadata are delivered to userspace applications using the psample generic netlink channel, where each sample includes the  following  netlink  at‐
       tributes:

       PSAMPLE_ATTR_IIFINDEX
	      The input interface index of the packet, if there is one.

       PSAMPLE_ATTR_OIFINDEX
	      The output interface index of the packet. This field is not relevant on ingress sampling

       PSAMPLE_ATTR_ORIGSIZE
	      The size of the original packet (before truncation)

       PSAMPLE_ATTR_SAMPLE_GROUP
	      The psample group the packet was sent to

       PSAMPLE_ATTR_GROUP_SEQ
	      A sequence number of the sampled packet. This number is incremented with each sampled packet of the current psample group

       PSAMPLE_ATTR_SAMPLE_RATE
	      The rate the packet was sampled with

OPTIONS
       rate RATE
	      The packet sample rate.  RATE is the expected ratio between observed packets and sampled packets. For example, RATE of 100 will lead to an aver‐
	      age of one sampled packet out of every 100 observed.

       trunc SIZE
	      Upon set, defines the maximum size of the sampled packets, and causes truncation if needed

       group GROUP
	      The  psample group the packet will be sent to. The psample module defines the concept of groups, which allows the user to match specific sampled
	      packets in the case of multiple sampling rules, thus identify only the packets that came from a specific rule.

       index INDEX
	      Is a unique ID for an action. When creating new action instance, this parameter allows one to set the new action index. When using existing  ac‐
	      tion, this parameter allows one to specify the existing action index.  The index must 32bit unsigned integer greater than zero.

EXAMPLES
       Sample one of every 100 packets flowing into interface eth0 to psample group 12:

	      tc qdisc add dev eth0 handle ffff: ingress
	      tc filter add dev eth0 parent ffff: matchall \
		   action sample rate 100 group 12 index 19

       Use the same action instance to sample eth1 too:

	      tc qdisc add dev eth1 handle ffff: ingress
	      tc filter add dev eth1 parent ffff: matchall \
		   action sample index 19

SEE ALSO
       tc(8), tc-matchall(8) psample(1)

iproute2								  31 Jan 2017						 Packet sample action in tc(8)
