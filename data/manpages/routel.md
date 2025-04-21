ROUTEL(8)								     Linux								     ROUTEL(8)

NAME
       routel - list routes with pretty output format

SYNOPSIS
       routel [ OPTIONS ] [ tablenr [ ip route options... ] ]

	OPTIONS := { -h | --help | [{-f | --family } {inet | inet6 } | -4 | -6 }

DESCRIPTION
       The routel script will list routes in a format that some might consider easier to interpret then the ip route list equivalent.

AUTHORS
       Rewritten by Stephen Hemminger <stephen@networkplumber.org>.
       Original script by Stephen R. van den Berg <srb@cuci.nl>.
       This manual page was written by Andreas Henriksson  <andreas@fatal.se>, for the Debian GNU/Linux system.

SEE ALSO
       ip(8)

iproute2								 1 Sept, 2021								     ROUTEL(8)
