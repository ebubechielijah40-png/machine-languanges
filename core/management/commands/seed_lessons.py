from django.core.management.base import BaseCommand
from core.models import Language, Lesson


class Command(BaseCommand):
    help = 'Seed C, Assembly, and Machine Language lessons with detailed content and coding challenges'

    def handle(self, *args, **options):
        c_language, _ = Language.objects.get_or_create(
            name='C',
            defaults={'description': 'A low level language that sits close to the hardware while remaining readable.'},
        )
        assembly_language, _ = Language.objects.get_or_create(
            name='Assembly',
            defaults={'description': 'The human-readable form of processor instructions.'},
        )
        machine_language, _ = Language.objects.get_or_create(
            name='Machine Language',
            defaults={'description': 'The raw binary and hex instructions the CPU executes directly.'},
        )

        c_lessons = [
            {
                'order': 1,
                'title': 'What is C',
                'content': (
                    'C is a compiled language created to give programmers direct control over the machine without requiring them to write every instruction by hand. '
                    'It was designed in the early 1970s as a practical language for systems software, and it became the foundation for operating systems, compilers, and embedded tools. '
                    'C sits above Assembly in abstraction but below high level languages such as Python because it still exposes memory and processor behavior. '
                    'When people say a language is close to the metal, they mean it is still explicit about storage, addresses, and control flow. '
                    'This is why operating systems, device drivers, and firmware are often written in C. '
                    'The compiler translates C into Assembly and then into machine instructions that the CPU can execute.'
                ),
                'challenge': 'Write a C program with just a main function that returns 0. Add a comment explaining what return 0 tells the operating system.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    // your code here\n    return 0;\n}',
            },
            {
                'order': 2,
                'title': 'Your first program',
                'content': (
                    'A C program begins with preprocessing directives such as #include. The preprocessor reads these lines before compilation and inserts the contents of standard headers such as stdio.h. '
                    'The file stdio.h provides declarations for input and output functions, including printf. '
                    'The function main is the entry point. The operating system calls main when the program starts, so every executable C program must define it. '
                    'The printf function writes text to standard output. The escape sequence \\n moves the cursor to the next line so the output is easier to read. '
                    'The return 0 statement signals that the program completed successfully. The operating system uses that status code to decide whether the program ran without error.'
                ),
                'challenge': 'Modify the program to print your name and the current year on separate lines using two printf calls.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}',
            },
            {
                'order': 3,
                'title': 'Variables and data types',
                'content': (
                    'A variable is a named location in memory. The compiler reserves a fixed number of bytes for it and gives that region a symbolic name so the program can refer to it. '
                    'The type of the variable tells the machine how to interpret those bits. An int is commonly 4 bytes and stores whole numbers, a char is 1 byte and stores a character code, and a float is usually 4 bytes and stores fractional values. '
                    'Signed types can represent negative values while unsigned types only represent zero and positive values. '
                    'When an integer overflows, the stored bits wrap around and the result can become incorrect, which is one reason low level programming requires care. '
                    'The machine does not understand the words int or float; it only sees the bytes and the instructions that operate on them.'
                ),
                'challenge': 'Declare an int, a char, and a float. Assign values to each. Print each one using the correct printf format specifier (%d, %c, %f).',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    int age;\n    char letter;\n    float temperature;\n    return 0;\n}',
            },
            {
                'order': 4,
                'title': 'Operators',
                'content': (
                    'Operators tell the compiler which computation the machine should perform. Arithmetic operators such as +, -, *, and / produce new values in memory or in registers. '
                    'Comparison operators such as ==, !=, <, and > produce a result that is interpreted as true or false, usually as 1 or 0. '
                    'Logical operators such as &&, ||, and ! combine boolean results and are used to express compound conditions. '
                    'Operator precedence determines the order in which the compiler groups parts of an expression before it emits instructions. '
                    'At the machine level, each operator becomes a sequence of instructions that move data, compute, and store the result.'
                ),
                'challenge': 'Write a program that takes two hardcoded integers, performs all arithmetic operations on them, and prints each result with a label.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    int a = 10;\n    int b = 3;\n    // perform operations here\n    return 0;\n}',
            },
            {
                'order': 5,
                'title': 'Control flow',
                'content': (
                    'The CPU executes instructions in sequence unless it is told to change direction. Control flow constructs such as if and else provide that instruction. '
                    'An if statement evaluates a condition and then chooses one path or another. At the machine level, this becomes a conditional jump that changes the instruction pointer. '
                    'The comparison operation produces flags inside the CPU, and the jump uses those flags to decide whether to continue or branch. '
                    'This is the mechanism by which programs make decisions instead of simply running from top to bottom.'
                ),
                'challenge': 'Write a program that checks if a number is positive, negative, or zero and prints the result.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    int number = -5;\n    // check and print\n    return 0;\n}',
            },
            {
                'order': 6,
                'title': 'Loops',
                'content': (
                    'Loops are repeated jumps. A loop causes the processor to revisit the same block of instructions until a condition changes. '
                    'A for loop has three parts: initialization, condition checking, and increment or decrement. '
                    'A while loop checks a condition before each iteration and repeats while the condition remains true. '
                    'Both forms compile into machine code that uses branches to return to the start of the loop body. '
                    'This makes repetition possible without writing the same instructions over and over by hand.'
                ),
                'challenge': 'Write a for loop that prints numbers 1 to 10. Then rewrite it as a while loop that does the same thing.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    // for loop here\n    \n    // while loop here\n    return 0;\n}',
            },
            {
                'order': 7,
                'title': 'Functions',
                'content': (
                    'A function groups instructions into a reusable unit. When a function is called, the machine pushes the return address onto the stack, jumps to the function body, and later resumes execution at the caller. '
                    'Parameters are passed to the function so it can work on specific values, and the return value is sent back to the caller. '
                    'This mechanism depends on the call stack and on the compiler arranging arguments and return addresses correctly. '
                    'Functions keep code organized and make it possible to reuse behavior without duplicating machine instructions.'
                ),
                'challenge': 'Write a function called add that takes two integers and returns their sum. Call it from main and print the result.',
                'starter_code': '#include <stdio.h>\n\nint add(int a, int b) {\n    // return the sum\n}\n\nint main() {\n    int result = add(5, 3);\n    return 0;\n}',
            },
            {
                'order': 8,
                'title': 'Pointers',
                'content': (
                    'Every variable resides at some memory address. A pointer is a variable that stores one of those addresses instead of storing the value directly. '
                    'The address-of operator & produces the location of a variable, while the dereference operator * reads or writes the value stored at that location. '
                    'C exposes pointers because low level programming requires direct control over memory. Other languages often hide this detail, but C allows the programmer to work with addresses explicitly when needed. '
                    'This is useful for arrays, strings, data structures, and performance-sensitive code.'
                ),
                'challenge': 'Declare an integer. Create a pointer to it. Print both the value and the memory address. Then change the value through the pointer and print again.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    int x = 42;\n    int *ptr = &x;\n    // print address and value\n    return 0;\n}',
            },
            {
                'order': 9,
                'title': 'Arrays',
                'content': (
                    'An array is a contiguous block of memory containing multiple values of the same type. The array name points to the first element, so indexing is really a form of pointer arithmetic. '
                    'The machine computes the address of each element by multiplying the index by the size of the element and adding that offset to the base address. '
                    'Arrays start at index 0 because the first element is at the base address and each later element is offset from it. '
                    'This layout is efficient because related values are stored next to each other in memory.'
                ),
                'challenge': 'Declare an array of 5 integers. Fill it with values. Print each element using a loop. Then print the memory address of each element to show they are contiguous.',
                'starter_code': '#include <stdio.h>\n\nint main() {\n    int numbers[5] = {10, 20, 30, 40, 50};\n    // print values and addresses\n    return 0;\n}',
            },
            {
                'order': 10,
                'title': 'Structs',
                'content': (
                    'A struct groups related pieces of data into one memory block. The compiler lays out each field in order, usually with padding to preserve alignment requirements. '
                    'This allows a program to treat a collection of values as one object while still keeping them stored close together in memory. '
                    'The dot operator accesses members by name, and the compiler translates that into an offset from the start of the struct. '
                    'Structs are useful for representing records such as CPU state, network packets, or configuration values.'
                ),
                'challenge': 'Create a struct called CPU with fields: name (char array), cores (int), clock_speed (float). Create an instance, assign values, and print all fields.',
                'starter_code': '#include <stdio.h>\n\nstruct CPU {\n    char name[50];\n    int cores;\n    float clock_speed;\n};\n\nint main() {\n    struct CPU processor;\n    // assign and print\n    return 0;\n}',
            },
        ]

        for item in c_lessons:
            Lesson.objects.update_or_create(
                language=c_language,
                order=item['order'],
                defaults={
                    'title': item['title'],
                    'content': item['content'],
                    'challenge': item['challenge'],
                    'starter_code': item['starter_code'],
                },
            )

        assembly_lessons = [
            {
                'order': 1,
                'title': 'What is Assembly',
                'content': (
                    'Assembly is the human-readable form of machine instructions. It is closer to the CPU than C because each statement maps to a small set of processor operations. '
                    'The assembler translates this notation into machine code that the processor can execute directly. '
                    'It exposes registers, memory addresses, and branching behavior in a way that high level languages hide. '
                    'This makes Assembly useful when the programmer needs precise control over execution and resource use. '
                    'It is often used in kernels, boot code, and low level performance work.'
                ),
                'challenge': 'Write a comment block in Assembly describing what each section directive does. Add section .text and section .data to your file.',
                'starter_code': '; Assembly program structure\n; Write your comments here\n\nsection .data\n\nsection .text\n    global _start\n\n_start:\n',
            },
            {
                'order': 2,
                'title': 'Registers',
                'content': (
                    'Registers are the processor storage locations that are fastest to access. x86-64 systems use names such as rax, rbx, rcx, and rdx for general purpose work, and they also use specialized registers for stack and instruction pointers. '
                    'The CPU uses registers to hold values being computed, addresses being manipulated, and temporary state during execution. '
                    'Because registers are inside the processor itself, they are faster than RAM and are used heavily in every instruction sequence. '
                    'A basic understanding of registers is required before any Assembly program can be read or written effectively.'
                ),
                'challenge': 'Write Assembly that loads different values into rax, rbx, rcx, and rdx. Add a comment on each line explaining what that register is typically used for.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    mov rax, 0    ; accumulator\n    mov rbx, 0    ; base\n    mov rcx, 0    ; counter\n    mov rdx, 0    ; data\n',
            },
            {
                'order': 3,
                'title': 'MOV instruction',
                'content': (
                    'The MOV instruction copies data from one place to another. It can move an immediate value into a register, copy one register into another, or move a value between a register and memory. '
                    'MOV does not perform arithmetic. It simply changes the location of the bits. '
                    'That makes it the basic building block for data movement, and most programs depend on it before they can do anything more interesting.'
                ),
                'challenge': 'Move the value 100 into rax. Move the value in rax into rbx. Move the value 200 into rcx. Then move rcx into rdx.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    ; move values between registers\n',
            },
            {
                'order': 4,
                'title': 'Arithmetic instructions',
                'content': (
                    'Arithmetic instructions such as ADD, SUB, and MUL operate directly on register contents. The processor performs the calculation using its arithmetic logic unit and updates flags that may be used later by branches. '
                    'These instructions are the low level basis for counters, loops, and arithmetic expressions. '
                    'A small arithmetic sequence in Assembly is often enough to realize the same logic that a high level language expresses with a single operator.'
                ),
                'challenge': 'Load 20 into rax and 7 into rbx. Add them. Store the result in rcx. Subtract rbx from rax. Store the result in rdx.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    mov rax, 20\n    mov rbx, 7\n    ; add and subtract here\n',
            },
            {
                'order': 5,
                'title': 'Logical operators',
                'content': (
                    'Logical instructions such as AND, OR, and XOR combine bit patterns in ways that are useful for masks, flags, and bit manipulation. '
                    'These are not the same as high level boolean operators, although they often serve similar purposes. '
                    'The CPU performs them at the bit level, and the result remains a number stored in a register. '
                    'This is why Assembly is often used for low level protocol handling and hardware control.'
                ),
                'challenge': 'Load 0xFF into rax and 0x0F into rbx. Perform AND, OR, and XOR and store each result in a different register.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    mov rax, 0xFF\n    mov rbx, 0x0F\n    ; logical operations here\n',
            },
            {
                'order': 6,
                'title': 'Comparisons',
                'content': (
                    'The CMP instruction compares two values and updates CPU flags such as zero, carry, and sign. Those flags are then used by conditional jumps. '
                    'This is the mechanism that lets the processor decide whether a branch should be taken. '
                    'Without comparisons and flags, Assembly would be limited to sequential execution and would not be able to express decisions. '
                    'This is why conditionals in high level languages ultimately rely on these low level flag updates.'
                ),
                'challenge': 'Load 10 into rax and 20 into rbx. Use CMP to compare them. Add a comment explaining what flags the CPU sets based on the result.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    mov rax, 10\n    mov rbx, 20\n    cmp rax, rbx\n    ; what flags are set?\n',
            },
            {
                'order': 7,
                'title': 'Jumps and labels',
                'content': (
                    'Jump instructions change the instruction pointer so execution continues at a different location. Labels provide symbolic names for those destinations. '
                    'A conditional jump uses the status flags set by a previous comparison or arithmetic instruction to decide whether the branch should be taken. '
                    'This is how loops and if statements are represented at the machine level. '
                    'The CPU does not see the concept of a loop as a high level abstraction; it sees a branch back to an earlier instruction.'
                ),
                'challenge': 'Write a loop using a label and JNZ that counts from 5 down to 0 using rcx as the counter.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    mov rcx, 5\nloop_start:\n    ; decrement and jump\n',
            },
            {
                'order': 8,
                'title': 'The stack',
                'content': (
                    'The stack is a region of memory used for temporary storage and for preserving state during function calls. PUSH places data on top of the stack and POP removes it. '
                    'The stack pointer register tracks the current top of the stack, so every push and pop updates that position. '
                    'Function calls rely on the stack to store return addresses and local state. '
                    'When code is written at a low level, the stack becomes an essential tool for organizing work and preserving context.'
                ),
                'challenge': 'Push the values 1, 2, 3 onto the stack in order. Then pop them and move each into rax, rbx, rcx respectively. Add comments explaining the order they come off.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    ; push values\n    push 1\n    push 2\n    push 3\n    ; pop values\n',
            },
            {
                'order': 9,
                'title': 'Functions',
                'content': (
                    'Functions in Assembly are just labeled blocks of instructions that can be reached with CALL and exited with RET. The call instruction saves the return address so execution can continue after the function returns. '
                    'The called function may use registers and the stack to perform work before returning a value. '
                    'This is the same general mechanism that higher level languages use behind the scenes, but Assembly exposes it directly. '
                    'Understanding this pattern is necessary for reading compiler output and writing reusable low level routines.'
                ),
                'challenge': 'Write a function called double_it that takes a value in rdi, doubles it, and returns it in rax. Call it from _start with the value 7.',
                'starter_code': 'section .text\n    global _start\n\ndouble_it:\n    ; your function here\n    ret\n\n_start:\n    mov rdi, 7\n    call double_it\n',
            },
            {
                'order': 10,
                'title': 'Interrupts',
                'content': (
                    'Interrupts and system calls are the boundary between user code and the operating system. A program requests a service by placing a system call number in a register and then issuing an interrupt or syscall instruction. '
                    'This is how Assembly programs perform file I/O, exit, and other privileged operations. '
                    'The operating system receives the request, performs the action, and returns control to the program. '
                    'This is one of the clearest places where Assembly meets the machine and the OS directly.'
                ),
                'challenge': 'Write an Assembly program that uses interrupt 0x80 or syscall to exit cleanly with exit code 0.',
                'starter_code': 'section .text\n    global _start\n\n_start:\n    mov rax, 60    ; syscall: exit\n    xor rdi, rdi   ; exit code 0\n    syscall\n',
            },
            {
                'order': 11,
                'title': 'Memory addressing',
                'content': (
                    'Assembly can access data in memory by address. The LEA instruction computes an address and places it in a register, while direct memory addressing loads the contents from that address. '
                    'This distinction matters because a program often needs either the address of a value or the value itself. '
                    'The machine uses address calculations constantly when reading variables, arrays, and structures. '
                    'Learning this form of addressing makes later work with pointers and data layout much easier to understand.'
                ),
                'challenge': 'Define a variable in the .data section. Load its address into rax using lea. Then load its value into rbx using direct memory addressing.',
                'starter_code': 'section .data\n    myvar dq 42\n\nsection .text\n    global _start\n\n_start:\n    lea rax, [myvar]\n    mov rbx, [myvar]\n',
            },
            {
                'order': 12,
                'title': 'First Assembly program',
                'content': (
                    'A complete Assembly program usually has a data section for constants and a text section for instructions. The data section stores strings and initialized values, while the text section contains the executable instructions. '
                    'The first instruction sequence usually sets up a system call request and then issues the call. '
                    'This low level structure reveals how even a simple program is built from data, instructions, and OS interaction. '
                    'Once a student can read this pattern, the rest of Assembly becomes much easier to follow.'
                ),
                'challenge': 'Write a complete Assembly program that writes HELLO to stdout using the write syscall and then exits cleanly.',
                'starter_code': 'section .data\n    msg db "HELLO", 10\n    msglen equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    ; write syscall\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, msglen\n    syscall\n    ; exit\n    mov rax, 60\n    xor rdi, rdi\n    syscall\n',
            },
        ]

        for item in assembly_lessons:
            Lesson.objects.update_or_create(
                language=assembly_language,
                order=item['order'],
                defaults={
                    'title': item['title'],
                    'content': item['content'],
                    'challenge': item['challenge'],
                    'starter_code': item['starter_code'],
                },
            )

        machine_lessons = [
            {
                'order': 1,
                'title': 'What machine language is',
                'content': (
                    'Machine language is the instruction form that the CPU executes directly. It is encoded as binary or hexadecimal bytes that specify opcodes, registers, and immediate values. '
                    'Assembly is a human-readable representation of these instructions, but the processor only understands the raw bytes. '
                    'This is why the instruction set architecture defines exactly how each opcode must be interpreted. '
                    'A programmer who learns machine language sees the hardware interface directly and can reason about instruction encoding instead of abstractions.'
                ),
                'challenge': 'Given the byte B8, look it up in the x86 opcode table provided in the lesson. Identify what instruction family it belongs to and what register it targets.',
                'starter_code': '; This is not Assembly. This is what the CPU sees.\n; B8 05 00 00 00\n; Decode this manually in the comments below.\n',
            },
            {
                'order': 2,
                'title': 'Assembly to machine code',
                'content': (
                    'An Assembly instruction is usually translated into a small sequence of bytes. The opcode identifies the operation while the remaining bytes provide the operands and immediate values. '
                    'For example, a MOV instruction may be encoded as an opcode plus a register selector and a literal number. '
                    'The exact encoding depends on the architecture and on whether the operand is a register, a memory address, or an immediate value. '
                    'Learning this translation reveals how the assembler works and why instruction encoding must be precise.'
                ),
                'challenge': 'Write the Assembly instruction MOV rax, 1 and below it in comments write what you think its hex encoding would be based on the lesson.',
                'starter_code': '; MOV rax, 1 in Assembly\n; In hex this is approximately:\n; 48 B8 01 00 00 00 00 00 00 00\n; Explain each byte in comments\n',
            },
            {
                'order': 3,
                'title': 'Instruction encoding',
                'content': (
                    'Instruction encoding is the process of describing an instruction in byte form. The opcode is the core of the instruction, and the rest of the bytes may include prefixes, register selectors, or immediate operands. '
                    'Reading these bytes carefully reveals how the CPU interprets a command. '
                    'A small change in one byte can change the instruction entirely, so encoding is precise and unforgiving. '
                    'This is why low level programmers inspect hex dumps and opcode tables directly.'
                ),
                'challenge': 'Decode the hex bytes 48 83 C0 05 manually in comments. Identify the opcode, the operand size prefix, and the immediate value.',
                'starter_code': '; 48 83 C0 05\n; 48 = REX prefix (64-bit operand)\n; 83 = ?\n; C0 = ?\n; 05 = ?\n',
            },
            {
                'order': 4,
                'title': 'Reading a hex dump',
                'content': (
                    'A hex dump is a compact view of machine instructions and data. Each byte is shown in hexadecimal, and the programmer must infer which bytes belong to which instruction. '
                    'This is a practical skill because the CPU sees bytes, not readable code. '
                    'A simple program can be reconstructed by decoding each instruction one byte at a time. '
                    'The process teaches how software and hardware agree on instruction format.'
                ),
                'challenge': 'The hex dump below is a simple exit program. Label each byte in comments — which bytes are the opcode, which are operands.',
                'starter_code': '; B8 3C 00 00 00   <- mov eax, 60\n; BF 00 00 00 00   <- mov edi, 0\n; 0F 05            <- syscall\n; Label each byte:\n',
            },
            {
                'order': 5,
                'title': 'Opcodes',
                'content': (
                    'An opcode is the part of the instruction that tells the CPU which operation to perform. The remaining bytes carry arguments such as registers or constants. '
                    'Different instruction families use different opcode patterns, and the processor uses those patterns to decide how to decode the rest of the bytes. '
                    'This is why opcode knowledge is central to machine language. '
                    'Even a small error in the bytes can change the meaning of the instruction or make it invalid.'
                ),
                'challenge': 'Given opcode 0F 05, identify what instruction this is and when the CPU uses it. Write your answer as comments.',
                'starter_code': '; Opcode: 0F 05\n; Instruction: ?\n; Used when: ?\n; In Assembly this is written as: ?\n',
            },
            {
                'order': 6,
                'title': 'Fetch-decode-execute',
                'content': (
                    'The fetch-decode-execute cycle is the basic loop of the CPU. The processor fetches the next instruction from memory, decodes it to determine its meaning, and then executes it. '
                    'A single instruction may move data, change flags, or alter the instruction pointer. '
                    'This cycle repeats constantly while the machine is running. '
                    'Understanding it makes the relationship between code, machine instructions, and hardware much clearer.'
                ),
                'challenge': 'Trace through the fetch-decode-execute cycle for the instruction MOV rax, 60 step by step in comments. What does the CPU fetch, what does it decode, what does it execute.',
                'starter_code': '; Instruction: MOV rax, 60\n; Hex: 48 B8 3C 00 00 00 00 00 00 00\n;\n; FETCH: ?\n; DECODE: ?\n; EXECUTE: ?\n',
            },
        ]

        for item in machine_lessons:
            Lesson.objects.update_or_create(
                language=machine_language,
                order=item['order'],
                defaults={
                    'title': item['title'],
                    'content': item['content'],
                    'challenge': item['challenge'],
                    'starter_code': item['starter_code'],
                },
            )

        self.stdout.write(self.style.SUCCESS('Seeded all lesson content with starter code and coding challenges.'))
