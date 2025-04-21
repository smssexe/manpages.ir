string(3)							   Library Functions Manual							     string(3)

NAME
       stpcpy, strcasecmp, strcat, strchr, strcmp, strcoll, strcpy, strcspn, strdup, strfry, strlen, strncat, strncmp, strncpy, strncasecmp, strpbrk, strrchr,
       strsep, strspn, strstr, strtok, strxfrm, index, rindex - string operations

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <strings.h>

       int strcasecmp(const char *s1, const char *s2);
	      Compare the strings s1 and s2 ignoring case.

       int strncasecmp(const char s1[.n], const char s2[.n], size_t n);
	      Compare the first n bytes of the strings s1 and s2 ignoring case.

       char *index(const char *s, int c);
	      Identical to strchr(3).

       char *rindex(const char *s, int c);
	      Identical to strrchr(3).

       #include <string.h>

       char *stpcpy(char *restrict dest, const char *restrict src);
	      Copy a string from src to dest, returning a pointer to the end of the resulting string at dest.

       char *strcat(char *restrict dest, const char *restrict src);
	      Append the string src to the string dest, returning a pointer dest.

       char *strchr(const char *s, int c);
	      Return a pointer to the first occurrence of the character c in the string s.

       int strcmp(const char *s1, const char *s2);
	      Compare the strings s1 with s2.

       int strcoll(const char *s1, const char *s2);
	      Compare the strings s1 with s2 using the current locale.

       char *strcpy(char *restrict dest, const char *restrict src);
	      Copy the string src to dest, returning a pointer to the start of dest.

       size_t strcspn(const char *s, const char *reject);
	      Calculate the length of the initial segment of the string s which does not contain any of bytes in the string reject,

       char *strdup(const char *s);
	      Return a duplicate of the string s in memory allocated using malloc(3).

       char *strfry(char *string);
	      Randomly swap the characters in string.

       size_t strlen(const char *s);
	      Return the length of the string s.

       char *strncat(char dest[restrict strlen(.dest) + .n + 1],
		     const char src[restrict .n],
		     size_t n);
	      Append at most n bytes from the unterminated string src to the string dest, returning a pointer to dest.

       int strncmp(const char s1[.n], const char s2[.n], size_t n);
	      Compare at most n bytes of the strings s1 and s2.

       char *strpbrk(const char *s, const char *accept);
	      Return a pointer to the first occurrence in the string s of one of the bytes in the string accept.

       char *strrchr(const char *s, int c);
	      Return a pointer to the last occurrence of the character c in the string s.

       char *strsep(char **restrict stringp, const char *restrict delim);
	      Extract the initial token in stringp that is delimited by one of the bytes in delim.

       size_t strspn(const char *s, const char *accept);
	      Calculate the length of the starting segment in the string s that consists entirely of bytes in accept.

       char *strstr(const char *haystack, const char *needle);
	      Find the first occurrence of the substring needle in the string haystack, returning a pointer to the found substring.

       char *strtok(char *restrict s, const char *restrict delim);
	      Extract tokens from the string s that are delimited by one of the bytes in delim.

       size_t strxfrm(char dest[restrict .n], const char src[restrict .n],
		      size_t n);
	      Transforms src to the current locale and copies the first n bytes to dest.

       char *strncpy(char dest[restrict .n], const char src[restrict .n],
		     size_t n);
	      Fill a fixed-size buffer with leading non-null bytes from a source array, padding with null bytes as needed.

DESCRIPTION
       The string functions perform operations on null-terminated strings.  See the individual man pages for descriptions of each function.

SEE ALSO
       bstring(3),  stpcpy(3),	strcasecmp(3),	strcat(3),  strchr(3),	strcmp(3),  strcoll(3),	 strcpy(3), strcspn(3), strdup(3), strfry(3), strlen(3), strn‐
       casecmp(3), strncat(3), strncmp(3), strncpy(3), strpbrk(3), strrchr(3), strsep(3), strspn(3), strstr(3), strtok(3), strxfrm(3)

Linux man-pages 6.7							  2023-11-14								     string(3)
