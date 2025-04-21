sln(8)								    System Manager's Manual								sln(8)

NAME
       sln - create symbolic links

SYNOPSIS
       sln source dest
       sln filelist

DESCRIPTION
       The  sln	 program creates symbolic links.  Unlike the ln(1) program, it is statically linked.  This means that if for some reason the dynamic linker is
       not working, sln can be used to make symbolic links to dynamic libraries.

       The command line has two forms.	In the first form, it creates dest as a new symbolic link to source.

       In the second form, filelist is a list of space-separated pathname pairs, and the effect is as if sln was executed once for each line of the file, with
       the two pathnames as the arguments.

       The sln program supports no command-line options.

SEE ALSO
       ln(1), ld.so(8), ldconfig(8)

Linux man-pages 6.7							  2023-10-31									sln(8)
