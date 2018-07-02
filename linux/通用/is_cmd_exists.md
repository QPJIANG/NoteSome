```
command -v foo >/dev/null 2>&1 || { echo >&2 "not exists.  Aborting.";}

type foo >/dev/null 2>&1 || { echo >&2 "not exists.  Aborting.";  }

hash foo 2>/dev/null || { echo >&2 "not exists.  Aborting.";  }


gnudate() {
    if hash gdate 2>/dev/null; then
        gdate "$@"
    else
        date "$@"
    fi
}

```

