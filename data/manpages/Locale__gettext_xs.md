Locale::gettext_xs(3pm)					      User Contributed Perl Documentation				       Locale::gettext_xs(3pm)

NAME
       Locale::gettext_xs - XS Implementation of Uniforum Message Translation

SYNOPSIS
	use gettext_xs qw(:locale_h :libintl_h);

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
       The module Locale::gettext_xs is the low-level interface to message translation according to the Uniforum approach that is for example used in GNU
       gettext and Sun's Solaris.

       The module does not necessarily work on your system.  It depends on the presence of shared libraries that are not always available.  The higher-level
       modules Locale::TextDomain::(3), resp.  Locale::Messages(3) will fall back to a pure Perl version if boostrapping Locale::gettext_xs fails.

       The interface of Locale::gettext_xs is mostly identical to the pure Perl version as described in Locale::gettext_pp(3), see there for details.
       Differences are outlined below.

       Locale::gettext_xs is downwards compatible to Locale::gettext(3) by Phillip Vandry <vandry@Mlink.NET>.  You can use it as replacement for
       Locale::gettext(3).

       Please note that directory names passed to the function bindtextdomain() are automatically converted from Perl semantics (slash as directory separator)
       to local semantics (for example the backslash for MS-DOS).

AUTHOR
       Copyright (C) 2002-2017 Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

       The module is based on the work of Phillip Vandry <vandry@Mlink.NET> in Locale::gettext(3).

SEE ALSO
       Locale::TextDomain(3pm), Locale::gettext_pp(3pm), Locale::gettext(3pm), Locale::Messages(3pm), File::Spec(3), perl(1)

perl v5.38.2								  2024-03-30						       Locale::gettext_xs(3pm)
