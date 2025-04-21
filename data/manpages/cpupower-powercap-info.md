CPUPOWER-POWERCAP-INFO(1)						cpupower Manual						     CPUPOWER-POWERCAP-INFO(1)

NAME
       cpupower-powercap-info - Shows powercapping related kernel and hardware configurations

SYNOPSIS
       cpupower powercap-info

DESCRIPTION
       cpupower	 powercap-info	 shows	kernel powercapping subsystem information.  This needs hardware support and a loaded powercapping driver (at this time
       only intel_rapl driver exits) exporting hardware values userspace via sysfs.

       Some options are platform wide, some affect single cores. By default values of core zero are displayed only. cpupower --cpu all cpuinfo will  show  the
       settings of all cores, see cpupower(1) how to choose specific cores.

DOCUMENTATION
       kernel sources: Documentation/power/powercap/powercap.rst

SEE ALSO
       cpupower(1)

									  05/08/2016						     CPUPOWER-POWERCAP-INFO(1)
