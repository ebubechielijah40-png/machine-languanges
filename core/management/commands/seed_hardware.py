from django.core.management.base import BaseCommand
from core.models import HardwareSystem, HardwareChallenge


class Command(BaseCommand):
    help = 'Seed hardware systems and challenges'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding hardware systems...')

        systems = [
            {
                'name': 'PERSONAL COMPUTER',
                'slug': 'pc',
                'description': 'The machine on your desk. A CPU, RAM, storage, and an OS mediating between you and the hardware. You will write the software that runs on it.',
                'category': 'classical',
                'unlock_order': 1,
                'challenges': [
                    {
                        'order': 1,
                        'title': 'Boot Sequence',
                        'description': 'The PC powers on. Before the OS loads, the BIOS/UEFI runs. Your task is to understand and simulate the first instructions the CPU executes.',
                        'instructions': 'Write a C program that simulates a boot sequence. Print each stage: POWER ON, BIOS CHECK, MEMORY TEST, LOADING OS. Use a function for each stage.',
                        'starter_code_c': '#include <stdio.h>\n\nvoid power_on() {\n    printf("POWER ON\\n");\n}\n\nint main() {\n    power_on();\n    // add remaining stages\n    return 0;\n}',
                        'starter_code_asm': '; Boot sequence simulation\nsection .data\n    msg1 db "POWER ON", 10\n    len1 equ $ - msg1\n\nsection .text\n    global _start\n\n_start:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg1\n    mov rdx, len1\n    syscall\n    ; add remaining stages\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 2,
                        'title': 'Memory Allocator',
                        'description': 'RAM is a flat array of bytes. The OS manages it. Your task is to simulate a simple memory allocator that tracks used and free blocks.',
                        'instructions': 'Write a C program that simulates memory allocation. Create an array of 256 bytes representing RAM. Write allocate() and free() functions that mark blocks as used or free. Print the memory state before and after each operation.',
                        'starter_code_c': '#include <stdio.h>\n\n#define MEM_SIZE 256\nunsigned char memory[MEM_SIZE];\n\nvoid allocate(int start, int size) {\n    // mark bytes as used (1)\n}\n\nvoid free_mem(int start, int size) {\n    // mark bytes as free (0)\n}\n\nvoid print_memory() {\n    // print memory state\n}\n\nint main() {\n    print_memory();\n    allocate(0, 64);\n    print_memory();\n    return 0;\n}',
                        'starter_code_asm': '; Memory simulation\nsection .bss\n    memory resb 256\n\nsection .text\n    global _start\n\n_start:\n    ; mark first 64 bytes as used\n    mov rcx, 64\n    mov rdi, memory\n    mov al, 1\n    rep stosb\n    ; exit\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 3,
                        'title': 'Process Scheduler',
                        'description': 'The OS runs multiple processes by switching between them rapidly. Simulate a round-robin scheduler.',
                        'instructions': 'Write a C program that simulates a round-robin process scheduler. Create a struct Process with fields: id, name, remaining_time. Create 3 processes with different remaining times. Simulate the scheduler running each process for 1 unit of time in a loop until all processes complete.',
                        'starter_code_c': '#include <stdio.h>\n\nstruct Process {\n    int id;\n    char name[20];\n    int remaining_time;\n};\n\nint main() {\n    struct Process processes[3] = {\n        {1, "PROC_A", 3},\n        {2, "PROC_B", 2},\n        {3, "PROC_C", 4}\n    };\n    // implement round-robin scheduler\n    return 0;\n}',
                        'starter_code_asm': '; Process scheduler simulation\nsection .data\n    proc_a db "PROC_A", 10\n    len_a equ $ - proc_a\n\nsection .text\n    global _start\n\n_start:\n    ; simulate 3 process cycles\n    mov rcx, 3\nloop:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, proc_a\n    mov rdx, len_a\n    syscall\n    dec rcx\n    jnz loop\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                ],
            },
            {
                'name': 'SERVER',
                'slug': 'server',
                'description': 'A machine that listens. It waits for requests and responds. No display, no keyboard. Just a process running, ports open, handling connections.',
                'category': 'classical',
                'unlock_order': 2,
                'challenges': [
                    {
                        'order': 1,
                        'title': 'Request Handler',
                        'description': 'A server receives a request and decides what to do with it. Simulate a basic request handler.',
                        'instructions': 'Write a C program that simulates a request handler. Define request types: GET, POST, DELETE. Write a function handle_request(type, path) that prints the appropriate response for each type.',
                        'starter_code_c': '#include <stdio.h>\n#include <string.h>\n\n#define GET 0\n#define POST 1\n#define DELETE 2\n\nvoid handle_request(int type, char *path) {\n    // handle each request type\n}\n\nint main() {\n    handle_request(GET, "/index");\n    handle_request(POST, "/data");\n    handle_request(DELETE, "/file");\n    return 0;\n}',
                        'starter_code_asm': '; Request handler simulation\nsection .data\n    get_msg db "GET REQUEST RECEIVED", 10\n    get_len equ $ - get_msg\n\nsection .text\n    global _start\n\n_start:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, get_msg\n    mov rdx, get_len\n    syscall\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 2,
                        'title': 'Connection Pool',
                        'description': 'Servers manage multiple simultaneous connections. Simulate a connection pool with a fixed capacity.',
                        'instructions': 'Write a C program simulating a connection pool of size 5. Write connect() and disconnect() functions. Track active connections. Print pool state after each operation. Reject connections when pool is full.',
                        'starter_code_c': '#include <stdio.h>\n\n#define POOL_SIZE 5\nint connections[POOL_SIZE];\n\nvoid connect(int id) {\n    // find empty slot and add connection\n}\n\nvoid disconnect(int id) {\n    // find and remove connection\n}\n\nvoid print_pool() {\n    // print all slots\n}\n\nint main() {\n    print_pool();\n    connect(101);\n    connect(102);\n    print_pool();\n    disconnect(101);\n    print_pool();\n    return 0;\n}',
                        'starter_code_asm': '; Connection pool\nsection .bss\n    pool resq 5\n\nsection .data\n    msg db "CONNECTING", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                ],
            },
            {
                'name': 'DATA CENTER',
                'slug': 'data-center',
                'description': 'Thousands of servers. Cooling systems. Redundant power. Your code runs across multiple machines simultaneously. Coordination is everything.',
                'category': 'classical',
                'unlock_order': 3,
                'challenges': [
                    {
                        'order': 1,
                        'title': 'Load Balancer',
                        'description': 'A load balancer distributes incoming requests across multiple servers to prevent any single machine from being overwhelmed.',
                        'instructions': 'Write a C program simulating a round-robin load balancer. Create 4 servers each with a request count. Write distribute_request() that sends each request to the next server in rotation. Run 12 requests and print which server handled each one.',
                        'starter_code_c': '#include <stdio.h>\n\n#define NUM_SERVERS 4\n\nstruct Server {\n    int id;\n    int request_count;\n};\n\nint current = 0;\n\nvoid distribute_request(struct Server servers[], int total) {\n    // round-robin distribution\n}\n\nint main() {\n    struct Server servers[NUM_SERVERS] = {{1,0},{2,0},{3,0},{4,0}};\n    for (int i = 0; i < 12; i++) {\n        distribute_request(servers, NUM_SERVERS);\n    }\n    return 0;\n}',
                        'starter_code_asm': '; Load balancer simulation\nsection .data\n    server1 db "SERVER 1", 10\n    len1 equ $ - server1\n\nsection .text\n    global _start\n\n_start:\n    mov rcx, 4\nroute:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, server1\n    mov rdx, len1\n    syscall\n    dec rcx\n    jnz route\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 2,
                        'title': 'Fault Detector',
                        'description': 'Data centers must detect and respond to server failures automatically.',
                        'instructions': 'Write a C program simulating fault detection. Create 5 servers each with a status (1=online, 0=failed) and a heartbeat counter. Write check_heartbeat() that decrements each counter and marks a server failed if it reaches 0. Simulate 5 cycles.',
                        'starter_code_c': '#include <stdio.h>\n\nstruct Server {\n    int id;\n    int status;\n    int heartbeat;\n};\n\nvoid check_heartbeat(struct Server servers[], int count) {\n    // decrement heartbeat, mark failed if 0\n}\n\nint main() {\n    struct Server servers[5] = {\n        {1, 1, 3},\n        {2, 1, 1},\n        {3, 1, 5},\n        {4, 1, 2},\n        {5, 1, 4}\n    };\n    for (int i = 0; i < 5; i++) {\n        printf("CYCLE %d\\n", i+1);\n        check_heartbeat(servers, 5);\n    }\n    return 0;\n}',
                        'starter_code_asm': '; Fault detection\nsection .data\n    msg db "HEARTBEAT CHECK", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rcx, 5\ncheck:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    dec rcx\n    jnz check\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                ],
            },
            {
                'name': 'SUPERCOMPUTER',
                'slug': 'supercomputer',
                'description': 'Millions of cores working in parallel. Problems that would take a PC years are solved in hours. You write code that splits work across processors.',
                'category': 'classical',
                'unlock_order': 4,
                'challenges': [
                    {
                        'order': 1,
                        'title': 'Parallel Sum',
                        'description': 'Supercomputers split large datasets across cores and combine results. Simulate parallel computation.',
                        'instructions': 'Write a C program that simulates parallel computation. Create an array of 1000 integers. Split it into 4 equal chunks. Write compute_chunk(array, start, end) that sums a chunk. Simulate 4 parallel workers each computing their chunk sum. Combine results and print total.',
                        'starter_code_c': '#include <stdio.h>\n\n#define SIZE 1000\n#define WORKERS 4\n\nint data[SIZE];\n\nlong compute_chunk(int arr[], int start, int end) {\n    long sum = 0;\n    // sum from start to end\n    return sum;\n}\n\nint main() {\n    for (int i = 0; i < SIZE; i++) data[i] = i + 1;\n    int chunk = SIZE / WORKERS;\n    long results[WORKERS];\n    // simulate 4 workers\n    long total = 0;\n    // combine results\n    printf("TOTAL: %ld\\n", total);\n    return 0;\n}',
                        'starter_code_asm': '; Parallel sum simulation\nsection .data\n    msg db "COMPUTING CHUNK", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rcx, 4\nworker:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    dec rcx\n    jnz worker\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 2,
                        'title': 'Matrix Multiply',
                        'description': 'Matrix multiplication is a core operation in scientific computing. Supercomputers do this across thousands of nodes.',
                        'instructions': 'Write a C program that multiplies two 4x4 matrices. Implement matrix_multiply(A, B, C) where C = A * B. Print the resulting matrix.',
                        'starter_code_c': '#include <stdio.h>\n\n#define N 4\n\nvoid matrix_multiply(int A[N][N], int B[N][N], int C[N][N]) {\n    // implement multiplication\n}\n\nvoid print_matrix(int M[N][N]) {\n    // print matrix\n}\n\nint main() {\n    int A[N][N] = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};\n    int B[N][N] = {{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1}};\n    int C[N][N] = {0};\n    matrix_multiply(A, B, C);\n    print_matrix(C);\n    return 0;\n}',
                        'starter_code_asm': '; Matrix multiply placeholder\nsection .data\n    msg db "MATRIX OPERATION", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                ],
            },
            {
                'name': 'SATELLITE',
                'slug': 'satellite',
                'description': 'A machine in orbit. No repair. No restart. Software must be fault-tolerant, power-efficient, and precise. Every byte costs fuel.',
                'category': 'classical',
                'unlock_order': 5,
                'challenges': [
                    {
                        'order': 1,
                        'title': 'Telemetry System',
                        'description': 'Satellites constantly transmit status data back to ground control.',
                        'instructions': 'Write a C program simulating a satellite telemetry system. Create a struct Telemetry with fields: altitude (float), velocity (float), battery (int), temperature (float), signal_strength (int). Write transmit() that prints all values in a formatted packet. Simulate 5 transmissions with slight value changes each cycle.',
                        'starter_code_c': '#include <stdio.h>\n\nstruct Telemetry {\n    float altitude;\n    float velocity;\n    int battery;\n    float temperature;\n    int signal_strength;\n};\n\nvoid transmit(struct Telemetry *t, int cycle) {\n    printf("--- PACKET %d ---\\n", cycle);\n    // print all fields\n}\n\nint main() {\n    struct Telemetry sat = {408.5, 7.66, 100, -10.5, 95};\n    for (int i = 1; i <= 5; i++) {\n        transmit(&sat, i);\n        sat.battery -= 2;\n        sat.altitude += 0.1;\n    }\n    return 0;\n}',
                        'starter_code_asm': '; Telemetry transmission\nsection .data\n    msg db "TRANSMITTING PACKET", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rcx, 5\ntransmit:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    dec rcx\n    jnz transmit\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 2,
                        'title': 'Error Correction',
                        'description': 'Radiation in space flips bits. Satellites use error correction to detect and fix corrupted data.',
                        'instructions': 'Write a C program simulating basic error detection using parity bits. Write add_parity(byte) that returns the byte with a parity bit added. Write check_parity(byte) that returns 1 if valid, 0 if corrupted. Simulate sending 5 bytes, corrupting one, and detecting the error.',
                        'starter_code_c': '#include <stdio.h>\n\nint add_parity(int byte) {\n    // count bits, add parity\n    return byte;\n}\n\nint check_parity(int byte) {\n    // verify parity\n    return 1;\n}\n\nint main() {\n    int data[] = {0b10110010, 0b11001100, 0b10101010, 0b11110000, 0b00001111};\n    // transmit with parity\n    // corrupt one byte\n    // check all bytes\n    return 0;\n}',
                        'starter_code_asm': '; Parity check\nsection .data\n    valid db "VALID", 10\n    vlen equ $ - valid\n    corrupt db "CORRUPTED", 10\n    clen equ $ - corrupt\n\nsection .text\n    global _start\n\n_start:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, valid\n    mov rdx, vlen\n    syscall\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                ],
            },
            {
                'name': 'QUANTUM SYSTEM',
                'slug': 'quantum',
                'description': 'Not classical. Qubits exist in superposition until measured. Entanglement links particles across distance. This is the frontier.',
                'category': 'quantum',
                'unlock_order': 6,
                'challenges': [
                    {
                        'order': 1,
                        'title': 'Superposition Simulator',
                        'description': 'A qubit is not 0 or 1. It is both until measured. Simulate this with probability.',
                        'instructions': 'Write a C program simulating qubit superposition. A qubit has a probability of being 0 and a probability of being 1 (must sum to 1.0). Write measure_qubit(prob_zero) that uses rand() to collapse the qubit to 0 or 1 based on probability. Run 100 measurements and print how many times you got 0 vs 1.',
                        'starter_code_c': '#include <stdio.h>\n#include <stdlib.h>\n#include <time.h>\n\nint measure_qubit(float prob_zero) {\n    float r = (float)rand() / RAND_MAX;\n    return r < prob_zero ? 0 : 1;\n}\n\nint main() {\n    srand(time(NULL));\n    float prob_zero = 0.7;\n    int zeros = 0, ones = 0;\n    for (int i = 0; i < 100; i++) {\n        int result = measure_qubit(prob_zero);\n        if (result == 0) zeros++;\n        else ones++;\n    }\n    printf("ZEROS: %d\\nONES: %d\\n", zeros, ones);\n    return 0;\n}',
                        'starter_code_asm': '; Quantum simulation placeholder\n; True quantum simulation requires floating point\n; This simulates the classical representation\nsection .data\n    msg db "QUBIT MEASURED", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                    {
                        'order': 2,
                        'title': 'Entanglement Model',
                        'description': 'Entangled qubits mirror each other instantly regardless of distance. Simulate entangled pairs.',
                        'instructions': 'Write a C program simulating quantum entanglement. Create two qubits that are entangled — when one is measured, the other instantly takes the opposite value. Simulate 10 measurements of the first qubit and print both qubits after each measurement.',
                        'starter_code_c': '#include <stdio.h>\n#include <stdlib.h>\n#include <time.h>\n\nstruct Qubit {\n    int value;  // -1 = unmeasured, 0 or 1 = measured\n    int entangled_with;  // index of entangled qubit\n};\n\nvoid measure(struct Qubit qubits[], int index) {\n    // measure qubit, collapse entangled partner\n}\n\nint main() {\n    srand(time(NULL));\n    struct Qubit qubits[2] = {{-1, 1}, {-1, 0}};\n    for (int i = 0; i < 10; i++) {\n        qubits[0].value = -1;\n        qubits[1].value = -1;\n        measure(qubits, 0);\n        printf("Q0: %d  Q1: %d\\n", qubits[0].value, qubits[1].value);\n    }\n    return 0;\n}',
                        'starter_code_asm': '; Entanglement simulation\nsection .data\n    msg db "ENTANGLED PAIR MEASURED", 10\n    len equ $ - msg\n\nsection .text\n    global _start\n\n_start:\n    mov rcx, 10\nmeasure:\n    mov rax, 1\n    mov rdi, 1\n    mov rsi, msg\n    mov rdx, len\n    syscall\n    dec rcx\n    jnz measure\n    mov rax, 60\n    xor rdi, rdi\n    syscall',
                    },
                ],
            },
        ]

        for system_data in systems:
            challenges_data = system_data.pop('challenges')
            system, created = HardwareSystem.objects.update_or_create(
                slug=system_data['slug'],
                defaults=system_data,
            )
            self.stdout.write(f"{'Created' if created else 'Updated'}: {system.name}")

            for challenge_data in challenges_data:
                HardwareChallenge.objects.update_or_create(
                    system=system,
                    order=challenge_data['order'],
                    defaults=challenge_data,
                )
                self.stdout.write(f"  Challenge: {challenge_data['title']}")

        self.stdout.write(self.style.SUCCESS('Hardware systems seeded successfully.'))
