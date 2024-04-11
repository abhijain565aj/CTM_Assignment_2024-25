/* This file was generated by the Hex-Rays decompiler version 8.3.0.230608.
   Copyright (c) 2007-2021 Hex-Rays <info@hex-rays.com>

   Detected compiler: GNU C++
*/

#include <defs.h>


//-------------------------------------------------------------------------
// Function declarations

__int64 (**init_proc())(void);
void sub_1020();
// void free(void *ptr);
// int puts(const char *s);
// size_t strcspn(const char *s, const char *reject);
// char *fgets(char *s, int n, FILE *stream);
// int strcmp(const char *s1, const char *s2);
// void *memcpy(void *dest, const void *src, size_t n);
// void *malloc(size_t size);
// void __noreturn exit(int status);
// int __fastcall _cxa_finalize(void *);
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void));
FILE **sub_10F0();
__int64 sub_1120();
FILE **sub_1160();
__int64 sub_11A0();
const char *sub_11A9();
void term_proc();
// int __fastcall _libc_start_main(int (__fastcall *main)(int, char **, char **), int argc, char **ubp_av, void (*init)(void), void (*fini)(void), void (*rtld_fini)(void), void *stack_end);
// int __fastcall __cxa_finalize(void *);
// __int64 _gmon_start__(void); weak

//-------------------------------------------------------------------------
// Data declarations

_UNKNOWN main;
_UNKNOWN unk_201E; // weak
void *off_4048 = &off_4048; // idb
FILE *stdin; // idb
char byte_4058; // weak


//----- (0000000000001000) ----------------------------------------------------
__int64 (**init_proc())(void)
{
  __int64 (**result)(void); // rax

  result = &_gmon_start__;
  if ( &_gmon_start__ )
    return (__int64 (**)(void))_gmon_start__();
  return result;
}
// 40B8: using guessed type __int64 _gmon_start__(void);

//----- (0000000000001020) ----------------------------------------------------
void sub_1020()
{
  JUMPOUT(0LL);
}
// 1026: control flows out of bounds to 0

//----- (00000000000010C0) ----------------------------------------------------
// positive sp value has been detected, the output may be wrong!
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void))
{
  __int64 v3; // rax
  int v4; // esi
  __int64 v5; // [rsp-8h] [rbp-8h] BYREF
  char *retaddr; // [rsp+0h] [rbp+0h] BYREF

  v4 = v5;
  v5 = v3;
  _libc_start_main((int (__fastcall *)(int, char **, char **))main, v4, &retaddr, 0LL, 0LL, a3, &v5);
  __halt();
}
// 10C6: positive sp value 8 has been found
// 10CD: variable 'v3' is possibly undefined

//----- (00000000000010F0) ----------------------------------------------------
FILE **sub_10F0()
{
  return &stdin;
}

//----- (0000000000001120) ----------------------------------------------------
__int64 sub_1120()
{
  return 0LL;
}

//----- (0000000000001160) ----------------------------------------------------
FILE **sub_1160()
{
  FILE **result; // rax

  if ( !byte_4058 )
  {
    if ( &__cxa_finalize )
      _cxa_finalize(off_4048);
    result = sub_10F0();
    byte_4058 = 1;
  }
  return result;
}
// 4058: using guessed type char byte_4058;

//----- (00000000000011A0) ----------------------------------------------------
// attributes: thunk
__int64 sub_11A0()
{
  return sub_1120();
}

//----- (00000000000011A9) ----------------------------------------------------
const char *sub_11A9()
{
  _BYTE *v1; // [rsp+8h] [rbp-18h]
  void *dest; // [rsp+10h] [rbp-10h]
  int i; // [rsp+1Ch] [rbp-4h]

  dest = malloc(0x1BuLL);
  if ( !dest )
  {
    puts("Memory allocation failed.");
    exit(1);
  }
  v1 = malloc(0x1BuLL);
  memcpy(dest, &unk_201E, 0x1BuLL);
  for ( i = 0; i <= 26; ++i )
    v1[i] = *((_BYTE *)dest + i) ^ 0x6B;
  return "tomper!";
}

//----- (000000000000124A) ----------------------------------------------------
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  char s[72]; // [rsp+0h] [rbp-50h] BYREF
  char *v5; // [rsp+48h] [rbp-8h]

  puts("Enter the password");
  fgets(s, 64, stdin);
  s[strcspn(s, "\n")] = 0;
  if ( !strcmp(s, "Sup3rS3cr3tP@ass") )
    v5 = (char *)sub_11A9();
  else
    v5 = "Noob";
  puts(v5);
  free(v5);
  return 0LL;
}
// 124A: using guessed type char s[72];

//----- (00000000000012E8) ----------------------------------------------------
void term_proc()
{
  ;
}

// nfuncs=30 queued=10 decompiled=10 lumina nreq=0 worse=0 better=0
// ALL OK, 10 function(s) have been successfully decompiled