Locale::RecodeData::_Encode(3pm)			      User Contributed Perl Documentation			      Locale::RecodeData::_Encode(3pm)

NAME
       Locale::RecodeData::_Encode - Internal wrapper around Encode

SYNOPSIS
       use Locale::RecodeData::_Encode;

       This module is internal to libintl.  Do not use directly!

DESCRIPTION
       This module converts text with the help of Encode(3).  It is tried first for conversions if libintl-perl detects the presence of Encode.

AUTHOR
       Copyright (C) 2002-2017 Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

SEE ALSO
       Locale::Recode(3), Encode(3), perl(1)

perl v5.38.2								  2024-03-30					      Locale::RecodeData::_Encode(3pm)
