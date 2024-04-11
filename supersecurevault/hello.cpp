  _BYTE *v1; // [rsp+8h] [rbp-18h]
  void *dest; // [rsp+10h] [rbp-10h]
  int i; // [rsp+1Ch] [rbp-4h]
  _UNKNOWN unk_201E

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
