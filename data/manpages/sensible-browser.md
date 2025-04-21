SENSIBLE-BROWSER(1)						    General Commands Manual						   SENSIBLE-BROWSER(1)

NAME
       sensible-browser - sensible web browsing

SYNOPSIS
       sensible-browser url

DESCRIPTION
       sensible-browser makes sensible decisions on which web browser to call.	Programs in Debian can use this script as their default web browser or emulate
       their behavior.
       BROWSER	environment  variable  could be set, and will be used if set.  Any string acceptable as a command_string operand to the sh -c command shall be
       valid (this is the same behavior of the EDITOR variable as documented in environ(7)).

SEE ALSO
       environ(7)

STANDARD
       Documentation of behavior of sensible-utils under  a  debian  system  is	 available  under  section  11.4  of  debian-policy  usually  installed	 under
       /usr/share/doc/debian-policy (you might need to install debian-policy)

Debian									  12 Jan 2020							   SENSIBLE-BROWSER(1)
