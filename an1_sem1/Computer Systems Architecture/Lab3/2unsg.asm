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
    a db 1
    b db 4
    c db 2
    d db 1
    e dw 1
    x dq 2
    y db 2
	r dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
		;(a*b-2*c*d)/(c-e)+x/a; a,b,c,d-byte; e-word; x-qword
        MOV AH, 0
        mov AL, [c]
        sub AX,word[e]
        mov BX, AX
        
        mov AL,[c]
        mov AH, [d]
        mul AH
		mov BH,0
        mov BL,[y]
        mul BX
		push DX
		push AX
		pop ECX
		
		mov EAX,0
        mov AL, [b]
        mov AH, [a]
        mul AH
        SUB EAX,ECX
       
        div BX 
		mov EBX,0
        MOV BX, AX
        
        mov EAX, dword[x]
		mov EDX, dword[x+4]
		mov ECX,0
        mov ECX, [a]
        div ECX
        add EBX, EAX 
		mov [r], EBX
   
         
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
