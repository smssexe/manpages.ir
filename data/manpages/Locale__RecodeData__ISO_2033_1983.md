Locale::RecodeData::ISO_2033_1983(3pm)			      User Contributed Perl Documentation			Locale::RecodeData::ISO_2033_1983(3pm)

NAME
       Locale::RecodeData::ISO_2033_1983 - Conversion routines for ISO_2033_1983

SYNOPSIS
       This module is internal to libintl.  Do not use directly!

DESCRIPTION
       This module is generated and contains the conversion tables and routines for ISO_2033-1983.

COMMENTS
       The following comments have been extracted from the original charmap:

	version: 1.0
	repertoiremap: mnemonic,ds
	 source: ECMA registry
	alias ISO-IR-98
	alias E13B

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
	   30 |	 00000030 | DIGIT ZERO
	   31 |	 00000031 | DIGIT ONE
	   32 |	 00000032 | DIGIT TWO
	   33 |	 00000033 | DIGIT THREE
	   34 |	 00000034 | DIGIT FOUR
	   35 |	 00000035 | DIGIT FIVE
	   36 |	 00000036 | DIGIT SIX
	   37 |	 00000037 | DIGIT SEVEN
	   38 |	 00000038 | DIGIT EIGHT
	   39 |	 00000039 | DIGIT NINE
	   3A |	 00002446 | OCR BRANCH BANK IDENTIFICATION
	   3B |	 00002447 | OCR AMOUNT OF CHECK
	   3C |	 00002448 | OCR DASH
	   3D |	 00002449 | OCR CUSTOMER ACCOUNT NUMBER
	   7F |	 0000007F | DELETE (DEL)

AUTHOR
       Copyright (C) 2002-2017 Guido Flohr <http://www.guido-flohr.net/> (<mailto:guido.flohr@cantanea.com>), all rights reserved.  See the source code for
       details!code for details!

SEE ALSO
       Locale::RecodeData(3), Locale::Recode(3), perl(1)

perl v5.38.2								  2024-03-30					Locale::RecodeData::ISO_2033_1983(3pm)
