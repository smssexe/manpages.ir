Locale::Recode::_Aliases(3pm)				      User Contributed Perl Documentation				 Locale::Recode::_Aliases(3pm)

NAME
       Locale::Recode::_Aliases - Internal Charset Alias Database for libintl-perl

SYNOPSIS
       use Locale::Recode::_Aliases

       die "This module is internal to libintl.	 Do not use it directly!\n";

DESCRIPTION
       Contains a list of codeset aliases that are known internally to libintl.

CONSTANTS
       ALIASES
	   The	constant  Locale::Recode::_Aliases::ALIASES  contains  a  hash	reference  the	keys  of which are internally known charset alias names all in
	   uppercase.  The corresponding value is the canonical name of the charset.

BUGS
       The format of the lookup table will most probably change, do not rely on the current format!

AUTHOR
       Copyright (C) 2002-2017 Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the  source  code  for
       details!code for details!

SEE ALSO
       Locale::Recode(3), perl(1)

perl v5.38.2								  2024-03-30						 Locale::Recode::_Aliases(3pm)
