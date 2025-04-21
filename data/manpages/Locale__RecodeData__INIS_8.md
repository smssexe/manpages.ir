Locale::RecodeData::INIS_8(3pm)				      User Contributed Perl Documentation			       Locale::RecodeData::INIS_8(3pm)

NAME
       Locale::RecodeData::INIS_8 - Conversion routines for INIS_8

SYNOPSIS
       This module is internal to libintl.  Do not use directly!

DESCRIPTION
       This module is generated and contains the conversion tables and routines for INIS-8.

COMMENTS
       The following comments have been extracted from the original charmap:

	version: 1.0
	repertoiremap: mnemonic,ds
	 source: ECMA registry
	alias ISO-IR-50

       Please note that aliases listed above are not necessarily valid!

CHARACTER TABLE
       The following table is sorted in the same order as the original charmap.	 All character codes are in hexadecimal.  Please read 'ISO-10646' as
       'ISO-10646-UCS4'.

	Local | ISO-10646 | Description
       -------+-----------+-------------------------------------------------
	   00 |	 00000000 | NULL (NUL)
	   01 |	 00000001 | START OF HEADING (SOH)
	   02 |	 00000002 | START OF TEXT (STX)
	   03 |	 00000003 | END OF TEXT (ETX)
	   04 |	 00000004 | END OF TRANSMISSION (EOT)
	   05 |	 00000005 | ENQUIRY (ENQ)
	   06 |	 00000006 | ACKNOWLEDGE (ACK)
	   07 |	 00000007 | BELL (BEL)
	   08 |	 00000008 | BACKSPACE (BS)
	   09 |	 00000009 | CHARACTER TABULATION (HT)
	   0A |	 0000000A | LINE FEED (LF)
	   0B |	 0000000B | LINE TABULATION (VT)
	   0C |	 0000000C | FORM FEED (FF)
	   0D |	 0000000D | CARRIAGE RETURN (CR)
	   0E |	 0000000E | SHIFT OUT (SO)
	   0F |	 0000000F | SHIFT IN (SI)
	   10 |	 00000010 | DATALINK ESCAPE (DLE)
	   11 |	 00000011 | DEVICE CONTROL ONE (DC1)
	   12 |	 00000012 | DEVICE CONTROL TWO (DC2)
	   13 |	 00000013 | DEVICE CONTROL THREE (DC3)
	   14 |	 00000014 | DEVICE CONTROL FOUR (DC4)
	   15 |	 00000015 | NEGATIVE ACKNOWLEDGE (NAK)
	   16 |	 00000016 | SYNCHRONOUS IDLE (SYN)
	   17 |	 00000017 | END OF TRANSMISSION BLOCK (ETB)
	   18 |	 00000018 | CANCEL (CAN)
	   19 |	 00000019 | END OF MEDIUM (EM)
	   1A |	 0000001A | SUBSTITUTE (SUB)
	   1B |	 0000001B | ESCAPE (ESC)
	   1C |	 0000001C | FILE SEPARATOR (IS4)
	   1D |	 0000001D | GROUP SEPARATOR (IS3)
	   1E |	 0000001E | RECORD SEPARATOR (IS2)
	   1F |	 0000001F | UNIT SEPARATOR (IS1)
	   20 |	 00000020 | SPACE
	   3A |	 000003B1 | GREEK SMALL LETTER ALPHA
	   3B |	 000003B2 | GREEK SMALL LETTER BETA
	   3C |	 000003B3 | GREEK SMALL LETTER GAMMA
	   3D |	 000003B4 | GREEK SMALL LETTER DELTA
	   3E |	 0000039E | GREEK CAPITAL LETTER XI
	   5E |	 00002192 | RIGHTWARDS ARROW
	   5F |	 0000222B | INTEGRAL
	   60 |	 00002070 | SUPERSCRIPT ZERO
	   61 |	 000000B9 | SUPERSCRIPT ONE
	   62 |	 000000B2 | SUPERSCRIPT TWO
	   63 |	 000000B3 | SUPERSCRIPT THREE
	   64 |	 00002074 | SUPERSCRIPT FOUR
	   65 |	 00002075 | SUPERSCRIPT FIVE
	   66 |	 00002076 | SUPERSCRIPT SIX
	   67 |	 00002077 | SUPERSCRIPT SEVEN
	   68 |	 00002078 | SUPERSCRIPT EIGHT
	   69 |	 00002079 | SUPERSCRIPT NINE
	   6A |	 0000207A | SUPERSCRIPT PLUS SIGN
	   6B |	 0000207B | SUPERSCRIPT MINUS
	   6C |	 000030EB | KATAKANA LETTER RU
	   6D |	 00000394 | GREEK CAPITAL LETTER DELTA
	   6E |	 0000039B | GREEK CAPITAL LETTER LAMDA
	   6F |	 000003A9 | GREEK CAPITAL LETTER OMEGA
	   70 |	 00002080 | SUBSCRIPT ZERO
	   71 |	 00002081 | SUBSCRIPT ONE
	   72 |	 00002082 | SUBSCRIPT TWO
	   73 |	 00002083 | SUBSCRIPT THREE
	   74 |	 00002084 | SUBSCRIPT FOUR
	   75 |	 00002085 | SUBSCRIPT FIVE
	   76 |	 00002086 | SUBSCRIPT SIX
	   77 |	 00002087 | SUBSCRIPT SEVEN
	   78 |	 00002088 | SUBSCRIPT EIGHT
	   79 |	 00002089 | SUBSCRIPT NINE
	   7A |	 000003A3 | GREEK CAPITAL LETTER SIGMA
	   7B |	 000003BC | GREEK SMALL LETTER MU
	   7C |	 000003BD | GREEK SMALL LETTER NU
	   7D |	 000003C9 | GREEK SMALL LETTER OMEGA
	   7E |	 000003C0 | GREEK SMALL LETTER PI
	   7F |	 0000007F | DELETE (DEL)

AUTHOR
       Copyright (C) 2002-2017 Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

SEE ALSO
       Locale::RecodeData(3), Locale::Recode(3), perl(1)

perl v5.38.2								  2024-03-30					       Locale::RecodeData::INIS_8(3pm)
