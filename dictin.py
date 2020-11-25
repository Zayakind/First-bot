def form_messege(a):
#a = {1:"no", 2:'yes', 3: "maibe"}
    b = ''
    for k in a.keys():
        b += str(k) + ' : ' + a[k] + '\n'

    return (b)