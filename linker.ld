ENTRY(reset)

SECTIONS
{
    . = 0x10000; /* Linux kernel starting address */

    .startup . :
    {
        startup.o(.text)
    }

    .text : 
    {
        *(.text)
    }

    .data : 
    { 
        *(.data) 
    }

    .bss : 
    { 
        *(.bss COMMON) 
    }
	
    . = ALIGN(8);
    . = . + 0x10000; /* 64K stack size */
    
	topOfStack = .;
}