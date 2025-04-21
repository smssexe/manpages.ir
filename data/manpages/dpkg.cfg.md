dpkg.cfg(5)								  dpkg suite								   dpkg.cfg(5)

NAME
       dpkg.cfg - dpkg configuration file

DESCRIPTION
       This file contains default options for dpkg.  Each line contains a single option which is exactly the same as a normal command line option for dpkg
       except for the leading hyphens which are not used here.	Quotes surrounding option values are stripped.	Comments are allowed by starting a line with a
       hash sign (‘#’).

FILES
       /etc/dpkg/dpkg.cfg.d/[0-9a-zA-Z_-]*

       /etc/dpkg/dpkg.cfg

       ~/.dpkg.cfg

SEE ALSO
       dpkg(1).

1.22.6									  2024-07-17								   dpkg.cfg(5)
