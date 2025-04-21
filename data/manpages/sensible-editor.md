SENSIBLE-EDITOR(1)						    General Commands Manual						    SENSIBLE-EDITOR(1)

NAME
       sensible-editor - launch sensibly chosen text editor

SYNOPSIS
       sensible-editor [OPTIONS...]

DESCRIPTION
       sensible-editor makes sensible decisions on which editor to call.  Programs in Debian can invoke this script to get a good default editor.

       sensible-editor	looks for an appropriate choice of editor in a series of places, and uses the first candidate that works.  It starts by checking envi‐
       ronment variables, followed by a variable defined via select-editor, then tries the default editor command defined by the alternatives system,  with  a
       series of hard-coded command names as fallbacks.

       Variables will be skipped if unset or null, but may include extra whitespace-separated parameters such as a --verbose flag.  Once sensible-editor has a
       candidate  commandline,	it  will  try  to run it (passing on the arguments it was given as the files to be edited).  If this fails because the command
       couldn't be executed (exit code 126) or was not found (exit code 127), it tries the next candidate.

       The specific candidates sensible-editor tries, in order, are:

       • $VISUAL – see environ (7)

       • $EDITOR – see environ (7)

       • $SENSIBLE_EDITOR

       • $SELECTED_EDITOR – see select-editor (1)

       • editor – see editor (1), update-alternatives (1)

       • nano

       • nano-tiny

       • vi

       If all of these fail, sensible-editor errors out.  This system is designed to make it easy for individual users to set a personal and/or temporary  de‐
       fault, overriding the system-wide defaults.

BUGS
       This  command  takes precautions against launching itself in an infinite loop if a user sets EDITOR=sensible-editor but indirect loops are still possi‐
       ble.

SEE ALSO
       sensible-browser(1), sensible-pager(1), select-editor(1), environ(7), editor(1), update-alternatives(1)

CONFORMS TO
       The behavior of sensible-utils under a Debian system is documented in section 11.4 of Debian-Policy, available  under  /usr/share/doc/debian-policy  if
       debian-policy is installed, or online at https://www.debian.org/doc/debian-policy/

Debian									  28 Aug 2022							    SENSIBLE-EDITOR(1)
