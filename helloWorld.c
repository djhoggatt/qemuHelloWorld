/// @file helloWorld.c
/// Super simple implementation of a "Hello World" program for hardware emulation.


//--------------------------------------------------------------------------------------------------
//  Macros and Error Checking
//--------------------------------------------------------------------------------------------------


#define ERR_NOERR 0
#define ERR_NULL  1

#define NULL 0


//--------------------------------------------------------------------------------------------------
//  Private Data Types
//--------------------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------------------
//  Private Function Prototypes
//--------------------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------------------
//  File Variables
//--------------------------------------------------------------------------------------------------


// See https://github.com/pebble/qemu/blob/master/hw/arm/versatilepb.c for peripheral locations and sizes

volatile char * const uart0Addr = (char *)0x101f1000; // const to prevent loading into RWX memory


//--------------------------------------------------------------------------------------------------
//  Private Functions
//--------------------------------------------------------------------------------------------------


/// @brief Prints the given string to UART port 0.
/// @param str String to print
///
static int print(char *str)
{
    if(str == NULL)
    {
	    return ERR_NULL;
    }

    int retVal = ERR_NOERR;

    while(*str != '\0')
    {
        *uart0Addr = *str;
        str++;
    }
	
    return retVal;
}


//--------------------------------------------------------------------------------------------------
//  Public Functions
//--------------------------------------------------------------------------------------------------


/// @brief Main entry point for the Hello World program.
///
void main(void)
{
    int err = print("Hello world!\n");

    while(!err)
    {
        // Do nothing
    }

    // Critical error, should not get here.
}


// EOF
