SYSTEMD-SYSV-GENERATOR(8)					    systemd-sysv-generator					     SYSTEMD-SYSV-GENERATOR(8)

NAME
       systemd-sysv-generator - Unit generator for SysV init scripts

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-sysv-generator

DESCRIPTION
       Note: this component is deprecated and scheduled for removal. Please replace remaining SysV init scripts with native unit files.

       systemd-sysv-generator is a generator that creates wrapper .service units for System V init[1] scripts in /etc/init.d/* at boot and when configuration
       of the system manager is reloaded. This allows systemd(1) to support them similarly to native units.

       LSB headers[2] in SysV init scripts are interpreted, and the ordering specified in the header is turned into dependencies between the generated unit
       and other units. The LSB facilities "$remote_fs", "$network", "$named", "$portmap", "$time" are supported and will be turned into dependencies on
       specific native systemd targets. See systemd.special(7) for more details.

       Note that compatibility is quite comprehensive but not 100%, for more details see Incompatibilities with SysV[3].

       SysV runlevels have corresponding systemd targets (runlevelX.target). The wrapper unit that is generated will be wanted by those targets which
       correspond to runlevels for which the script is enabled.

       systemd does not support SysV scripts as part of early boot, so all wrapper units are ordered after basic.target.

       systemd-sysv-generator implements systemd.generator(7).

SEE ALSO
       systemd(1), systemd.service(5), systemd.target(5)

NOTES
	1. System V init
	   https://savannah.nongnu.org/projects/sysvinit

	2. LSB headers
	   http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html

	3. Incompatibilities with SysV
	   https://www.freedesktop.org/wiki/Software/systemd/Incompatibilities

systemd 255															     SYSTEMD-SYSV-GENERATOR(8)
