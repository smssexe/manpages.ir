WrapI18N(3pm)						      User Contributed Perl Documentation						 WrapI18N(3pm)

NAME
       Text::WrapI18N - Line wrapping module with support for multibyte, fullwidth, and combining characters and languages without whitespaces between words

SYNOPSIS
	 use Text::WrapI18N qw(wrap $columns);
	 wrap(firstheader, nextheader, texts);

DESCRIPTION
       This module intends to be a better Text::Wrap module.  This module is needed to support multibyte character encodings such as UTF-8, EUC-JP, EUC-KR,
       GB2312, and Big5.  This module also supports characters with irregular widths, such as combining characters (which occupy zero columns on terminal,
       like diacritical marks in UTF-8) and fullwidth characters (which occupy two columns on terminal, like most of east Asian characters).  Also, minimal
       handling of languages which doesn't use whitespaces between words (like Chinese and Japanese) is supported.

       Like Text::Wrap, hyphenation and "kinsoku" processing are not supported, to keep simplicity.

       wrap(firstheader, nextheader, texts) is the main subroutine of Text::WrapI18N module to execute the line wrapping.  Input parameters and output data
       emulate Text::Wrap.  The texts have to be written in locale encoding.

SEE ALSO
       locale(5), utf-8(7), charsets(7)

AUTHOR
       Tomohiro KUBOTA, <kubota@debian.org>

COPYRIGHT AND LICENSE
       Copyright 2003 by Tomohiro KUBOTA

       This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

perl v5.36.0								  2022-08-29								 WrapI18N(3pm)
