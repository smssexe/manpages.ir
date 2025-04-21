CPUPOWER-SET(1)								cpupower Manual							       CPUPOWER-SET(1)

NAME
       cpupower-set - Set processor power related kernel or hardware configurations

SYNOPSIS
       cpupower set [ -b VAL ]

DESCRIPTION
       cpupower set  sets kernel configurations or directly accesses hardware registers affecting processor power saving policies.

       Some  options  are platform wide, some affect single cores. By default values are applied on all cores. How to modify single core configurations is de‐
       scribed in the cpupower(1) manpage in the --cpu option section. Whether an option affects the whole system or can be applied to individual cores is de‐
       scribed in the Options sections.

       Use cpupower info  to read out current settings and whether they are supported on the system at all.

Options
       --perf-bias, -b
	   Sets a register on supported Intel processore which allows software to convey its policy for the relative importance of performance	versus	energy
	   savings to the  processor.

	   The range of valid numbers is 0-15, where 0 is maximum performance and 15 is maximum energy efficiency.

	   The processor uses this information in model-specific ways when it must select trade-offs between performance and energy efficiency.

	   This policy hint does not supersede Processor Performance states (P-states) or CPU Idle power states (C-states), but allows software to have influ‐
	   ence where it would otherwise be unable to express a preference.

	   For	example,  this setting may tell the hardware how aggressively or conservatively to control frequency in the "turbo range" above the explicitly
	   OS-controlled P-state frequency range.  It may also tell the hardware how aggressively it should enter the OS requested C-states.

	   This option can be applied to individual cores only via the --cpu option, cpupower(1).

	   Setting the performance bias value on one CPU can modify the setting on related CPUs as well (for example all CPUs on one socket), because of hard‐
	   ware restrictions.  Use cpupower -c all info -b to verify.

	   This options needs the msr kernel driver (CONFIG_X86_MSR) loaded.

SEE ALSO
       cpupower-info(1), cpupower-monitor(1), powertop(1)

AUTHORS
       --perf-bias parts written by Len Brown <len.brown@intel.com>
       Thomas Renninger <trenn@suse.de>

									  22/02/2011							       CPUPOWER-SET(1)
