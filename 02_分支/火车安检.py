has_ticket=True
knifeLength=400

if has_ticket:
    print('well i will test you knife')
    if knifeLength>20:
        print('you knife has %.2f is to long'%(float(knifeLength)))
    else:
        print('good you can go')
else:
    print("you shit cant in")