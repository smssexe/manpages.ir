LOADUNIMAP(8)							    System Manager's Manual							 LOADUNIMAP(8)

NAME
       loadunimap - load the kernel unicode-to-font mapping table

SYNOPSIS
       loadunimap [ -C console ] [ -o oldmap ] [ map ]

DESCRIPTION
       The  loadunimap	command	 is  obsolete - its function is now built-in into setfont(8).  However, for backwards compatibility it is still available as a
       separate command.

       The program loadunimap loads the specified map in the kernel unicode-to-font mapping table.  If no map is given def mapping table is assumed.  The  de‐
       fault extension (that can be omitted) is .uni.

       If the -o oldmap option is given, the old map is saved in the file specified.

       On Linux 2.6.1 and later one can specify the console device using the -C option.

       Usually one does not call loadunimap directly - its function is also built into setfont(8).

FILES
       /usr/share/unimaps
	      The default directory for unicode mappings.

       /usr/share/unimaps/def.uni
	      The default mapping file.

SEE ALSO
       mapscrn(8), setfont(8)

kbd									  2004-01-01								 LOADUNIMAP(8)
