```c
// startWith:  使用strncmp 前n个字符相同，相同返回0
static inline bool strstarts(const char *str, const char *prefix)
{
	return strncmp(str, prefix, strlen(prefix)) == 0;
}
```

