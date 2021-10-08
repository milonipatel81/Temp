def check(data):
    ret=''
    for i in data:
        if i in "aeiouAEIOU":
            ret=ret+i
    return ret
