bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fscanf, fprintf         ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import exit msvcrt.dll
import fopen msvcrt.dll
import fscanf msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "ion.txt", 0   
    access_mode db "a+", 0         
    file_descriptor dd -1
    format dd "%x",0
    n dd 0
    x dd 0
    print2 db 10, 13,"%x", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword access_mode     
        push dword file_name
        call [fopen]
        add esp, 4*2  
        
        mov [file_descriptor], eax 
        cmp eax,0
        je stop
        
        push dword n
        push dword format   
        push dword [file_descriptor]        
        call [fscanf]
        add esp, 4*3
        
        mov BX,word[n]
        mov ECX,8
        
        do:
        
        mov DX,1111b
        and DX,BX
        mov [x],DX
        shr BX,4
        
        push ECX
        
        push dword [x]
        push print2
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*3
        pop ECX
        loop do
        
        
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        stop:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
