PASTEBINIT(1)								 User Commands								 PASTEBINIT(1)

NAME
       pastebinit - command-line pastebin client

SYNOPSIS

       pastebinit [OPTION...] [FILE...]

DESCRIPTION
       This manual page documents briefly the pastebinit commands.

       pastebinit reads text and sends it to a "pastebin" on the internet, returning the URL to the user.

       It allows the text to be passed through a pipe (|) or from files as arguments.

OPTIONS
   General arguments
       -b [pastebin] (default is distro-specific with a fallback to dpaste.com)

       -i [input file]

       -l List all supported pastebins

       -E Print the content to stdout too

       -h Print the help screen

       -v Print the version number

       -V Print verbose output to stderr

   Optional arguments (not supported by all pastebins)
       -a [author] (default: $USER)

       -t [title of paste] (default: none)

       -f [format of paste] (default: text)

       -j [jabberid] (default: none)

       -m [permatag] (default: none)

       -P [private level] (default: 1)

       -u [username] (default: none)

       -p [password] (default: none)

CONFIGURATION FILES
       If a ~/.pastebinit.xml file is found in the user's home directory, pastebinit will use it for its configuration.

       Here's an example file:

	   <pastebinit>
	       <pastebin>paste.ubuntu.com</pastebin>
	       <author>Stephane Graber</author>
	       <jabberid>stgraber@stgraber.org</jabberid>
	       <format>text</format>
	       <private>1</private>
	   </pastebinit>

       Similarly, pastebin configuration files can be put under a ~/.pastebin.d directory to override the specific options of those.

       XDG config and data locations are also supported for these two.

AUTHORS
       pastebinit is currently written by Stephane Graber.

       username, password, format, title, arguments and redirect support added by Daniel Bartlett.

       Website: https://launchpad.net/pastebinit

       E-mail: stgraber@ubuntu.com

COPYRIGHT
       Copyright © 2007-2014 Stephane Graber

pastebinit								August 26, 2022								 PASTEBINIT(1)
