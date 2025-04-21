SYSTEMD-RC-LOCAL-GENERATOR(8)					  systemd-rc-local-generator					 SYSTEMD-RC-LOCAL-GENERATOR(8)

NAME
       systemd-rc-local-generator, rc-local.service - Compatibility generator and service to start /etc/rc.local during boot

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-rc-local-generator

       rc-local.service

DESCRIPTION
       systemd-rc-local-generator is a generator that checks whether /etc/rc.local exists and is executable, and if it is, pulls the rc-local.service unit
       into the boot process. This unit is responsible for running this script during late boot. The script is run after network.target, but in parallel with
       most other regular system services.

       Note that rc-local.service runs with slightly different semantics than the original System V version, which was executed "last" in the boot process,
       which is a concept that does not translate to systemd.

       Also note that rc-local.service is ordered after network.target, which does not mean that the network is functional, see systemd.special(7). If the
       script requires a configured network connection, it may be desirable to pull in and order it after network-online.target with a drop-in:

	   # /etc/systemd/system/rc-local.service.d/network.conf
	   [Unit]
	   Wants=network-online.target
	   After=network-online.target

       Support for /etc/rc.local is provided for compatibility with specific System V systems only. However, it is strongly recommended to avoid making use of
       this script today, and instead provide proper unit files with appropriate dependencies for any scripts to run during the boot process. Note that the
       path to the script is set at compile time and varies between distributions.

       systemd-rc-local-generator implements systemd.generator(7).

SEE ALSO
       systemd(1), systemctl(1)

systemd 255															 SYSTEMD-RC-LOCAL-GENERATOR(8)
