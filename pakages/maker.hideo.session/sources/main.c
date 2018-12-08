#include <skift/generic.h>
#include <skift/process.h>
#include <skift/thread.h>

int program()
{
    int compositor = sk_process_exec("app/maker.hideo.compositor", NULL);
    int panel = sk_process_exec("app/maker.hideo.panel", NULL);

    sk_thread_waitproc(compositor);
    sk_thread_waitproc(panel);
    
    return 0;
}
