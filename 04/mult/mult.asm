// This file is part of www.nand2tetris.org

// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)


//a = RAM[0]
//b = RAM[1]
//i = b
//LOOP
//if i < 0 goto end
//c = a + b
// i = i -1
@R0 
  D=M
@R1
  D = M
@i
  M=D
@R2
 M=0
(LOOP)
  @i
    D=M
  @END
  D;JEQ

  @R0
    D=M
  @R2
    M=M+D
  @i
    M = M-1
  @LOOP
  0;JMP

(END)
  @END
  0;JMP





