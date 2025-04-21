TEXTDOMAIN(3)							   Library Functions Manual							 TEXTDOMAIN(3)

NAME
       textdomain - set domain for future gettext() calls

SYNOPSIS
       #include <libintl.h>

       char * textdomain (const char * domainname);

DESCRIPTION
       The textdomain function sets or retrieves the current message domain.

       A message domain is a set of translatable msgid messages. Usually, every software package has its own message domain. The domain name is used to deter‐
       mine the message catalog where a translation is looked up; it must be a non-empty string.

       The  current  message domain is used by the gettext, ngettext functions, and by the dgettext, dcgettext, dngettext and dcngettext functions when called
       with a NULL domainname argument.

       If domainname is not NULL, the current message domain is set to domainname. The string the function stores internally is a copy of the domainname argu‐
       ment.

       If domainname is NULL, the function returns the current message domain.

RETURN VALUE
       If successful, the textdomain function returns the current message domain, after possibly changing it. The resulting string is  valid  until  the  next
       textdomain call and must not be modified or freed. If a memory allocation failure occurs, it sets errno to ENOMEM and returns NULL.

ERRORS
       The following error can occur, among others:

       ENOMEM Not enough memory available.

BUGS
       The return type ought to be const char *, but is char * to avoid warnings in C code predating ANSI C.

SEE ALSO
       gettext(3), ngettext(3), bindtextdomain(3), bind_textdomain_codeset(3)

GNU gettext 0.20.1.124-32cf						   May 2001								 TEXTDOMAIN(3)
