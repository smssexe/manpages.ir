CPUPOWER-IDLE-INFO(1)							cpupower Manual							 CPUPOWER-IDLE-INFO(1)

NAME
       cpupower-idle-info - Utility to retrieve cpu idle kernel information

SYNTAX
       cpupower [ -c cpulist ] idle-info [options]

DESCRIPTION
       A tool which prints out per cpu idle information helpful to developers and interested users.

OPTIONS
       -f --silent
	      Only print a summary of all available C-states in the system.

       -e --proc
	      deprecated.   Prints  out idle information in old /proc/acpi/processor/*/power format. This interface has been removed from the kernel for quite
	      some time, do not let further code depend on this option, best do not use it.

IDLE-INFO DESCRIPTIONS
       CPU sleep state statistics and descriptions are retrieved from sysfs files, exported by the cpuidle kernel subsystem. The  kernel  only	updates	 these
       statistics  when	 it  enters  or leaves an idle state, therefore on a very idle or a very busy system, these statistics may not be accurate. They still
       provide a good overview about the usage and availability of processor sleep states on the platform.

       Be aware that the sleep states as exported by the hardware or BIOS and used by the Linux kernel may not exactly reflect the capabilities of the proces‐
       sor. This often is the case on the X86 architecture when the acpi_idle driver is used. It is also possible that the hardware overrules the  kernel  re‐
       quests,	due to internal activity monitors or other reasons.  On recent X86 platforms it is often possible to read out hardware registers which monitor
       the duration of sleep states the processor resided in. The cpupower monitor tool (cpupower-monitor(1)) can be used to show real	sleep  state  residen‐
       cies. Please refer to the architecture specific description section below.

IDLE-INFO ARCHITECTURE SPECIFIC DESCRIPTIONS
   X86
       POLL idle state

       If  cpuidle is active, X86 platforms have one special idle state.  The POLL idle state is not a real idle state, it does not save any power. Instead, a
       busy-loop is executed doing nothing for a short period of time. This state is used if the kernel knows that work has to be processed very soon and  en‐
       tering any real hardware idle state may result in a slight performance penalty.

       There exist two different cpuidle drivers on the X86 architecture platform:

       "acpi_idle" cpuidle driver

       The  acpi_idle cpuidle driver retrieves available sleep states (C-states) from the ACPI BIOS tables (from the _CST ACPI function on recent platforms or
       from the FADT BIOS table on older ones).	 The C1 state is not retrieved from ACPI tables. If the C1 state is entered, the kernel will call the hlt  in‐
       struction (or mwait on Intel).

       "intel_idle" cpuidle driver

       In kernel 2.6.36 the intel_idle driver was introduced.  It only serves recent Intel CPUs (Nehalem, Westmere, Sandybridge, Atoms or newer). On older In‐
       tel  CPUs  the  acpi_idle driver is still used (if the BIOS provides C-state ACPI tables).  The intel_idle driver knows the sleep state capabilities of
       the processor and ignores ACPI BIOS exported processor sleep states tables.

REMARKS
       By default only values of core zero are displayed. How to display settings of other cores is described in the cpupower(1) manpage in the	 --cpu	option
       section.

REFERENCES
       https://uefi.org/specifications

FILES
       /sys/devices/system/cpu/cpu*/cpuidle/state*
       /sys/devices/system/cpu/cpuidle/*

AUTHORS
       Thomas Renninger <trenn@suse.de>

SEE ALSO
       cpupower(1), cpupower-monitor(1), cpupower-info(1), cpupower-set(1), cpupower-idle-set(1)

									      0.1							 CPUPOWER-IDLE-INFO(1)
