operator(7)						       Miscellaneous Information Manual							   operator(7)

NAME
       operator - C operator precedence and order of evaluation

DESCRIPTION
       This manual page lists C operators and their precedence in evaluation.

       Operator				   Associativity   Notes
       [] () . -> ++ --			   left to right   [1]
       ++ -- & * + - ~ ! sizeof		   right to left   [2]
       (type)				   right to left
       * / %				   left to right
       + -				   left to right
       << >>				   left to right
       < > <= >=			   left to right
       == !=				   left to right
       &				   left to right
       ^				   left to right
       |				   left to right
       &&				   left to right
       ||				   left to right
       ?:				   right to left
       = *= /= %= += -= <<= >>= &= ^= |=   right to left
       ,				   left to right

       The following notes provide further information to the above table:

       [1]  The ++ and -- operators at this precedence level are the postfix flavors of the operators.
       [2]  The ++ and -- operators at this precedence level are the prefix flavors of the operators.

Linux man-pages 6.7							  2023-10-31								   operator(7)
