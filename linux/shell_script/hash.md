```
check_program_installed() {
    hash $1 > /dev/null 2>&1
    if [ "$?" != "0" ]; then
    print "command $1 not found. is it installed?."
    exit 1
    fi
}
```





```
if hash <cmd> 2>/dev/null; then
	echo "exists"
else
	echo "not exists"
fi

```

