def num_to_indian_sys(n_s):
    n_s = str(n_s)
    if len(n_s.split('.')) == 1:
        s = n_s
    else:
        s,d = n_s.split('.')
    if len(s)<3:
        print(s)
    if len(s)>3:
        r = ''.join(s[-3:])
        for x in range(-3,-len(s),-2):
        
            r = s[x-2:x] + ","+r
    if len(n_s.split('.')) == 1:
        f = r
    else:
        f = r+ '.'+d
        
    return f
