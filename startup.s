.global reset

reset:
    ldr sp, =topOfStack  @ Initialize the stack
    bl main              @ Should not return
    b reset

