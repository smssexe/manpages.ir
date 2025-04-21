DCB-BUFFER(8)								     Linux								 DCB-BUFFER(8)

NAME
       dcb-buffer - show / manipulate port buffer settings of the DCB (Data Center Bridging) subsystem

SYNOPSIS
       dcb [ OPTIONS ] buffer { COMMAND | help }

       dcb buffer show dev DEV [ prio-buffer ] [ buffer-size ] [ total-size ]

       dcb buffer set dev DEV [ prio-buffer PRIO-MAP ] [ buffer-size SIZE-MAP ]

       PRIO-MAP := [ PRIO-MAP ] PRIO-MAPPING

       PRIO-MAPPING := { PRIO | all }:BUFFER

       SIZE-MAP := [ SIZE-MAP ] SIZE-MAPPING

       SIZE-MAPPING := { BUFFER | all }:SIZE

       PRIO := { 0 .. 7 }

       BUFFER := { 0 .. 7 }

       SIZE := { INTEGER | INTEGERK | INTEGERM | ... }

DESCRIPTION
       dcb buffer is used to configure assignment of traffic to port buffers based on traffic priority, and sizes of those buffers. It can be also used to in‐
       spect the current configuration, as well as total device memory that the port buffers take.

PARAMETERS
       For read-write parameters, the following describes only the write direction, i.e. as used with the set command. For the show command, the parameter
       name is to be used as a simple keyword without further arguments. This instructs the tool to show the value of a given parameter. When no parameters
       are given, the tool shows the complete buffer configuration.

       total-size
	      A	 read-only  property  that  shows  the total device memory taken up by port buffers. This might be more than a simple sum of individual buffer
	      sizes if there are any hidden or internal buffers.

       prio-buffer PRIO-MAP
	      PRIO-MAP uses the array parameter syntax, see dcb(8) for details. Keys are priorities, values are buffer	indices.  For  each  priority  sets  a
	      buffer where traffic with that priority is directed to.

       buffer-size SIZE-MAP
	      SIZE-MAP	uses the array parameter syntax, see dcb(8) for details. Keys are buffer indices, values are sizes of that buffer in bytes.  The sizes
	      can use the notation documented in section PARAMETERS at tc(8).  Note that the size requested by the tool can be rounded or capped by the driver
	      to satisfy the requirements of the device.

EXAMPLE & USAGE
       Configure the priomap in a one-to-one fashion:

       # dcb buffer set dev eth0 prio-buffer 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7

       Set sizes of all buffers to 10KB, except for buffer 6, which will have the size 1MB:

       # dcb buffer set dev eth0 buffer-size all:10K 6:1M

       Show what was set:

       # dcb buffer show dev eth0
       prio-buffer 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
       buffer-size 0:10Kb 1:10Kb 2:10Kb 3:10Kb 4:10Kb 5:10Kb 6:1Mb 7:10Kb
       total-size 1222Kb

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       dcb(8)

REPORTING BUGS
       Report any bugs to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.	  You  do  not
       have to be subscribed to the list to send a message there.

AUTHOR
       Petr Machata <me@pmachata.org>

iproute2							       12 November 2020								 DCB-BUFFER(8)
