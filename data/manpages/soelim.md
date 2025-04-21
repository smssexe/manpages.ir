soelim(1)							    General Commands Manual							     soelim(1)

Name
       soelim - recursively interpolate source requests in roff or other text files

Synopsis
       soelim [-Crt] [-I dir] [input-file ...]

       soelim --help

       soelim -v
       soelim --version

Description
       GNU  soelim  is	a  preprocessor	 for  the groff(7) document formatting system.	soelim works as a filter to eliminate source requests in roff(7) input
       files; that is, it replaces lines of the form “.so included-file” within each text input-file with the contents of included-file, recursively.  By  de‐
       fault, it writes lf requests as well to record the name and line number of each input-file and included-file, so that any diagnostics produced by later
       processing  can	be  accurately traced to the original input.  Options allow this information to be suppressed (-r) or supplied in TeX comments instead
       (-t).  In the absence of input-file arguments, soelim reads the standard input stream.  Output is written to the standard output stream.

       If the name of a macro-file contains a backslash, use \\ or \e to embed it.  To embed a space, write “\ ” (backslash followed by a space).   Any	 other
       escape sequence in macro-file, including “\[rs]”, prevents soelim from replacing the source request.

       The  dot	 must  be at the beginning of a line and must be followed by “so” without intervening spaces or tabs for soelim to handle it.  This convention
       allows source requests to be “protected” from processing by soelim, for instance as part of macro definitions or “if” requests.

       There must also be at least one space between “so” and its macro-file argument.	The -C option overrides this requirement.

       The foregoing is the limit of soelim's understanding of the roff language; it does not, for example, replace the input line
	      .if 1 .so otherfile
       with the contents of otherfile.	With its -r option, therefore, soelim can be used to process text files in general, to flatten a tree of  input	 docu‐
       ments.

       soelim was designed to handle situations where the target of a roff source request requires a preprocessor such as eqn(1), pic(1), refer(1), or tbl(1).
       The usual processing sequence of groff(1) is as follows.

		 input	      sourced
		 file	       file
		   ⎪		 ⎪
		   ↓		 ↓
	       preprocessor ⎯→ troff ⎯→ postprocessor
					     ⎪
					     ↓
					  output
					   file

       That is, files sourced with “so” are normally read only by the formatter, troff.	 soelim is not required for troff to source files.

       If  a  file to be sourced should also be preprocessed, it must already be read before the input file passes through the preprocessor.  soelim, normally
       invoked via groff's -s option, handles this.

		 input
		 file
		   ⎪
		   ↓
		 soelim ⎯→ preprocessor ⎯→ troff ⎯→ postprocessor
		   ↑					 ⎪
		   ⎪					 ↓
		sourced				      output
		 file				       file

Options
       --help displays a usage message, while -v and --version show version information; all exit afterward.

       -C     Recognize an input line starting with .so even if a character other than a space or newline follows.

       -I dir Search the directory dir path for input- and included-files.  -I may be specified more than once; each dir is searched in the given  order.   To
	      search the current working directory before others, add “-I .” at the desired place; it is otherwise searched last.

       -r     Write files “raw”; do not add lf requests.

       -t     Emit TeX comment lines starting with “%” indicating the current file and line number, rather than lf requests for the same purpose.

       If both -r and -t are given, the last one specified controls.

See also
       groff(1)

groff 1.23.0								 31 March 2024								     soelim(1)
