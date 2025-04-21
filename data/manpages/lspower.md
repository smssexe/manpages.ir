LSPOWER(1)							    General Commands Manual							    LSPOWER(1)

NAME
       lspower - enumerate power sources

SYNOPSIS
       lspower

DESCRIPTION
       This program displays power sources available on this machine, and their status.

       The status is given as an icon:

       ✗      a power source that's not present or somehow disabled

       ✓      a power source that's not an (apparent) battery, that is working ok

       +      a battery that's currently charging

       •      a battery that's full or otherwise not charging

       -      a battery that's giving off its stored power

       If the charge level is known, it is displayed as well.  So are abnormal conditions such as overheating.

CAVEATS
       The output is meant only for human consumption, and is not supposed to be screen-scraped.  For a program, it's much easier to read data from the kernel
       directly (/sys/class/power_supply/*).

									  2022-08-16								    LSPOWER(1)
