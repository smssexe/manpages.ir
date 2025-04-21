POD2MAN(1)						       Perl Programmers Reference Guide							    POD2MAN(1)

NAME
       pod2man - Convert POD data to formatted *roff input

SYNOPSIS
       pod2man [--center=string] [--date=string]
	   [--encoding=encoding] [--errors=style] [--fixed=font]
	   [--fixedbold=font] [--fixeditalic=font]
	   [--fixedbolditalic=font] [--guesswork=rule[,rule...]]
	   [--name=name] [--nourls] [--official]
	   [--release=version] [--section=manext]
	   [--quotes=quotes] [--lquote=quote] [--rquote=quote]
	   [--stderr] [--utf8] [--verbose] [input [output] ...]

       pod2man --help

DESCRIPTION
       pod2man is a wrapper script around the Pod::Man module, using it to generate *roff input from POD source.  The resulting *roff code is suitable for
       display on a terminal using nroff(1), normally via man(1), or printing using troff(1).

       By default (on non-EBCDIC systems), pod2man outputs UTF-8 manual pages.	Its output should work with the man program on systems that use groff (most
       Linux distributions) or mandoc (most BSD variants), but may result in mangled output on older UNIX systems.  To choose a different, possibly more
       backward-compatible output mangling on such systems, use "--encoding=roff" (the default in earlier Pod::Man versions).  See the --encoding option and
       "ENCODING" in Pod::Man for more details.

       input is the file to read for POD source (the POD can be embedded in code).  If input isn't given, it defaults to "STDIN".  output, if given, is the
       file to which to write the formatted output.  If output isn't given, the formatted output is written to "STDOUT".  Several POD files can be processed
       in the same pod2man invocation (saving module load and compile times) by providing multiple pairs of input and output files on the command line.

       --section, --release, --center, --date, and --official can be used to set the headers and footers to use.  If not given, Pod::Man will assume various
       defaults.  See below for details.

OPTIONS
       Each option is annotated with the version of podlators in which that option was added with its current meaning.

       -c string, --center=string
	   [1.00]  Sets the centered page header for the ".TH" macro to string.	 The default is "User Contributed Perl Documentation", but also see --official
	   below.

       -d string, --date=string
	   [4.00] Set the left-hand footer string for the ".TH" macro to string.  By default, the first of POD_MAN_DATE, SOURCE_DATE_EPOCH,  the  modification
	   date	 of  the  input	 file,	or  the	 current date (if input comes from "STDIN") will be used, and the date will be in UTC.	See "CLASS METHODS" in
	   Pod::Man for more details.

       -e encoding, --encoding=encoding
	   [5.00] Specifies the encoding of the output.	 encoding must be an encoding recognized by the Encode module (see Encode::Supported).	The default on
	   non-EBCDIC systems is UTF-8.

	   If the output contains characters that cannot be represented in this encoding, that is an error that will be reported as configured by the --errors
	   option.  If error handling is other than "die", the unrepresentable character will be replaced with the  Encode  substitution  character  (normally
	   "?").

	   If  the  "encoding"	option	is  set to the special value "groff" (the default on EBCDIC systems), or if the Encode module is not available and the
	   encoding is set to anything other than "roff" (see below), Pod::Man will translate all non-ASCII characters to "\[uNNNN]" Unicode  escapes.	 These
	   are	not  traditionally part of the *roff language, but are supported by groff and mandoc and thus by the majority of manual page processors in use
	   today.

	   If encoding is set to the special value "roff", pod2man will do its historic transformation of (some) ISO 8859-1 characters into *roff escapes that
	   may be adequate in troff and may be readable (if ugly) in nroff.  This was the default behavior of versions of  pod2man  before  5.00.   With  this
	   encoding,  all  other  non-ASCII characters will be replaced with "X".  It may be required for very old troff and nroff implementations that do not
	   support UTF-8, but its representation of any non-ASCII character is very poor and often specific to European languages.  Its use is discouraged.

	   WARNING: The input encoding of the POD source is independent from the output encoding, and setting this option does not affect  the	interpretation
	   of  the POD input.  Unless your POD source is US-ASCII, its encoding should be declared with the "=encoding" command in the source.	If this is not
	   done, Pod::Simple will will attempt to guess the encoding and may be successful if it's Latin-1 or  UTF-8,  but  it	will  produce  warnings.   See
	   perlpod(1) for more information.

       --errors=style
	   [2.5.0]  Set	 the  error handling style.  "die" says to throw an exception on any POD formatting error.  "stderr" says to report errors on standard
	   error, but not to throw an exception.  "pod" says to include a POD ERRORS section in the resulting documentation summarizing	 the  errors.	"none"
	   ignores POD errors entirely, as much as possible.

	   The default is "die".

       --fixed=font
	   [1.0]  The  fixed-width  font  to  use  for verbatim text and code.	Defaults to "CW".  Some systems may want "CR" instead.	Only matters for troff
	   output.

       --fixedbold=font
	   [1.0] Bold version of the fixed-width font.	Defaults to "CB".  Only matters for troff output.

       --fixeditalic=font
	   [1.0] Italic version of the fixed-width font (something of a misnomer, since most fixed-width fonts only have an oblique  version,  not  an	italic
	   version).  Defaults to "CI".	 Only matters for troff output.

       --fixedbolditalic=font
	   [1.0]  Bold	italic (in theory, probably oblique in practice) version of the fixed-width font.  Pod::Man doesn't assume you have this, and defaults
	   to "CB".  Some systems (such as Solaris) have this font available as "CX".  Only matters for troff output.

       --guesswork=rule[,rule...]
	   [5.00] By default, pod2man applies some default formatting rules based on guesswork and regular expressions that are intended to make writing  Perl
	   documentation  easier and require less explicit markup.  These rules may not always be appropriate, particularly for documentation that isn't about
	   Perl.  This option allows turning all or some of it off.

	   The special rule "all" enables all guesswork.  This is also the default for backward compatibility reasons.	The special rule "none"	 disables  all
	   guesswork.  Otherwise, the value of this option should be a comma-separated list of one or more of the following keywords:

	   functions
	       Convert function references like foo() to bold even if they have no markup.  The function name accepts valid Perl characters for function names
	       (including ":"), and the trailing parentheses must be present and empty.

	   manref
	       Make the first part (before the parentheses) of man page references like foo(1) bold even if they have no markup.  The section must be a single
	       number optionally followed by lowercase letters.

	   quoting
	       If  no guesswork is enabled, any text enclosed in C<> is surrounded by double quotes in nroff (terminal) output unless the contents are already
	       quoted.	When this guesswork is enabled, quote marks will also be suppressed for Perl variables, function names, function calls,	 numbers,  and
	       hex constants.

	   variables
	       Convert	Perl  variable names to a fixed-width font even if they have no markup.	 This transformation will only be apparent in troff output, or
	       some other output format (unlike nroff terminal output) that supports fixed-width fonts.

	   Any unknown guesswork name is silently ignored (for potential future compatibility), so be careful about spelling.

       -h, --help
	   [1.00] Print out usage information.

       -l, --lax
	   [1.00] No longer used.  pod2man used to check its input for validity as a manual page, but this  should  now	 be  done  by  podchecker(1)  instead.
	   Accepted for backward compatibility; this option no longer does anything.

       --language=language
	   [5.00]  Add	commands  telling  groff  that the input file is in the given language.	 The value of this setting must be a language abbreviation for
	   which groff provides supplemental configuration, such as "ja" (for Japanese) or "zh" (for Chinese).

	   This adds:

	       .mso <language>.tmac
	       .hla <language>

	   to the start of the file, which configure correct line breaking for the specified language.	Without these commands, groff may not know how to  add
	   proper line breaks for Chinese and Japanese text if the man page is installed into the normal man page directory, such as /usr/share/man.

	   On  many  systems,  this  will  be  done  automatically  if	the  man  page	is  installed  into  a	language-specific  man page directory, such as
	   /usr/share/man/zh_CN.  In that case, this option is not required.

	   Unfortunately, the commands added with this option are specific to groff and will not work with other troff and nroff implementations.

       --lquote=quote
       --rquote=quote
	   [4.08] Sets the quote marks used to surround C<> text.  --lquote sets the left quote mark and --rquote sets the right quote mark.  Either may  also
	   be set to the special value "none", in which case no quote mark is added on that side of C<> text (but the font is still changed for troff output).

	   Also	 see  the  --quotes  option,  which can be used to set both quotes at once.  If both --quotes and one of the other options is set, --lquote or
	   --rquote overrides --quotes.

       -n name, --name=name
	   [4.08] Set the name of the manual page for the ".TH" macro to name.	Without this option, the manual name is set to the uppercased base name of the
	   file being converted unless the manual section is 3, in which case the path is parsed to see if it is a Perl module path.  If it is,	 a  path  like
	   ".../lib/Pod/Man.pm" is converted into a name like "Pod::Man".  This option, if given, overrides any automatic determination of the name.

	   Although  one  does not have to follow this convention, be aware that the convention for UNIX manual pages is for the title to be in all-uppercase,
	   even if the command isn't.  (Perl modules traditionally use mixed case for the manual page title, however.)

	   This option is probably not useful when converting multiple POD files at once.

	   When converting POD source from standard input, the name will be set to "STDIN" if this option is not provided.  Providing this option is  strongly
	   recommended to set a meaningful manual page name.

       --nourls
	   [2.5.0] Normally, L<> formatting codes with a URL but anchor text are formatted to show both the anchor text and the URL.  In other words:

	       L<foo|http://example.com/>

	   is formatted as:

	       foo <http://example.com/>

	   This	 flag,	if  given,  suppresses	the  URL  when	anchor text is given, so this example would be formatted as just "foo".	 This can produce less
	   cluttered output in cases where the URLs are not particularly important.

       -o, --official
	   [1.00] Set the default header to indicate that this page is part of the standard Perl release, if --center is not also given.

       -q quotes, --quotes=quotes
	   [4.00] Sets the quote marks used to surround C<> text to quotes.  If quotes is a single character, it is used as both the  left  and	 right	quote.
	   Otherwise, it is split in half, and the first half of the string is used as the left quote and the second is used as the right quote.

	   quotes may also be set to the special value "none", in which case no quote marks are added around C<> text (but the font is still changed for troff
	   output).

	   Also	 see  the  --lquote  and  --rquote options, which can be used to set the left and right quotes independently.  If both --quotes and one of the
	   other options is set, --lquote or --rquote overrides --quotes.

       -r version, --release=version
	   [1.00] Set the centered footer for the ".TH" macro to version.  By default, this is set to the version of Perl you run pod2man under.  Setting this
	   to the empty string will cause some *roff implementations to use the system default value.

	   Note that some system "an" macro sets assume that the centered footer will be a modification date and will prepend something like  "Last  modified:
	   ".  If this is the case for your target system, you may want to set --release to the last modified date and --date to the version number.

       -s string, --section=string
	   [1.00]  Set	the  section  for the ".TH" macro.  The standard section numbering convention is to use 1 for user commands, 2 for system calls, 3 for
	   functions, 4 for devices, 5 for file formats, 6 for games, 7 for miscellaneous information, and 8 for administrator commands.  There is  a  lot  of
	   variation  here, however; some systems (like Solaris) use 4 for file formats, 5 for miscellaneous information, and 7 for devices.  Still others use
	   1m instead of 8, or some mix of both.  About the only section numbers that are reliably consistent are 1, 2, and 3.

	   By default, section 1 will be used unless the file ends in ".pm", in which case section 3 will be selected.

       --stderr
	   [2.1.3] By default, pod2man dies if any errors are detected in the POD input.  If --stderr is given and no --errors flag  is	 present,  errors  are
	   sent to standard error, but pod2man does not abort.	This is equivalent to "--errors=stderr" and is supported for backward compatibility.

       -u, --utf8
	   [2.1.0]  This  option  used	to  tell  pod2man  to  produce UTF-8 output.  Since this is now the default as of version 5.00, it is ignored and does
	   nothing.

       -v, --verbose
	   [1.11] Print out the name of each output file as it is being generated.

EXIT STATUS
       As long as all documents processed result in some output, even if that output includes errata (a "POD ERRORS" section generated	with  "--errors=pod"),
       pod2man	will  exit  with  status 0.  If any of the documents being processed do not result in an output document, pod2man will exit with status 1.  If
       there are syntax errors in a POD document being processed and the error handling style is set to the default of "die", pod2man will  abort  immediately
       with exit status 255.

DIAGNOSTICS
       If pod2man fails with errors, see Pod::Man and Pod::Simple for information about what those errors might mean.

EXAMPLES
	   pod2man program > program.1
	   pod2man SomeModule.pm /usr/perl/man/man3/SomeModule.3
	   pod2man --section=7 note.pod > note.7

       If  you	would  like  to	 print out a lot of man page continuously, you probably want to set the C and D registers to set contiguous page numbering and
       even/odd paging, at least on some versions of man(7).

	   troff -man -rC1 -rD1 perl.1 perldata.1 perlsyn.1 ...

       To get index entries on "STDERR", turn on the F register, as in:

	   troff -man -rF1 perl.1

       The indexing merely outputs messages via ".tm" for each major page, section, subsection, item, and any "X<>" directives.

AUTHOR
       Russ Allbery <rra@cpan.org>, based on the original pod2man by Larry Wall and Tom Christiansen.

COPYRIGHT AND LICENSE
       Copyright 1999-2001, 2004, 2006, 2008, 2010, 2012-2019, 2022 Russ Allbery <rra@cpan.org>

       This program is free software; you may redistribute it and/or modify it under the same terms as Perl itself.

SEE ALSO
       Pod::Man, Pod::Simple, man(1), nroff(1), perlpod(1), podchecker(1), perlpodstyle(1), troff(1), man(7)

       The man page documenting the an macro set may be man(5) instead of man(7) on your system.

       The current version of this script is always available from its web site at <https://www.eyrie.org/~eagle/software/podlators/>.	It is also part of the
       Perl core distribution as of 5.6.0.

perl v5.38.2								  2025-04-08								    POD2MAN(1)
