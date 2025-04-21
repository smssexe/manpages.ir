MULTIPATHC(8)							    System Manager's Manual							 MULTIPATHC(8)

NAME
       multipathc - Interactive client for multipathd

SYNOPSIS
       multipathc [ timeout ]

DESCRIPTION
       The multipathc tool provides an interactive shell for communicating with the multipathd daemon.	The command multipathd -k invokes multipathc.

       All  commands  documented  in multipathd(8) are supported.  The available commands can be viewed by entering 'help'.  Use quit, exit, or CTRL-D to exit
       the shell.  Keywords can be abbreviated with the first letters (for example, shu for shutdown), if the abbreviation is unique.  Some  commands  support
       pretty-printing	using  printf-style  format  specifiers.  The supported format specifiers can be listed with the command show wildcards.  Depending on
       build options, the interactive shell may provide command completion and history expansion features.

       The optional parameter timeout specifies the timeout to wait for a reply from multipathd, in milliseconds. The default is 4000 ms.

SEE ALSO
       multipathd(8)

AUTHORS
       multipath-tools was developed by Christophe Varoqui <christophe.varoqui@opensvc.com> and others.

Linux									  2022-09-03								 MULTIPATHC(8)
