bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 11010010b
    b dw 1100101000110110b
    c dd 0b
    
; our code starts here
    ;Given the byte A and the word B, compute the doubleword C as follows:
    ;the bits 24-31 of C are the same as the bits of A
    ;the bits 15-23 of C are the invert of the bits of the lowest byte of B
    ;the bits 10-14 of C have the value 1
    ;the bits 2-9 of C are the same as the bits of the highest byte of B
    
    ;the bits 0-1 both contain the value of the sign bit of A
segment code use32 class=code
    start:
        ; ...
        mov CL,24
        mov EBX,0
        mov BL,[a]
        SHL EBX,CL
        or [c], EBX
        
        mov EBX, [b]
        not EBX
        and EBX,00000000000000000000000111111111b
        shl EBX,15
        or [c],EBX
        
        or dword[c],00000000000001111110000000000b
        mov EAX,[c]
        
        mov EBX,0
        mov BX, [b]
        and EBX,00000000000000001111111100000000b
        shr EBX,6
        or [c],EBX
        
        mov EAX,0
        mov AL, [a]
        and AL, 10000000
        shr AL,7
        or [c],EAX
        
        shl AL,1
        or [c],EAX
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
