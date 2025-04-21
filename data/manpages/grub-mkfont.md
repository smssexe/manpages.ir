GRUB-MKFONT(1)								 User Commands								GRUB-MKFONT(1)

NAME
       grub-mkfont - make GRUB font files

SYNOPSIS
       grub-mkfont [OPTION...] [OPTIONS] FONT_FILES

DESCRIPTION
       Convert common font file formats into PF2

       -a, --force-autohint
	      force autohint

       -b, --bold
	      convert to bold font

       -c, --asce=NUM
	      set font ascent

       -d, --desc=NUM
	      set font descent

       -i, --index=NUM
	      select face index

       --no-bitmap
	      ignore bitmap strikes when loading

       --no-hinting
	      disable hinting

       -n, --name=NAME
	      set font family name

       -o, --output=FILE
	      save output in FILE [required]

       -r, --range=FROM-TO[,FROM-TO]
	      set font range

       -s, --size=SIZE
	      set font size

       -v, --verbose
	      print verbose messages.

       -?, --help
	      give this help list

       --usage
	      give a short usage message

       -V, --version
	      print program version

       Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.

REPORTING BUGS
       Report bugs to <bug-grub@gnu.org>.

SEE ALSO
       grub-mkconfig(8)

       The  full  documentation	 for grub-mkfont is maintained as a Texinfo manual.  If the info and grub-mkfont programs are properly installed at your site,
       the command

	      info grub-mkfont

       should give you access to the complete manual.

GRUB 2.12-1ubuntu7.1							September 2024								GRUB-MKFONT(1)
