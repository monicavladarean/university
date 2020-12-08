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
    aux resb len
    lenght db 0
    rez resw len

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, sir
        mov ecx, len
        mov edi, aux
        
        repeta:
        
        lodsb
        mov BL,AL
        push esi
        push ecx
        mov esi, aux
        mov ecx, [lenght]
        jecxz adauga
        do:
        
        lodsb
        cmp AL, BL
        je break
        
        loop do
        break:
        cmp ecx,0
        
        jne continua
        adauga:
        mov AL,BL
        stosb
        inc byte[lenght]
        continua:
        pop ecx
        pop esi
        
        loop repeta
        
        mov ecx, [lenght]
        mov esi, aux
        mov edi, rez
        repeta2:
        
        lodsb 
        mov BL, AL
        push esi
        push ecx
        mov ecx, len
        mov esi, sir
        mov BH,0
        do2:
        
        lodsb
        cmp AL,BL
        jne continue
        add BH,1
        continue:
        loop do2
        mov AX,BX
        stosw
        pop ecx
        pop esi
        
        loop repeta2
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
