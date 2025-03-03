haystack = "hello"
needle = "ll"
a = 0
t = -1
for i in haystack:
    for j in haystack[a:len(needle)+a]:
        print(haystack[a:len(needle)+a])
        if needle==haystack[a:len(needle)+a]:
            # print(haystack[a:len(needle)+a])
            t=a
            # print(t)
        a+=1
