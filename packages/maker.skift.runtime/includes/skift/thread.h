#pragma once

#include <skift/generic.h>
#include <skift/syscalls.h>

DECL_SYSCALL0(sk_thread_self);
DECL_SYSCALL3(sk_thread_create, int entry, void *arg, int flags);
DECL_SYSCALL1(sk_thread_exit, void *exitval);
DECL_SYSCALL1(sk_thread_cancel, int thread);
DECL_SYSCALL1(sk_thread_sleep, int time);
DECL_SYSCALL1(sk_thread_wakeup, int thread);
DECL_SYSCALL1(sk_thread_wait, int thread);
DECL_SYSCALL1(sk_thread_waitproc, int process);