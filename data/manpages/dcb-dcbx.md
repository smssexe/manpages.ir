DCB-DCBX(8)								     Linux								   DCB-DCBX(8)

NAME
       dcb-dcbx - show / manipulate port DCBX (Data Center Bridging eXchange)

SYNOPSIS
       dcb [ OPTIONS ] dcbx { COMMAND | help }

       dcb dcbx show dev DEV

       dcb dcbx set dev DEV [ host ] [ lld-managed ] [ cee ] [ ieee ] [ static ]

DESCRIPTION
       Data Center Bridging eXchange (DCBX) is a protocol used by DCB devices to exchange configuration information with directly connected peers. The Linux
       DCBX object is a 1-byte bitfield of flags that configure whether DCBX is implemented in the device or in the host, and which version of the protocol
       should be used.	dcb dcbx is used to access the per-port Linux DCBX object.

       There are two principal modes of operation: in host mode, DCBX protocol is implemented by the host LLDP agent, and the DCB interfaces are used to prop‐
       agate the negotiate parameters to capable devices. In lld-managed mode, the configuration is handled by the device, and DCB interfaces are used for in‐
       spection of negotiated parameters, and can also be used to set initial parameters.

PARAMETERS
       When used with dcb dcbx set, the following keywords enable the corresponding configuration. The keywords that are not mentioned on the command line are
       considered disabled. When used with show, each enabled feature is shown by its corresponding keyword.

       host
       lld-managed
	      The  device  is  in  the host mode of operation and, respectively, the lld-managed mode of operation, as described above. In principle these two
	      keywords are mutually exclusive, but dcb dcbx allows setting both and lets the driver handle it as appropriate.

       cee
       ieee   The device supports CEE (Converged Enhanced Ethernet) and, respectively, IEEE version of the DCB specification. Typically only one of these will
	      be set, but dcb dcbx does not mandate this.

       static indicates the engine supports static configuration. No actual negotiation is performed, negotiated parameters are always the initial  configura‐
	      tion.

EXAMPLE & USAGE
       Put the DCB engine into the "host" mode of operation, and use IEEE-standardized DCB interfaces:

       # dcb dcbx set dev eth0 host ieee

       Show what was set:

       # dcb dcbx show dev eth0
       host ieee

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       dcb(8)

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Petr Machata <me@pmachata.org>

iproute2							       13 December 2020								   DCB-DCBX(8)
