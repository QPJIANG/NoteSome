https://en.wikipedia.org/wiki/CPUID#EAX=0:_Highest_Function_Parameter_and_Manufacturer_ID



```
#include <stdio.h>

int main()
{
  int a, b;

  for (a = 0; a < 5; a++)
  {
    __asm__("cpuid"
            :"=a"(b)                 // EAX into b (output)
            :"0"(a)                  // a into EAX (input)
            :"%ebx","%ecx","%edx");  // clobbered registers

    printf("The code %i gives %i\n", a, b);
  }

  return 0;
}
```

