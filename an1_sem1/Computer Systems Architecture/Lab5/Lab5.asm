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
    
    s db 1, 4, 2, 4, 8, 2, 1, 1
    len equ $-s 
    d resb len 
    
; our code starts here
segment code use32 class=code
        ; ...
        ;A byte string S is given. Obtain in the string D the set of the elements of S. 
        ;Example:
        ;S: 1, 4, 2, 4, 8, 2, 1, 1
        ;D: 1, 4, 2, 8
    start:
    
        mov esi, s
        mov edi, d
        mov ecx, len
        cld
        jecxz stop
        
        repeta:
        
        mov al,[esi]
        push ecx
        mov ecx,edi
        sub ecx, d 
        jecxz adaugare
        
        mov ebx, d
        repeta2:
        
        cmp al, [ebx]
        
        JE nu_adauga
        inc ebx 
        loop repeta2
		
        jecxz adaugare
        
        nu_adauga:
        inc esi
        jmp continua
        
        adaugare:  
        mov [edi], al
        inc edi
        inc esi
        
        continua:
        pop ecx
        jecxz stop
        loop repeta
		
        stop:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
