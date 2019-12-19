```



PS1='$(if [[ $? == 0 ]]; then echo "\[\e[32m\]:)"; else echo "\[\e[31m\]:("; fi)\[\e[0m\]  \[\e[0;36m\]\d \t \[\e[1;34m\]  \[\033[01;33;1m\]\u\[\033[00;32;1m\]@\[\033[01;36;1m\]\h\[\033[00;32;1m\]:\[\033[00;34;1m\]\w \[\033[01;32;1m\]$(git branch 2>/dev/null | sed -n "s/* \(.*\)/\1 /p")\$ \[\033[01;37;1m\]'

reset="\[\e[0m\]"

# Magic Bash Prompt Version 1.0.1
next_hue()
{
    color=$((31 + (++color % 7)))   # set 31 to 30 for dark on light
    PS1="\[\e[1;${color}m\]\\$ $reset"  # set 1 to 0 for dark on light
    PS1='$(if [[ $? == 0 ]]; then echo "\[\e[32m\]:)"; else echo "\[\e[31m\]:("; fi)\[\e[0m\]  \[\e[0;36m\]\d \t \[\e[1;34m\] \[\033[01;33;1m\]\u\[\033[00;32;1m\]@\[\033[01;36;1m\]\h\[\033[00;32;1m\]:\[\033[00;34;1m\]\w \[\033[01;32;1m\]$(git branch 2>/dev/null | sed -n "s/* \(.*\)/\1 /p")  \[\e[1;${color}m\]\\$ $reset '

}

random_hue()
{
    color=$(($RANDOM % 7 + 31)) # set 31 to 30 for dark on light
    PS1="\[\e[1;${color}m\]\\$ $reset"  # set 1 to 0 for dark on light
    PS1='$(if [[ $? == 0 ]]; then echo "\[\e[32m\]:)"; else echo "\[\e[31m\]:("; fi)\[\e[0m\]  \[\e[0;36m\]\d \t \[\e[1;34m\] \[\033[01;33;1m\]\u\[\033[00;32;1m\]@\[\033[01;36;1m\]\h\[\033[00;32;1m\]:\[\033[00;34;1m\]\w \[\033[01;32;1m\]$(git branch 2>/dev/null | sed -n "s/* \(.*\)/\1 /p")\[\e[1;${color}m\]\\$ '
}
# 执行命令前执行一次，生成随机颜色。
PROMPT_COMMAND="random_hue"  
```

