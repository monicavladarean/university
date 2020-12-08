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
    a db 2
    e dw 2
    b db 2
    c db 3
    d db 2
    x dq 2
    y db 2
    aux dw 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
		;(a*b-2*c*d)/(c-e)+x/a; a,b,c,d-byte; e-word; x-qword
        MOV AL, [c]
        CBW
        SUB AX,word[e]
        MOV [aux],AX
        
        MOV AL, [a]
        MOV CL,[b]
        IMUL CL
        CWD
        MOV CX,AX
        mov BX, DX
        
        MOV AL,byte[d]
        CBW
        MOV DX,AX
        MOV AL,byte[y]
        IMUL byte[c]
        IMUL DX
        
        SUB CX, AX
        SBB BX,DX
        mov AX, CX
        mov DX,BX
       
        IDIV word[aux]
        CWDE
        MOV ECX,EAX
        
        MOV AL,byte[a]
        CBW
        CWDE
        MOV EBX, EAX
        MOV EAX,dword[x]
		MOV EDX, dword[x+4]
        IDIV EBX
        
        ADD EAX,ECX
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
