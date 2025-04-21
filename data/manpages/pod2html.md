POD2HTML(1)						       Perl Programmers Reference Guide							   POD2HTML(1)

NAME
       pod2html - convert .pod files to .html files

SYNOPSIS
	   pod2html --help --htmldir=<name> --htmlroot=<URL>
		    --infile=<name> --outfile=<name>
		    --podpath=<name>:...:<name> --podroot=<name>
		    --cachedir=<name> --flush --recurse --norecurse
		    --quiet --noquiet --verbose --noverbose
		    --index --noindex --backlink --nobacklink
		    --header --noheader --poderrors --nopoderrors
		    --css=<URL> --title=<name>

DESCRIPTION
       Converts files from pod format (see perlpod) to HTML format.

ARGUMENTS
       pod2html takes the following arguments:

       backlink
	     --backlink
	     --nobacklink

	   Turn	 =head1	 directives  into  links  pointing  to	the  top of the HTML file.  --nobacklink (which is the default behavior) does not create these
	   backlinks.

       cachedir
	     --cachedir=name

	   Specify which directory is used for storing cache. Default directory is the current working directory.

       css
	     --css=URL

	   Specify the URL of cascading style sheet to link from resulting HTML file.  Default is none style sheet.

       flush
	     --flush

	   Flush the cache.

       header
	     --header
	     --noheader

	   Create header and footer blocks containing the text of the "NAME" section.  --noheader -- which is the default behavior -- does not	create	header
	   or footer blocks.

       help
	     --help

	   Displays the usage message.

       htmldir
	     --htmldir=name

	   Sets	 the  directory	 to  which  all cross references in the resulting HTML file will be relative. Not passing this causes all links to be absolute
	   since this is the value that tells Pod::Html the root of the documentation tree.

	   Do not use this and --htmlroot in the same call to pod2html; they are mutually exclusive.

       htmlroot
	     --htmlroot=URL

	   Sets the base URL for the HTML files.  When cross-references are made, the HTML root is prepended to the URL.

	   Do not use this if relative links are desired: use --htmldir instead.

	   Do not pass both this and --htmldir to pod2html; they are mutually exclusive.

       index
	     --index

	   Generate an index at the top of the HTML file (default behaviour).

	   noindex
		 --noindex

	       Do not generate an index at the top of the HTML file.

       infile
	     --infile=name

	   Specify the pod file to convert.  Input is taken from STDIN if no infile is specified.

       outfile
	     --outfile=name

	   Specify the HTML file to create.  Output goes to STDOUT if no outfile is specified.

       poderrors
	     --poderrors
	     --nopoderrors

	   Include a "POD ERRORS" section in the outfile if there were any POD errors in the infile (default behaviour).  --nopoderrors does not  create  this
	   "POD ERRORS" section.

       podpath
	     --podpath=name:...:name

	   Specify which subdirectories of the podroot contain pod files whose HTML converted forms can be linked-to in cross-references.

       podroot
	     --podroot=name

	   Specify the base directory for finding library pods.

       quiet
	     --quiet
	     --noquiet

	   Don't  display mostly harmless warning messages.  --noquiet -- which is the default behavior -- does display these mostly harmless warning messages
	   (but this is not the same as "verbose" mode).

       recurse
	     --recurse
	     --norecurse

	   Recurse into subdirectories specified in podpath (default behaviour).  --norecurse does not recurse into these subdirectories.

       title
	     --title=title

	   Specify the title of the resulting HTML file.

       verbose
	     --verbose
	     --noverbose

	   Display progress messages. --noverbose -- which is the default behavior -- does not display these progress messages.

AUTHOR
       Tom Christiansen, <tchrist@perl.com>.

BUGS
       See Pod::Html for a list of known bugs in the translator.

SEE ALSO
       perlpod, Pod::Html

COPYRIGHT
       This program is distributed under the Artistic License.

perl v5.38.2								  2025-04-08								   POD2HTML(1)
