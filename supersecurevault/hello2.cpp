#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

void sub_11A9();

int main() {
  char s[72]; // BYREF
  char *v5; // BYREF

  std::cout << "Enter the password: ";
  std::fgets(s, 64, stdin);
  s[strcspn(s, "\n")] = 0;
  if (std::strcmp(s, "Sup3rS3cr3tP@ass") == 0)
    sub_11A9();
  else
    v5 = "Noob";
  std::puts(v5);
  return 0;
}

void sub_11A9() {
  char dest[27];
  const char* encrypted = "P|sf|<5Qmldxmszq}6p";
  for (int i = 0; i < 26; ++i)
    dest[i] = encrypted[i] ^ 0x6B;
  std::puts(dest);
}
