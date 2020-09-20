# Parser

Several problems consist in parser/evaluating an expression.

!227 basic calculator
!726 number of atoms
!394 decode string
!536 construct binary tree

All these problems are more easily solved using a stack (rather than
recursive descending parsing).

Tokens are stacked up, until they can be "reduced" on the stack.
If the stack stays bounded, it may not be needed.