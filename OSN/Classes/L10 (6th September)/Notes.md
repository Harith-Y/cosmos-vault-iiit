### Memory Virtualization Fundamentals

The operating system provides each process with the illusion of having access to infinite memory through a virtual address space (VA), while in reality there's only limited physical memory available. The goal of memory virtualization is to efficiently translate virtual addresses to physical addresses. Two main approaches were discussed: base and bounds (simpler) and segmentation (more advanced).

### Segmentation Approach

Segmentation divides a process's memory into logical segments (code, heap, stack), each mapped separately to physical memory. For address translation, the system:

1. Identifies which segment an address belongs to
2. Calculates the offset within that segment
3. Maps to the correct physical location

While segmentation offers more flexibility than base and bounds, it suffers from **external fragmentation** - as processes allocate and free memory, the physical memory becomes fragmented with unusable "holes" between segments. Free space management algorithms (best fit, first fit, etc.) can help but don't solve the fundamental issue.

### Paging Mechanism

Paging solves fragmentation issues by dividing both virtual and physical memory into fixed-size blocks:

- Virtual memory divided into pages
- Physical memory divided into page frames
- All pages/frames have identical size
- Pages map to frames without concern for logical segments

For a 64-byte virtual address space with 16-byte pages:

- 2 bits needed to identify page number (Virtual Page Number/VPN)
- 4 bits needed for offset within page
- Address translation simply maps VPN to Page Frame Number (PFN)

### Page Tables and Address Translation

Page tables store the mapping between virtual pages and physical frames:

- Each process has its own page table
- Page Table Base Register (PTBR) points to current process's page table
- Page tables are stored in physical memory

Each Page Table Entry (PTE) contains:

- Physical Frame Number (PFN)
- Valid bit (is this mapping valid?)
- Protection bits (read/write/execute permissions)
- Present bit (is page in physical memory or on disk?)
- Dirty bit (has page been modified?)
- Reference bit (has page been recently used?)

For a 32-bit address space with 4KB pages:

- 20 bits for page number (2^20 entries)
- 12 bits for offset
- Page table size: 4MB per process (2^20 * 4 bytes)

### Efficiency Considerations and TLB

The page table approach introduces performance concerns:

- Large memory overhead (e.g., 400MB for 100 processes)
- Each memory access requires multiple memory accesses (one to page table, one to actual data)

To improve efficiency, systems use a Translation Lookaside Buffer (TLB):

- Hardware cache inside the MMU for address translations
- Stores recently used VPN-to-PFN mappings
- Significantly reduces translation overhead

For larger processes that exceed physical memory, the OS can intelligently swap pages between memory and disk using the present, dirty, and reference bits to determine which pages to keep in memory.

