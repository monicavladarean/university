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
    sir DB 2, 4, 2, 5, 2, 2, 4, 4 
    len equ $-sir
    rez resw len

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, sir
        mov ecx, len
        mov edi, rez
        cld
        
        repeta:
        
        lodsb
        mov BL,AL
        mov BH,0
        push esi
        push ecx
        mov ecx, len
        mov esi,sir
        
        do:
        lodsb
        cmp AL,BL
        jne continue
        
        add BH,1
        
        continue:
        
        loop do
        
        pop ecx
        pop esi
        mov AX,BX
        stosw
        
        loop repeta
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
