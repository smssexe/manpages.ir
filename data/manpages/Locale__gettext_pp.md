Locale::gettext_pp(3pm)					      User Contributed Perl Documentation				       Locale::gettext_pp(3pm)

NAME
       Locale::gettext_pp - Pure Perl Implementation of Uniforum Message Translation

SYNOPSIS
	use Locale::gettext_pp qw(:locale_h :libintl_h);

	gettext $msgid;
	dgettext $domainname, $msgid;
	dcgettext $domainname, $msgid, LC_MESSAGES;
	ngettext $msgid, $msgid_plural, $count;
	dngettext $domainname, $msgid, $msgid_plural, $count;
	dcngettext $domainname, $msgid, $msgid_plural, $count, LC_MESSAGES;
	pgettext $msgctxt, $msgid;
	dpgettext $domainname, $msgctxt, $msgid;
	dcpgettext $domainname, $msgctxt, $msgid, LC_MESSAGES;
	npgettext $msgctxt, $msgid, $msgid_plural, $count;
	dnpgettext $domainname, $msgctxt, $msgid, $msgid_plural, $count;
	dcnpgettext $domainname, $msgctxt, $msgid, $msgid_plural, $count, LC_MESSAGES;
	textdomain $domainname;
	bindtextdomain $domainname, $directory;
	bind_textdomain_codeset $domainname, $encoding;
	my $category = LC_CTYPE;
	my $category = LC_NUMERIC;
	my $category = LC_TIME;
	my $category = LC_COLLATE;
	my $category = LC_MONETARY;
	my $category = LC_MESSAGES;
	my $category = LC_ALL;

DESCRIPTION
       The module Locale::gettext_pp is the low-level interface to message translation according to the Uniforum approach that is for example used in GNU
       gettext and Sun's Solaris.

       Normally you should not use this module directly, but the high level interface Locale::TextDomain(3) that provides a much simpler interface.    This
       description is therefore deliberately kept brief.    Please refer to the GNU gettext documentation available at <http://www.gnu.org/manual/gettext/>
       for in-depth and background information on the topic.

FUNCTIONS
       The module exports by default nothing.	 Every function has to be imported explicitly or via an export tag ("EXPORT TAGS").

       gettext MSGID
	   See "FUNCTIONS" in Locale::Messages.

       dgettext TEXTDOMAIN, MSGID
	   See "FUNCTIONS" in Locale::Messages.

       dcgettext TEXTDOMAIN, MSGID, CATEGORY
	   See "FUNCTIONS" in Locale::Messages.

       ngettext MSGID, MSGID_PLURAL, COUNT
	   See "FUNCTIONS" in Locale::Messages.

       dngettext TEXTDOMAIN, MSGID, MSGID_PLURAL, COUNT
	   See "FUNCTIONS" in Locale::Messages.

       dcngettext TEXTDOMAIN, MSGID, MSGID_PLURAL, COUNT, CATEGORY
	   See "FUNCTIONS" in Locale::Messages.

       pgettext MSGCTXT, MSGID
	   See "FUNCTIONS" in Locale::Messages.

       dpgettext TEXTDOMAIN, MSGCTXT, MSGID
	   See "FUNCTIONS" in Locale::Messages.

       dcpgettext TEXTDOMAIN, MSGCTXT, MSGID, CATEGORY
	   See "FUNCTIONS" in Locale::Messages.

       npgettext MSGCTXT, MSGID, MSGID_PLURAL, COUNT
	   See "FUNCTIONS" in Locale::Messages.

       dnpgettext TEXTDOMAIN, MSGCTXT, MSGID, MSGID_PLURAL, COUNT
	   See "FUNCTIONS" in Locale::Messages.

       dcnpgettext TEXTDOMAIN, MSGCTXT, MSGID, MSGID_PLURAL, COUNT, CATEGORY
	   See "FUNCTIONS" in Locale::Messages.

       textdomain TEXTDOMAIN
	   See "FUNCTIONS" in Locale::Messages.

       bindtextdomain TEXTDOMAIN, DIRECTORY
	   See "FUNCTIONS" in Locale::Messages.

       bind_textdomain_codeset TEXTDOMAIN, ENCODING
       nl_putenv ENVSPEC
	   See "FUNCTIONS" in Locale::Messages.

       setlocale
	   See "FUNCTIONS" in Locale::Messages.

CONSTANTS
       You can (maybe) get the same constants from POSIX(3); see there for a detailed description

       LC_CTYPE
       LC_NUMERIC
       LC_TIME
       LC_COLLATE
       LC_MONETARY
       LC_MESSAGES
       LC_ALL
	   See "CONSTANTS" in Locale::Messages for more information.

EXPORT TAGS
       This module does not export anything unless explicitly requested.  You can import groups of functions via two tags:

       use Locale::gettext_pp qw(':locale_h')
	   Imports the functions that are normally defined in the C include file locale.h:

	   gettext()
	   dgettext()
	   dcgettext()
	   ngettext()
	   dngettext()
	   dcngettext()
	   pgettext()
		   Introduced with libintl-perl 1.17.

	   dpgettext()
		   Introduced with libintl-perl 1.17.

	   dcpgettext()
		   Introduced with libintl-perl 1.17.

	   npgettext()
		   Introduced with libintl-perl 1.17.

	   dnpgettext()
		   Introduced with libintl-perl 1.17.

	   dcnpgettext()
		   Introduced with libintl-perl 1.17.

	   textdomain()
	   bindtextdomain()
	   bind_textdomain_codeset()
       use Locale::gettext_pp (':libintl_h')
	   Imports the locale category constants:

	   LC_CTYPE
	   LC_NUMERIC
	   LC_TIME
	   LC_COLLATE
	   LC_MONETARY
	   LC_MESSAGES
	   LC_ALL

AUTHOR
       Copyright  (C)  2002-2017  Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

SEE ALSO
       Locale::TextDomain(3pm), Locale::Messages(3pm), Encode(3pm), perllocale(3pm), POSIX(3pm), perl(1), gettext(1), gettext(3)

perl v5.38.2								  2024-03-30						       Locale::gettext_pp(3pm)
