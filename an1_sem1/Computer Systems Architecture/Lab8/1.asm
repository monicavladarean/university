bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern scanf
import scanf msvcrt.dll 
extern printf
import printf msvcrt.dll 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    x dd 0
    read db "%x",0
    print db "%d",  0
    print2 db "%u",10, 13, 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword x
        push dword read
        call [scanf]
        add esp, 4*2
        
        push dword [x]
        push dword print2
        call [printf]
        add esp, 4*2
        
        mov AL, byte[x]
        CBW
        CWDE
        
        push EAX
        push dword print
        call [printf]
        add esp, 4*2
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
