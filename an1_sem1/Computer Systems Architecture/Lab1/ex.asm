bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,fopen,fread,printf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fread msvcrt.dll                                                ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll  

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    acces_mode dd "a+",0
    file_name db "ion.txt",0
    file_descriptor dd -1
    len equ 100
    sir times len+1 db 0
    rez times len+1 db 0
    nr_caract dd 0
    format dd "%s",0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push dword acces_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor],eax
        cmp eax,0
        je stop
        
        push dword [file_descriptor]
        push dword len
        push dword 1
        push dword sir
        
        call [fread]
        add esp, 4*4
        
        mov [nr_caract],eax
        cmp eax,0
        je stop
        
        mov ecx, [nr_caract]
        
        mov esi, sir
        mov edi, rez
        
        repeta:
        
        do:
        
        lodsb
        
        cmp al,'.'
        je jos
        
        add al,1
        
        jos:
        
        stosb
        sub dword[nr_caract],1
        
        loop do
        
        cmp dword[nr_caract],0
        jne repeta
        
        push dword rez
        push dword format
        call [printf]
        add esp, 4*2

        
        
        stop:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
