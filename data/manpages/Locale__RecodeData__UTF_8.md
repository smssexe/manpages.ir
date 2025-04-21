Locale::RecodeData::UTF_8(3pm)				      User Contributed Perl Documentation				Locale::RecodeData::UTF_8(3pm)

NAME
       Locale::RecodeData::UTF_8 - Conversion routines for UTF-8

SYNOPSIS
       This module is internal to libintl.  Do not use directly!

DESCRIPTION
       This modules contains the conversion tables for UTF-8.  It is capable of converting from UTF-8 to the internal format of libintl-perl and vice versa.
       It is only suitable for Perl versions <= 5.8.0.	However, you do not have to bother about version checking, Locale::Recode(3) will do that for you.

CHARACTER TABLE
       See http://www.unicode.org/.

AUTHOR
       Copyright (C) 2002-2017 Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

SEE ALSO
       Locale::RecodeData(3), Locale::Recode(3), perl(1)

perl v5.38.2								  2024-03-30						Locale::RecodeData::UTF_8(3pm)
