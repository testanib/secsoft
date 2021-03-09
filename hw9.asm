ection .text: 
        global _start ;;tells the linker where start is

_start:  
        xor ebx, ebx
        push ebx
        ;;push 0x0a21 ;;push '!'
        ;;push 0x646c726f 
        ;;push 0x57202c6f ;;push 'o, W' 
        ;;push 0x6c6c6548 ;; push 'Hell' in little-endian
        ;;push 0xa2d
        ;;mov ebx, 1 ;; the file descript, stdout in this case
        ;;mov ecx, esp ;; address to read from
        ;;mov edx, 15  ;; len of message
        mov eax, 79 ;; sys_call number 
        int 0x80 ;; call to kernel
        mov ebx, 1
        mov ecx, esp
        mov edx, 20
        mov eax, 4
        int 0x80
        xor ebx, ebx
 
        mov eax, 1 ;; sys_call number (exit) 
        int 0x80 ;; call to kernel
