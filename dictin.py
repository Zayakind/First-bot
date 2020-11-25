def form_messege(a):
    b = ''
    for k in a.keys():
        b += str(k) + ' : ' + a[k] + '\n'
    return (b)