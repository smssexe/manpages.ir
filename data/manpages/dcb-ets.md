DCB-ETS(8)								     Linux								    DCB-ETS(8)

NAME
       dcb-ets - show / manipulate ETS (Enhanced Transmission Selection) settings of the DCB (Data Center Bridging) subsystem

SYNOPSIS
       dcb [ OPTIONS ] ets { COMMAND | help }

       dcb ets show dev DEV [ willing ] [ ets-cap ] [ cbs ] [ tc-tsa ] [ reco-tc-tsa ] [ pg-bw ] [ tc-bw ] [ reco-tc-bw ] [ prio-tc ] [ reco-prio-tc ]

       dcb ets set dev DEV [ willing { on | off } ] [ { tc-tsa | reco-tc-tsa } TSA-MAP ] [ { pg-bw | tc-bw | reco-tc-bw } BW-MAP ] [ { prio-tc | reco-prio-tc
	       } PRIO-MAP ]

       TSA-MAP := [ TSA-MAP ] TSA-MAPPING

       TSA-MAPPING := { TC | all }:{ strict | cbs | ets | vendor }

       BW-MAP := [ BW-MAP ] BW-MAPPING

       BW-MAPPING := { TC | all }:INTEGER

       PRIO-MAP := [ PRIO-MAP ] PRIO-MAPPING

       PRIO-MAPPING := { PRIO | all }:TC

       TC := { 0 .. 7 }

       PRIO := { 0 .. 7 }

DESCRIPTION
       dcb ets is used to configure Enhanced Transmission Selection attributes through Linux DCB (Data Center Bridging) interface. ETS permits configuration
       of mapping of priorities to traffic classes, traffic selection algorithm to use per traffic class, bandwidth allocation, etc.

       Two DCB TLVs are related to the ETS feature: a configuration and recommendation values. Recommendation values are named with a prefix reco-, while the
       configuration ones have plain names.

PARAMETERS
       For read-write parameters, the following describes only the write direction, i.e. as used with the set command. For the show command, the parameter
       name is to be used as a simple keyword without further arguments. This instructs the tool to show the value of a given parameter. When no parameters
       are given, the tool shows the complete ETS configuration.

       ets-cap
	      A read-only property that shows the number of supported ETS traffic classes.

       cbs    A read-only property that is enabled if the driver and the hardware support the CBS Transmission Selection Algorithm.

       willing { on | off }
	      Whether local host should accept configuration from peer TLVs.

       prio-tc PRIO-MAP
       reco-prio-tc PRIO-MAP
	      PRIO-MAP	uses  the array parameter syntax, see dcb(8) for details. Keys are priorities, values are traffic classes. For each priority sets a TC
	      where traffic with that priority is directed to.

       tc-tsa TSA-MAP
       reco-tc-tsa TSA-MAP
	      TSA-MAP uses the array parameter syntax, see dcb(8) for details. Keys are TCs, values are Transmission Selection Algorithm  (TSA)	 keywords  de‐
	      scribed  below.  For  each TC sets an algorithm used for deciding how traffic queued up at this TC is scheduled for transmission. Supported TSAs
	      are:

	      strict - for strict priority, where traffic in higher-numbered TCs always takes precedence over traffic in lower-numbered TCs.
	      ets - for Enhanced Traffic Selection, where available bandwidth is distributed among the ETS-enabled TCs according to the weights set  by	 tc-bw
	      and reco-tc-bw, respectively.
	      cbs - for Credit Based Shaper, where traffic is scheduled in a strict manner up to the limit set by a shaper.
	      vendor - for vendor-specific traffic selection algorithm.

       tc-bw BW-MAP
       reco-tc-bw BW-MAP
	      BW-MAP  uses  the	 array parameter syntax, see dcb(8) for details. Keys are TCs, values are integers representing percent of available bandwidth
	      given to the traffic class in question. The value should be 0 for TCs whose TSA is not ets, and the sum of all values shall be 100. As an excep‐
	      tion to the standard wording, a configuration with no ets TCs is permitted to sum up to 0 instead.

       pg-bw BW-MAP
	      The precise meaning of pg-bw is not standardized, but the assumption seems to be that the same scheduling process as on the transmit side is ap‐
	      plicable on receive side as well, and configures receive bandwidth allocation for ets ingress traffic classes (priority groups).

EXAMPLE & USAGE
       Configure ETS priomap in a one-to-one fashion:

       # dcb ets set dev eth0 prio-tc 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7

       Set TSA and transmit bandwidth configuration:

       # dcb ets set dev eth0 tc-tsa all:strict 0:ets 1:ets 2:ets \
			      tc-bw all:0 0:33 1:33 2:34

       Show what was set:

       # dcb ets show dev eth0 prio-tc tc-tsa tc-bw
       prio-tc 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
       tc-tsa 0:ets 1:ets 2:ets 3:strict 4:strict 5:strict 6:strict 7:strict
       tc-bw 0:33 1:33 2:34 3:0 4:0 5:0 6:0 7:0

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       dcb(8)

REPORTING BUGS
       Report any bugs to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.	  You  do  not
       have to be subscribed to the list to send a message there.

AUTHOR
       Petr Machata <me@pmachata.org>

iproute2								19 October 2020								    DCB-ETS(8)
