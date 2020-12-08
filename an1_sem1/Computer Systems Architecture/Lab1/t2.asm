bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,fopen  ,fread,fclose ,printf         ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll 
import fread msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll 
import fclose msvcrt.dll 


; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    acces1 dd "a+",0 
    filer db "p.txt",0
    file_descriptor dd -1
    format db "%s",0
    len equ 100
    sir times len+1 db 0
    rez times len+1 db 0
    nr_caract dd 0
    nr_cuv dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword acces1
        push dword filer
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
        
        mov ecx,eax
        mov esi, sir
        mov edi,rez
        
         mov [nr_caract], eax
        
        ; Initializam registrii pentru parcurgere
        ; In rezultat vom avea la fiecare propozitie primul cuvant si numarul de cuvinte
        
        mov esi, sir
        mov edi, rez
        cld 
        mov ecx, [nr_caract]
        
        
        
        
        prop:
        ; Parcurgem cate o propozitie pana intalnim primul cuvant, memorand in acelasi timp literele din acesta
        ; in sirul rez
        
        lodsb
        sub ecx, 1
        cmp ecx, 0
        je finish
        
        stosb
        
        cmp al, ' '
        je primcuv
               
        jmp prop
        
        
        primcuv:
        ; Dupa ce am gasit primul cuvant incrementam numarul de cuvinte si parcurgem restul cuvintelor 
        
        add dword [nr_cuv], 1
        
        repeta:
        
        lodsb
        sub ecx, 1
        cmp al, ' '
        je primcuv      ; Daca am gasit spatiu reluam ciclul primcuv 
        
        cmp al, '.'     ; Cand am gasit punct sarim la below 
        je below
        
        jmp repeta     ; daca nu am gasit nici punct nici spatiu continuam parcurgerea
        
        below:
        
        ; O propozitie nu poate avea mai mult de 9 cuvinte.
        ; Dupa '.' urmeaza ' '
        ; Inainte de '.' nu se pune spatiu
        ; In acest moment am gasit caracterul .
        
        lodsb            ; incarcam si spatiul pentru a incepe urmatoarea propozitie de la litera
        sub ecx, 1
        
        
        add dword [nr_cuv], 1      ; numaram si ultimul cuvant care nu a fost adaugat
        
        mov edx, '0'               ; formam din int un char pentru a putea adauga nr_cuv la sirul rezultat
        add dword [nr_cuv], edx
        mov eax, dword[nr_cuv]
        
        stosb                      ; incarcam numarul de cuvinte
        mov al, ' '
        stosb                      ; incarcam si spatiu pentru a afisara corespunzator
        
        pushad
        
        push dword rez                    ; afisam primul cuvant si nr de cuvinte curente
        push dword format
        call [printf]
        add esp, 4*2
        
        popad
        
        
        mov edi, rez                     ; reinitializam sirul destinatie pentru a putea parcurge 
                                         ; urmatoare propozitie
        cld
        mov dword [nr_cuv], 0
        
        cmp ecx, 0                       ; pentru ca am mai incrcat un spatiu verificam daca am ajuns la finalul textului
        je finish
        
        
        jmp prop
        
        
        
        
        finish:
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        

        stop:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
