CPUPOWER-FREQUENCY-SET(1)						cpupower Manual						     CPUPOWER-FREQUENCY-SET(1)

NAME
       cpupower-frequency-set - A small tool which allows to modify cpufreq settings.

SYNTAX
       cpupower [ -c cpu ] frequency-set [options]

DESCRIPTION
       cpupower	 frequency-set	allows you to modify cpufreq settings without having to type e.g. "/sys/devices/system/cpu/cpu0/cpufreq/scaling_set_speed" all
       the time.

OPTIONS
       -d --min <FREQ>
	      new minimum CPU frequency the governor may select.

       -u --max <FREQ>
	      new maximum CPU frequency the governor may select.

       -g --governor <GOV>
	      new cpufreq governor.

       -f --freq <FREQ>
	      specific frequency to be set. Requires userspace governor to be available and loaded.

       -r --related
	      modify all hardware-related CPUs at the same time

       REMARKS

       By default values are applied on all cores. How to modify single core configurations is described in the cpupower(1) manpage in the --cpu  option  sec‐
       tion.

       The -f FREQ, --freq FREQ parameter cannot be combined with any other parameter.

       FREQuencies can be passed in Hz, kHz (default), MHz, GHz, or THz by postfixing the value with the wanted unit name, without any space (frequency in kHz
       =^ Hz * 0.001 =^ MHz * 1000 =^ GHz * 1000000).

       On Linux kernels up to 2.6.29, the -r or --related parameter is ignored.

FILES
       /sys/devices/system/cpu/cpu*/cpufreq/
       /proc/cpufreq (deprecated)
       /proc/sys/cpu/ (deprecated)

AUTHORS
       Dominik Brodowski <linux@brodo.de> - author
       Mattia Dongili<malattia@gmail.com> - first autolibtoolization

SEE ALSO
       cpupower-frequency-info(1), cpupower(1)

									      0.1						     CPUPOWER-FREQUENCY-SET(1)
