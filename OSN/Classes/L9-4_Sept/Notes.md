### Key Concepts of Memory Virtualization

Memory virtualization creates the illusion for each process that it has its own complete memory space while the OS manages the actual physical memory. This is similar to how e-commerce platforms make users feel they have access to unlimited products, though physical inventory is limited.

Every process has a virtual address space containing:

- Code segment (instructions)
- Heap segment (dynamic memory)
- Stack segment (function variables)
- Free space

The physical memory is limited and must be shared among processes. The Memory Management Unit (MMU) handles the translation between virtual addresses and physical addresses.

### Goals of Memory Virtualization

- **Transparency**: Processes believe they have complete memory access
- **Efficiency**: Fast address translation with minimal overhead
- **Protection**: Processes cannot access each other's memory spaces
- **Flexibility**: Support for varying memory requirements

### Base and Bounds Approach

The simplest memory management technique:

- Each process has a base register and a bounds register in the MMU
- Virtual address translation formula: physical_address = base + virtual_address
- System checks if result is within bounds
- Memory allocation is contiguous for each process
- Dynamic relocation occurs at runtime

Example:

- If base = 16KB and virtual address = 0, physical address = 16KB
- If bounds = 4KB and virtual address = 4400, this would cause an out-of-bounds error

### Limitations of Base and Bounds

- Entire process must be in one contiguous block
- Memory fragmentation issues
- Inefficient use of physical memory
- Not suitable for large address spaces

### Segmentation

Segmentation is a "generalized base and bounds" approach:

- Process divided into multiple segments (code, heap, stack)
- Each segment has its own base and bounds values
- MMU contains segment registers for each process
- More flexible as segments can have different sizes
- Physical memory divided into many segments of varying sizes

Address translation process:

1. Identify which segment the virtual address belongs to
2. Calculate offset within that segment
3. Add offset to segment's base address
4. Check if within segment bounds
5. If out of bounds, trigger segmentation fault

Example:

- Code segment: Base = 32KB, Size = 2KB
- Heap segment: Base = 34KB, Initial size = 2KB
- Stack segment: Base = 28KB, Size = 2KB
- For virtual address 100 in code segment: Physical address = 32KB + 100
- For virtual address 4200 in heap segment: Offset = 4200-4096 = 104, Physical address = 34KB + 104

### Action Items

- [ ]  Review the formula for RTT calculation: estimated RTT + 4 × deviation RTT
- [ ]  Understand the difference between flow control (sender-receiver) and congestion control (network level)
- [ ]  Practice address translation examples for both base-bounds and segmentation approaches

