OPENSSL-NAMEDISPLAY-OPTIONS(1SSL)					    OpenSSL					     OPENSSL-NAMEDISPLAY-OPTIONS(1SSL)

NAME
       openssl-namedisplay-options - Distinguished name display options

SYNOPSIS
       openssl command [ options ... ] [ parameters ... ]

DESCRIPTION
       OpenSSL provides fine-grain control over how the subject and issuer DN's are displayed.	This is specified by using the -nameopt option, which takes a
       comma-separated list of options from the following set.	An option may be preceded by a minus sign, "-", to turn it off.	 The default value is
       "oneline".  The first four are the most commonly used.

OPTIONS
   Name Format Option Arguments
       The DN output format can be fine tuned with the following flags.

       compat
	   Display the name using an old format from previous OpenSSL versions.

       RFC2253
	   Display  the name using the format defined in RFC 2253.  It is equivalent to esc_2253, esc_ctrl, esc_msb, utf8, dump_nostr, dump_unknown, dump_der,
	   sep_comma_plus, dn_rev and sname.

       oneline
	   Display the name in one line, using a format that is more readable RFC 2253.	 It is equivalent to esc_2253, esc_ctrl,  esc_msb,  utf8,  dump_nostr,
	   dump_der, use_quote, sep_comma_plus_space, space_eq and sname options.

       multiline
	   Display the name using multiple lines.  It is equivalent to esc_ctrl, esc_msb, sep_multiline, space_eq, lname and align.

       esc_2253
	   Escape the "special" characters in a field, as required by RFC 2253.	 That is, any of the characters ",+"<>;", "#" at the beginning of a string and
	   leading or trailing spaces.

       esc_2254
	   Escape the "special" characters in a field as required by RFC 2254 in a field.  That is, the NUL character and of "()*".

       esc_ctrl
	   Escape non-printable ASCII characters, codes less than 0x20 (space) or greater than 0x7F (DELETE). They are displayed using RFC 2253 "\XX" notation
	   where XX are the two hex digits representing the character value.

       esc_msb
	   Escape any characters with the most significant bit set, that is with values larger than 127, as described in esc_ctrl.

       use_quote
	   Escapes  some  characters  by  surrounding  the  entire  string  with quotation marks, """.	Without this option, individual special characters are
	   preceded with a backslash character, "\".

       utf8
	   Convert all strings to UTF-8 format first as required by RFC 2253.  If the output device is UTF-8 compatible,  then	using  this  option  (and  not
	   setting  esc_msb) may give the correct display of multibyte characters.  If this option is not set, then multibyte characters larger than 0xFF will
	   be output as "\UXXXX" for 16 bits or "\WXXXXXXXX" for 32 bits.  In addition, any UTF8Strings will be converted to their character form first.

       ignore_type
	   This option does not attempt to interpret multibyte characters in any way. That is, the content octets  are	merely	dumped	as  though  one	 octet
	   represents each character. This is useful for diagnostic purposes but will result in rather odd looking output.

       show_type
	   Display the type of the ASN1 character string before the value, such as "BMPSTRING: Hello World".

       dump_der
	   Any	fields	that  would  be	 output	 in  hex  format  are  displayed using the DER encoding of the field.  If not set, just the content octets are
	   displayed.  Either way, the #XXXX... format of RFC 2253 is used.

       dump_nostr
	   Dump non-character strings, such as ASN.1 OCTET STRING.  If this option is not set, then non character string types will  be	 displayed  as	though
	   each content octet represents a single character.

       dump_all
	   Dump all fields. When this used with dump_der, this allows the DER encoding of the structure to be unambiguously determined.

       dump_unknown
	   Dump any field whose OID is not recognised by OpenSSL.

       sep_comma_plus, sep_comma_plus_space, sep_semi_plus_space, sep_multiline
	   Specify  the	 field separators. The first word is used between the Relative Distinguished Names (RDNs) and the second is between multiple Attribute
	   Value Assertions (AVAs). Multiple AVAs are very rare and their use is discouraged.  The options ending in "space" additionally place a space	 after
	   the separator to make it more readable.  The sep_multiline starts each field on its own line, and uses "plus space" for the AVA separator.  It also
	   indents the fields by four characters.  The default value is sep_comma_plus_space.

       dn_rev
	   Reverse  the	 fields of the DN as required by RFC 2253.  This also reverses the order of multiple AVAs in a field, but this is permissible as there
	   is no ordering on values.

       nofname, sname, lname, oid
	   Specify how the field name is displayed.  nofname does not display the field at all.	 sname uses the "short	name"  form  (CN  for  commonName  for
	   example).  lname uses the long form.	 oid represents the OID in numerical form and is useful for diagnostic purpose.

       align
	   Align field values for a more readable output. Only usable with sep_multiline.

       space_eq
	   Places spaces round the equal sign, "=", character which follows the field name.

COPYRIGHT
       Copyright 2000-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05					     OPENSSL-NAMEDISPLAY-OPTIONS(1SSL)
