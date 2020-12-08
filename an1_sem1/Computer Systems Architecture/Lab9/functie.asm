bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)      

; declare external functions needed by our program
global _func
extern _printf
extern s2  
extern s1         ; tell nasm that exit exists even if we won't be defining it  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
             ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
global func

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
	alfabet db 'OPQRSTUVWXYZABCDEFGHIJKLMN'   
	format db '%s',0

; our code starts here
segment code use32 class=code
    ; ...
    _func:
		push ebp
		mov ebp, esp
        mov esi, s1
        mov edi, s2
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
        
        push dword s2
        push dword format
        call _printf
        add esp, 4*2
        
        finish:
		mov esp, ebp
		pop ebp
        ret
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
