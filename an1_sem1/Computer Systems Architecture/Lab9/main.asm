bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,scanf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll 
extern func   ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
global format
global s2
global s1
global alfabet

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    alfabet db 'OPQRSTUVWXYZABCDEFGHIJKLMN'
    format dd"%s",0
    s1 resb 100
    s2 resb 100
; our code starts here
segment code use32 class=code
    
    start:
        ; ...
        push dword s1
        push dword format
        call [scanf]
        add esp, 4*2
        call func
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
