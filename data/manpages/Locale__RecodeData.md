Locale::RecodeData(3pm)					      User Contributed Perl Documentation				       Locale::RecodeData(3pm)

NAME
       Locale::RecodeData - Abstract Base Class for Charset Converters

SYNOPSIS
	   # For compatibility with Perl 5.005 and earlier, you must
	   # *use* the module before inheriting from it!
	   use qw (Locale::RecodeData);
	   use base qw (Locale::RecodeData);

DESCRIPTION
       The module Locale::RecodeData serves as an abstract base class to all converters used by Locale::Recode(3).

       Adding new conversion modules is currently not straightforward, and you will have to edit the sources of some modules for that purpose.

       First, you have to add your new converter class to the list found in Locale::_Conversions(3), so that Locale::Recode(3) knows about its presence.  If
       there are valid aliases for the codeset of your converter, you will also have to edit Locale::_Aliases(3).

       Finally, you have to implement the (protected) conversion routine _recode().  See below ("INTERFACE") for details.

CONSTRUCTOR
       new (from => FROM_CODESET, to => TO_CODESET)
	   The constructor takes two (named) arguments:

	   from	   The canonical name of the source codeset.  Aliases have already been resolved and the name is converted to uppercase.

	   to	   The canonical name of the destination codeset.  Aliases have already been resolved and the name is converted to uppercase.

	   You	normally  don't have to implement the constructor.  The default constructor implemented here will store the source and destination codesets in
	   the protected members "_from" and "_to".

METHODS
       The class implements one method:

       _getError
	   Returns the (protected) member "_error".

INTERFACE
       New conversion classes must provide the following interface:

       new (from => FROM_CODESET, to => TO_CODESET)
	   The constructor takes two (named) arguments:

	   from	   The canonical name of the source codeset.  Aliases have already been resolved and the name is converted to uppercase.

	   to	   The canonical name of the destination codeset.  Aliases have already been resolved and the name is converted to uppercase.

       _getError
	   Should return the last error (as a string) or false if there was no error.

	   This method is implemented in the base class already.

       _recode STRINGREF
	   Should convert the argument "STRINGREF" in-place.  In case of failure, return false, and make provisions that the  method  _getError()  returns  an
	   informative error message.

AUTHOR
       Copyright  (C)  2002-2017  Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

SEE ALSO
       Locale::Recode::_Aliases(3pm), Locale::Recode::_Conversions(3pm), Locale::Recode(3pm), perl(1)

perl v5.38.2								  2024-03-30						       Locale::RecodeData(3pm)
