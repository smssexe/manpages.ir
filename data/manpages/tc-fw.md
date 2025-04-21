Firewall mark classifier in tc(8)					     Linux					     Firewall mark classifier in tc(8)

NAME
       fw - fwmark traffic control filter

SYNOPSIS
       tc filter ... fw [ classid CLASSID ] [ action ACTION_SPEC ]

DESCRIPTION
       the  fw	filter	allows	one  to classify packets based on a previously set fwmark by iptables.	If the masked value of the fwmark matches the filter's
       masked handle, the filter matches. By default, all 32 bits of the handle and the fwmark are masked.  iptables allows one to mark	 single	 packets  with
       the  MARK  target,  or whole connections using CONNMARK.	 The benefit of using this filter instead of doing the heavy-lifting with tc itself is that on
       one hand it might be convenient to keep packet filtering and classification in one place, possibly having to match a packet just once, and on the other
       users familiar with iptables but not tc will have a less hard time adding QoS to their setups.

OPTIONS
       classid CLASSID
	      Push matching packets to the class identified by CLASSID.

       action ACTION_SPEC
	      Apply an action from the generic actions framework on matching packets.

EXAMPLES
       Take e.g. the following tc filter statement:

	      tc filter add ... handle 6 fw classid 1:1

       will match if the packet's fwmark value is 6.  This is a sample iptables statement marking packets coming in on eth0:

	      iptables -t mangle -A PREROUTING -i eth0 -j MARK --set-mark 6

       Specific bits of the packet's fwmark can be set using the skbedit action. For example, to only set one bit of the fwmark	 without  changing  any	 other
       bit:

	      tc filter add ... action skbedit mark 0x8/0x8

       The fw filter can then be used to match on this bit by masking the handle:

	      tc filter add ... handle 0x8/0x8 fw action drop

       This is useful when different bits of the fwmark are assigned different meanings.

SEE ALSO
       tc(8), iptables(8), iptables-extensions(8), tc-skbedit(8)

iproute2								  21 Oct 2015					     Firewall mark classifier in tc(8)
