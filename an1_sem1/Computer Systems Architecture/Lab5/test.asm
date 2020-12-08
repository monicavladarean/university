bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,fopen ,fclose,printf,fread            ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fclose msvcrt.dll 
import printf msvcrt.dll 
import fread msvcrt.dll 

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
sir db "abcdefghij"
file_descriptor dd -1
file_name db "input.txt",0
n1 db 0
access_read dd "r",0
print_nr dd "%s",0
rez db ""
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword access_read
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor],eax
        cmp eax,0
        je stop
        
        push dword [file_descriptor]
        push dword 1
        push dword 1
        push dword n1
        call [fread]
        add esp,4*4

        
        mov ecx,2
        add ecx,1
        
        mov esi, sir
        mov edi, rez
        cld
        
        do:
       
        sub ecx,1
        
        lodsb
        stosb
        
        pushad
        
        push dword rez
        push dword print_nr
        call [printf]
        add esp, 4*2
        

        
        push dword 0
        push dword print_nr
        call [printf]
        add esp, 4*2
        
        popad
        
        cmp ecx,0
        jne do
     
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4*1
        
        stop:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
