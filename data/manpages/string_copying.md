string_copying(7)					       Miscellaneous Information Manual						     string_copying(7)

NAME
       stpcpy, strcpy, strcat, stpecpy, strtcpy, strlcpy, strlcat, stpncpy, strncpy, strncat - copying strings and character sequences

SYNOPSIS
   Strings
       // Chain-copy a string.
       char *stpcpy(char *restrict dst, const char *restrict src);

       // Copy/catenate a string.
       char *strcpy(char *restrict dst, const char *restrict src);
       char *strcat(char *restrict dst, const char *restrict src);

       // Chain-copy a string with truncation.
       char *stpecpy(char *dst, char end[0], const char *restrict src);

       // Copy/catenate a string with truncation.
       ssize_t strtcpy(char dst[restrict .dsize], const char *restrict src,
		      size_t dsize);
       size_t strlcpy(char dst[restrict .dsize], const char *restrict src,
		      size_t dsize);
       size_t strlcat(char dst[restrict .dsize], const char *restrict src,
		      size_t dsize);

   Null-padded character sequences
       // Fill a fixed-size buffer with characters from a string
       // and pad with null bytes.
       char *strncpy(char dst[restrict .dsize], const char *restrict src,
		      size_t dsize);
       char *stpncpy(char dst[restrict .dsize], const char *restrict src,
		      size_t dsize);

       // Chain-copy a null-padded character sequence into a character sequence.
       mempcpy(dst, src, strnlen(src, NITEMS(src)));

       // Chain-copy a null-padded character sequence into a string.
       stpcpy(mempcpy(dst, src, strnlen(src, NITEMS(src))), "");

       // Catenate a null-padded character sequence into a string.
       char *strncat(char *restrict dst, const char src[restrict .ssize],
		      size_t ssize);

   Known-length character sequences
       // Chain-copy a known-length character sequence.
       void *mempcpy(void dst[restrict .len], const void src[restrict .len],
		      size_t len);

       // Chain-copy a known-length character sequence into a string.
       stpcpy(mempcpy(dst, src, len), "");

DESCRIPTION
   Terms (and abbreviations)
       string (str)
	      is a sequence of zero or more non-null characters followed by a null character.

       character sequence
	      is  a  sequence of zero or more non-null characters.  A program should never use a character sequence where a string is required.	 However, with
	      appropriate care, a string can be used in the place of a character sequence.

	      null-padded character sequence
		     Character sequences can be contained in fixed-size buffers, which contain padding null bytes after the character sequence,	 to  fill  the
		     rest  of  the  buffer without affecting the character sequence; however, those padding null bytes are not part of the character sequence.
		     Don't confuse null-padded with null-terminated: null-padded means 0 or more padding null bytes, while  null-terminated  means  exactly  1
		     terminating null character.

	      known-length character sequence
		     Character sequence delimited by its length.  It may be a slice of a larger character sequence, or even of a string.

       length (len)
	      is the number of non-null characters in a string or character sequence.  It is the return value of strlen(str) and of strnlen(buf, size).

       size   refers to the entire buffer where the string or character sequence is contained.

       end    is  the name of a pointer to one past the last element of a buffer.  It is equivalent to &str[size].  It is used as a sentinel value, to be able
	      to truncate strings or character sequences instead of overrunning the containing buffer.

       copy   This term is used when the writing starts at the first element pointed to by dst.

       catenate
	      This term is used when a function first finds the terminating null character in dst, and then starts writing at that position.

       chain  This term is used when it's the programmer who provides a pointer to the terminating null character in the string dst (or	 one  after  the  last
	      character in a character sequence), and the function starts writing at that location.  The function returns a pointer to the new location of the
	      terminating  null character (or one after the last character in a character sequence) after the call, so that the programmer can use it to chain
	      such calls.

   Copy, catenate, and chain-copy
       Originally, there was a distinction between functions that copy and those that catenate.	 However, newer functions that copy  while  allowing  chaining
       cover  both  use	 cases with a single API.  They are also algorithmically faster, since they don't need to search for the terminating null character of
       the existing string.  However, functions that catenate have a much simpler use, so if performance is not important, it can make sense to use  them  for
       improving readability.

       The pointer returned by functions that allow chaining is a byproduct of the copy operation, so it has no performance costs.  Functions that return such
       a pointer, and thus can be chained, have names of the form *stp*(), since it's common to name the pointer just p.

       Chain-copying  functions	 that truncate should accept a pointer to the end of the destination buffer, and have names of the form *stpe*().  This allows
       not having to recalculate the remaining size after each call.

   Truncate or not?
       The first thing to note is that programmers should be careful with buffers, so they always have the correct size, and truncation is not necessary.

       In most cases, truncation is not desired, and it is simpler to just do the copy.	 Simpler code is safer code.  Programming against programming mistakes
       by adding more code just adds more points where mistakes can be made.

       Nowadays, compilers can detect most programmer errors with features like compiler warnings, static analyzers, and _FORTIFY_SOURCE (see ftm(7)).	 Keep‐
       ing the code simple helps these overflow-detection features be more precise.

       When validating user input, code should normally not truncate, but instead fail and prevent the copy at all.

       In some cases, however, it makes sense to truncate.

       Functions that truncate:

       •  stpecpy()

       •  strtcpy()

       •  strlcpy(3bsd) and strlcat(3bsd) are similar, but have important performance problems; see BUGS.

       •  stpncpy(3) and strncpy(3) also truncate, but they don't write strings, but rather null-padded character sequences.

   Null-padded character sequences
       For  historic reasons, some standard APIs and file formats, such as utmpx(5) and tar(1), use null-padded character sequences in fixed-size buffers.  To
       interface with them, specialized functions need to be used.

       To copy bytes from strings into these buffers, use strncpy(3) or stpncpy(3).

       To read a null-padded character sequence, use strnlen(src, NITEMS(src)), and then you can treat it as a known-length character sequence; or  use	 strn‐
       cat(3) directly.

   Known-length character sequences
       The  simplest  character	 sequence copying function is mempcpy(3).  It requires always knowing the length of your character sequences, for which struc‐
       tures can be used.  It makes the code much faster, since you always know the length of your character sequences, and can	 do  the  minimal  copies  and
       length measurements.  mempcpy(3) copies character sequences, so you need to explicitly set the terminating null character if you need a string.

       In programs that make considerable use of strings or character sequences, and need the best performance, using overlapping character sequences can make
       a big difference.  It allows holding subsequences of a larger character sequence, while not duplicating memory nor using time to do a copy.

       However, this is delicate, since it requires using character sequences.	C library APIs use strings, so programs that use character sequences will have
       to take care of differentiating strings from character sequences.

       To copy a known-length character sequence, use mempcpy(3).

       To copy a known-length character sequence into a string, use stpcpy(mempcpy(dst, src, len), "").

       A  string is also accepted as input, because mempcpy(3) asks for the length, and a string is composed of a character sequence of the same length plus a
       terminating null character.

   String vs character sequence
       Some functions only operate on strings.	Those require that the input src is a string, and guarantee an output string (even  when  truncation  occurs).
       Functions that catenate also require that dst holds a string before the call.  List of functions:

       •  stpcpy(3)
       •  strcpy(3), strcat(3)
       •  stpecpy()
       •  strtcpy()
       •  strlcpy(3bsd), strlcat(3bsd)

       Other  functions	 require an input string, but create a character sequence as output.  These functions have confusing names, and have a long history of
       misuse.	List of functions:

       •  stpncpy(3)
       •  strncpy(3)

       Other functions operate on an input character sequence, and create an output string.  Functions that catenate also require that dst holds a string  be‐
       fore the call.  strncat(3) has an even more misleading name than the functions above.  List of functions:

       •  strncat(3)

       Other functions operate on an input character sequence to create an output character sequence.  List of functions:

       •  mempcpy(3)

   Functions
       stpcpy(3)
	      Copy  the	 input	string	into  a destination string.  The programmer is responsible for allocating a buffer large enough.  It returns a pointer
	      suitable for chaining.

       strcpy(3)
       strcat(3)
	      Copy and catenate the input string into a destination string.  The programmer is responsible for allocating a buffer large enough.   The	return
	      value is useless.

	      stpcpy(3) is a faster alternative to these functions.

       stpecpy()
	      Chain-copy  the  input string into a destination string.	If the destination buffer, limited by a pointer to its end, isn't large enough to hold
	      the copy, the resulting string is truncated (but it is guaranteed to be null-terminated).	 It returns a pointer suitable for chaining.   Trunca‐
	      tion needs to be detected only once after the last chained call.

	      This function is not provided by any library; see EXAMPLES for a reference implementation.

       strtcpy()
	      Copy  the	 input string into a destination string.  If the destination buffer isn't large enough to hold the copy, the resulting string is trun‐
	      cated (but it is guaranteed to be null-terminated).  It returns the length of the string, or -1 if it truncated.

	      This function is not provided by any library; see EXAMPLES for a reference implementation.

       strlcpy(3bsd)
       strlcat(3bsd)
	      Copy and catenate the input string into a destination string.  If the destination buffer, limited by its size, isn't large enough	 to  hold  the
	      copy,  the resulting string is truncated (but it is guaranteed to be null-terminated).  They return the length of the total string they tried to
	      create.

	      Check BUGS before using these functions.

	      strtcpy() and stpecpy() are better alternatives to these functions.

       stpncpy(3)
	      Copy the input string into a destination null-padded character sequence in a fixed-size buffer.  If the destination buffer, limited by its size,
	      isn't large enough to hold the copy, the resulting character sequence is truncated.  Since it creates a character sequence, it doesn't  need  to
	      write  a	terminating  null character.  It's impossible to distinguish truncation by the result of the call, from a character sequence that just
	      fits the destination buffer; truncation should be detected by comparing the length of the input string with the size of the destination buffer.

       strncpy(3)
	      This function is identical to stpncpy(3) except for the useless return value.

	      stpncpy(3) is a more useful alternative to this function.

       strncat(3)
	      Catenate the input character sequence, contained in a null-padded fixed-size buffer, into a destination string.  The programmer  is  responsible
	      for allocating a buffer large enough.  The return value is useless.

	      Do not confuse this function with strncpy(3); they are not related at all.

	      stpcpy(mempcpy(dst, src, strnlen(src, NITEMS(src))), "") is a faster alternative to this function.

       mempcpy(3)
	      Copy the input character sequence, limited by its length, into a destination character sequence.	The programmer is responsible for allocating a
	      buffer large enough.  It returns a pointer suitable for chaining.

RETURN VALUE
       stpcpy(3)
	      A pointer to the terminating null character in the destination string.

       stpecpy()
	      A pointer to the terminating null character in the destination string, on success.  On error, NULL is returned, and errno is set to indicate the
	      error.

       mempcpy(3)
       stpncpy(3)
	      A pointer to one after the last character in the destination character sequence.

       strtcpy()
	      The length of the string, on success.  On error, -1 is returned, and errno is set to indicate the error.

       strlcpy(3bsd)
       strlcat(3bsd)
	      The length of the total string that they tried to create (as if truncation didn't occur).

       strcpy(3)
       strcat(3)
       strncpy(3)
       strncat(3)
	      The dst pointer, which is useless.

ERRORS
       Most of these functions don't set errno.

       stpecpy()
       strtcpy()

	      ENOBUFS
		     dsize was 0.

	      E2BIG  The string has been truncated.

NOTES
       The Linux kernel has an internal function for copying strings, strscpy(9), which is identical to strtcpy(), except that it returns -E2BIG instead of -1
       and it doesn't set errno.

CAVEATS
       Don't  mix  chain calls to truncating and non-truncating functions.  It is conceptually wrong unless you know that the first part of a copy will always
       fit.  Anyway, the performance difference will probably be negligible, so it will probably be more clear if you use consistent semantics:	 either	 trun‐
       cating or non-truncating.  Calling a non-truncating function after a truncating one is necessarily wrong.

BUGS
       All  catenation	functions  share  the  same performance problem: Shlemiel the painter.	As a mitigation, compilers are able to transform some calls to
       catenation functions into normal copy functions, since strlen(dst) is usually a byproduct of the previous copy.

       strlcpy(3) and strlcat(3) need to read the entire src string, even if the destination buffer is small.  This makes them vulnerable to Denial of Service
       (DoS) attacks if an attacker can control the length of the src string.  And if not, they're still unnecessarily slow.

EXAMPLES
       The following are examples of correct use of each of these functions.

       stpcpy(3)
	      p = buf;
	      p = stpcpy(p, "Hello ");
	      p = stpcpy(p, "world");
	      p = stpcpy(p, "!");
	      len = p - buf;
	      puts(buf);

       strcpy(3)
       strcat(3)
	      strcpy(buf, "Hello ");
	      strcat(buf, "world");
	      strcat(buf, "!");
	      len = strlen(buf);
	      puts(buf);

       stpecpy()
	      end = buf + NITEMS(buf);
	      p = buf;
	      p = stpecpy(p, end, "Hello ");
	      p = stpecpy(p, end, "world");
	      p = stpecpy(p, end, "!");
	      if (p == NULL) {
		  len = NITEMS(buf) - 1;
		  goto toolong;
	      }
	      len = p - buf;
	      puts(buf);

       strtcpy()
	      len = strtcpy(buf, "Hello world!", NITEMS(buf));
	      if (len == -1)
		  goto toolong;
	      puts(buf);

       strlcpy(3bsd)
       strlcat(3bsd)
	      if (strlcpy(buf, "Hello ", NITEMS(buf)) >= NITEMS(buf))
		  goto toolong;
	      if (strlcat(buf, "world", NITEMS(buf)) >= NITEMS(buf))
		  goto toolong;
	      len = strlcat(buf, "!", NITEMS(buf));
	      if (len >= NITEMS(buf))
		  goto toolong;
	      puts(buf);

       stpncpy(3)
	      p = stpncpy(u->ut_user, "alx", NITEMS(u->ut_user));
	      if (NITEMS(u->ut_user) < strlen("alx"))
		  goto toolong;
	      len = p - u->ut_user;
	      fwrite(u->ut_user, 1, len, stdout);

       strncpy(3)
	      strncpy(u->ut_user, "alx", NITEMS(u->ut_user));
	      if (NITEMS(u->ut_user) < strlen("alx"))
		  goto toolong;
	      len = strnlen(u->ut_user, NITEMS(u->ut_user));
	      fwrite(u->ut_user, 1, len, stdout);

       mempcpy(dst, src, strnlen(src, NITEMS(src)))
	      char  buf[NITEMS(u->ut_user)];
	      p = buf;
	      p = mempcpy(p, u->ut_user, strnlen(u->ut_user, NITEMS(u->ut_user)));
	      len = p - buf;
	      fwrite(buf, 1, len, stdout);

       stpcpy(mempcpy(dst, src, strnlen(src, NITEMS(src))), "")
	      char  buf[NITEMS(u->ut_user) + 1];
	      p = buf;
	      p = mempcpy(p, u->ut_user, strnlen(u->ut_user, NITEMS(u->ut_user)));
	      p = stpcpy(p, "");
	      len = p - buf;
	      puts(buf);

       strncat(3)
	      char  buf[NITEMS(u->ut_user) + 1];
	      strcpy(buf, "");
	      strncat(buf, u->ut_user, NITEMS(u->ut_user));
	      len = strlen(buf);
	      puts(buf);

       mempcpy(3)
	      p = buf;
	      p = mempcpy(p, "Hello ", 6);
	      p = mempcpy(p, "world", 5);
	      p = mempcpy(p, "!", 1);
	      len = p - buf;
	      fwrite(buf, 1, len, stdout);

       stpcpy(mempcpy(dst, src, len), "")
	      p = buf;
	      p = mempcpy(p, "Hello ", 6);
	      p = mempcpy(p, "world", 5);
	      p = mempcpy(p, "!", 1);
	      p = stpcpy(p, "");
	      len = p - buf;
	      puts(buf);

   Implementations
       Here are reference implementations for functions not provided by libc.

	   /* This code is in the public domain. */

	   char *
	   stpecpy(char *dst, char end[0], const char *restrict src)
	   {
	       size_t  dlen;

	       if (dst == NULL)
		   return NULL;

	       dlen = strtcpy(dst, src, end - dst);
	       return (dlen == -1) ? NULL : dst + dlen;
	   }

	   ssize_t
	   strtcpy(char *restrict dst, const char *restrict src, size_t dsize)
	   {
	       bool    trunc;
	       size_t  dlen, slen;

	       if (dsize == 0) {
		   errno = ENOBUFS;
		   return -1;
	       }

	       slen = strnlen(src, dsize);
	       trunc = (slen == dsize);
	       dlen = slen - trunc;

	       stpcpy(mempcpy(dst, src, dlen), "");
	       if (trunc)
		   errno = E2BIG;
	       return trunc ? -1 : slen;
	   }

SEE ALSO
       bzero(3), memcpy(3), memccpy(3), mempcpy(3), stpcpy(3), strlcpy(3bsd), strncat(3), stpncpy(3), string(3)

Linux man-pages 6.7							  2023-12-17							     string_copying(7)
