pthread_spin_lock(3)						   Library Functions Manual						  pthread_spin_lock(3)

NAME
       pthread_spin_lock, pthread_spin_trylock, pthread_spin_unlock - lock and unlock a spin lock

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <pthread.h>

       int pthread_spin_lock(pthread_spinlock_t *lock);
       int pthread_spin_trylock(pthread_spinlock_t *lock);
       int pthread_spin_unlock(pthread_spinlock_t *lock);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       pthread_spin_lock(), pthread_spin_trylock():
	   _POSIX_C_SOURCE >= 200112L

DESCRIPTION
       The pthread_spin_lock() function locks the spin lock referred to by lock.  If the spin lock is currently unlocked, the calling thread acquires the lock
       immediately.   If  the spin lock is currently locked by another thread, the calling thread spins, testing the lock until it becomes available, at which
       point the calling thread acquires the lock.

       Calling pthread_spin_lock() on a lock that is already held by the caller or a lock that has not been initialized with pthread_spin_init(3)  results  in
       undefined behavior.

       The pthread_spin_trylock() function is like pthread_spin_lock(), except that if the spin lock referred to by lock is currently locked, then, instead of
       spinning, the call returns immediately with the error EBUSY.

       The pthread_spin_unlock() function unlocks the spin lock referred to lock.  If any threads are spinning on the lock, one of those threads will then ac‐
       quire the lock.

       Calling pthread_spin_unlock() on a lock that is not held by the caller results in undefined behavior.

RETURN VALUE
       On success, these functions return zero.	 On failure, they return an error number.

ERRORS
       pthread_spin_lock() may fail with the following errors:

       EDEADLOCK
	      The system detected a deadlock condition.

       pthread_spin_trylock() fails with the following errors:

       EBUSY  The spin lock is currently locked by another thread.

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.2.  POSIX.1-2001.

CAVEATS
       Applying any of the functions described on this page to an uninitialized spin lock results in undefined behavior.

       Carefully read NOTES in pthread_spin_init(3).

SEE ALSO
       pthread_spin_destroy(3), pthread_spin_init(3), pthreads(7)

Linux man-pages 6.7							  2023-10-31							  pthread_spin_lock(3)
