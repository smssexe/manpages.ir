SYSTEMD.SYNTAX(7)							systemd.syntax							     SYSTEMD.SYNTAX(7)

NAME
       systemd.syntax - General syntax of systemd configuration files

INTRODUCTION
       This page describes the basic principles of configuration files used by systemd(1) and related programs for:

       •   systemd unit files, see systemd.unit(5), systemd.service(5), systemd.socket(5), systemd.device(5), systemd.mount(5), systemd.automount(5),
	   systemd.swap(5), systemd.target(5), systemd.path(5), systemd.timer(5), systemd.slice(5), systemd.scope(5)

       •   link files, see systemd.link(5)

       •   netdev and network files, see systemd.netdev(5), systemd.network(5)

       •   daemon config files, see systemd-system.conf(5), systemd-user.conf(5), logind.conf(5), journald.conf(5), journal-remote.conf(5), journal-
	   upload.conf(5), systemd-sleep.conf(5), timesyncd.conf(5)

       •   nspawn files, see systemd.nspawn(5)

       The syntax is inspired by XDG Desktop Entry Specification[1] .desktop files, which are in turn inspired by Microsoft Windows .ini files.

       Each file is a plain text file divided into sections, with configuration entries in the style key=value. Whitespace immediately before or after the "="
       is ignored. Empty lines and lines starting with "#" or ";" are ignored, which may be used for commenting.

       Lines ending in a backslash are concatenated with the following line while reading and the backslash is replaced by a space character. This may be used
       to wrap long lines. The limit on line length is very large (currently 1 MB), but it is recommended to avoid such long lines and use multiple
       directives, variable substitution, or other mechanism as appropriate for the given file type. When a comment line or lines follow a line ending with a
       backslash, the comment block is ignored, so the continued line is concatenated with whatever follows the comment block.

       Example 1.

	   [Section A]
	   KeyOne=value 1
	   KeyTwo=value 2

	   # a comment

	   [Section B]
	   Setting="something" "some thing" "..."
	   KeyTwo=value 2 \
		  value 2 continued

	   [Section C]
	   KeyThree=value 3\
	   # this line is ignored
	   ; this line is ignored too
		  value 3 continued

       Boolean arguments used in configuration files can be written in various formats. For positive settings the strings 1, yes, true and on are equivalent.
       For negative settings, the strings 0, no, false and off are equivalent.

       Time span values encoded in configuration files can be written in various formats. A stand-alone number specifies a time in seconds. If suffixed with a
       time unit, the unit is honored. A concatenation of multiple values with units is supported, in which case the values are added up. Example: "50" refers
       to 50 seconds; "2min 200ms" refers to 2 minutes and 200 milliseconds, i.e. 120200 ms. The following time units are understood: "s", "min", "h", "d",
       "w", "ms", "us". For details see systemd.time(7).

       Various settings are allowed to be specified more than once, in which case the interpretation depends on the setting. Often, multiple settings form a
       list, and setting to an empty value "resets", which means that previous assignments are ignored. When this is allowed, it is mentioned in the
       description of the setting. Note that using multiple assignments to the same value makes the file incompatible with parsers for the XDG .desktop file
       format.

QUOTING
       For settings where quoting is allowed, the following general rules apply: double quotes ("...") and single quotes ('...') may be used to wrap a whole
       item (the opening quote may appear only at the beginning or after whitespace that is not quoted, and the closing quote must be followed by whitespace
       or the end of line), in which case everything until the next matching quote becomes part of the same item. Quotes themselves are removed. C-style
       escapes are supported. The table below contains the list of known escape patterns. Only escape patterns which match the syntax in the table are
       allowed; other patterns may be added in the future and unknown patterns will result in a warning. In particular, any backslashes should be doubled.
       Finally, a trailing backslash ("\") may be used to merge lines, as described above. UTF-8 is accepted, and hence typical unicode characters do not need
       to be escaped.

       Table 1. Supported escapes
       ┌──────────────┬─────────────────────────────────────────────────────┐
       │ Literal      │ Actual value					    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\a"	      │ bell						    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\b"	      │ backspace					    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\f"	      │ form feed					    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\n"	      │ newline						    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\r"	      │ carriage return					    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\t"	      │ tab						    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\v"	      │ vertical tab					    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\\"	      │ backslash					    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\""	      │ double quotation mark				    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\'"	      │ single quotation mark				    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\s"	      │ space						    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\xxx"	      │ character number xx in hexadecimal encoding	    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\nnn"	      │ character number nnn in octal encoding		    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\unnnn"     │ unicode code point nnnn in hexadecimal encoding	    │
       ├──────────────┼─────────────────────────────────────────────────────┤
       │ "\Unnnnnnnn" │ unicode code point nnnnnnnn in hexadecimal encoding │
       └──────────────┴─────────────────────────────────────────────────────┘

SEE ALSO
       systemd.time(7)

NOTES
	1. XDG Desktop Entry Specification
	   https://standards.freedesktop.org/desktop-entry-spec/latest/

systemd 255																     SYSTEMD.SYNTAX(7)
