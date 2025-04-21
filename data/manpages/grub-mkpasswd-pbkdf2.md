GRUB-MKPASSWD-PBKDF2(1)							 User Commands						       GRUB-MKPASSWD-PBKDF2(1)

NAME
       grub-mkpasswd-pbkdf2 - generate hashed password for GRUB

SYNOPSIS
       grub-mkpasswd-pbkdf2 [OPTION...] [OPTIONS]

DESCRIPTION
       Generate PBKDF2 password hash.

       -c, --iteration-count=NUM
	      Number of PBKDF2 iterations

       -l, --buflen=NUM
	      Length of generated hash

       -s, --salt=NUM
	      Length of salt

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

       The  full  documentation	 for  grub-mkpasswd-pbkdf2  is maintained as a Texinfo manual.	If the info and grub-mkpasswd-pbkdf2 programs are properly in‐
       stalled at your site, the command

	      info grub-mkpasswd-pbkdf2

       should give you access to the complete manual.

GRUB 2.12-1ubuntu7.1							September 2024						       GRUB-MKPASSWD-PBKDF2(1)
