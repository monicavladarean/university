bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)      

; declare external functions needed by our program
global _func
extern _printf
extern _s1         ; tell nasm that exit exists even if we won't be defining it  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
global _s2  ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data public data use32 
    ; ...
	alfabet db 'OPQRSTUVWXYZABCDEFGHIJKLMN'   
	format db '%s',0

; our code starts here
segment code public code use32
    ; ...
    _func:
		push ebp
		mov ebp, esp
        mov esi, _s1
        mov edi, _s2
        jecxz finish
        mov ebx, alfabet
        cld
        
        do:
        
        lodsb
        
        cmp al,0
        je stop
        
        sub al,'a'
        xlat 
        stosb 
        jmp do
        
        stop:
        
        finish:
		mov esp, ebp
		pop ebp
        ret
