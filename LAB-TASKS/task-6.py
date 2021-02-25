Pz = [['chicken fajita Pizza', 700],['mayoneese pizza', 650],['grilled Pizza', 650],['hawaiian pizaa',700],['simple Chicken Pizza',850]]
Bg = [['Zinger Burger', 230],[' crispy Zinger  Burger', 260],['chicken Burger', 250],['fish burger', 320],['cowbo burger', 400],['meat burger', 350],['fish cheese burger', 380],['shami burger', 120]]

opts = []
loop = 1
for lo in range (0,10000):
    if loop != 0:
        print('\nMenu\n')
        print('Select what do you want\n\n1.Burger Menu\n\n2.Pizza Menu\n\n3.Total Bill\n')
        print('select 1 or 2 : ')
        optn = input()
        
        if optn == '3':
            cnt = -1
            tot = []
            for k in opts:
                cnt += 1
                print(f'{opts[cnt][0]} - price {opts[cnt][1]} {opts[cnt][2]}x [total: {opts[cnt][1] * opts[cnt][2]}]')
                tot.append(int(opts[cnt][1]) * int(opts[cnt][2]))
            print(f'total bill: {sum(tot)}')
            with open('bill.txt', 'w+') as l:
                l.write(str(sum(tot)))
                l.close()


        if optn == '2':
            cnt = 0
            number = []
            for itm in Pz:
                cnt += 1
                number.append(cnt)
                print(f'{cnt}. {itm[0]} - price {itm[1]}')
            optn2 = input('Plz select your Pizza (No.): ')
            qnty = input('Enter the number of quantity (No.): ')
            opts.append([Pz[int(optn2) - 1][0], Pz[int(optn2) - 1][1], int(qnty)])


        if optn == '1':
            cnt = 0
            number = []
            for itm in Bg:
                cnt += 1
                number.append(cnt)
                print(f'{cnt}. {itm[0]} - price {itm[1]}')
            optn2 = input('Plz select your burger (No.): ')
            qnty = input('Enter the number of quantity (No.): ')
            opts.append([Bg[int(optn2) - 1][0], Bg[int(optn2) - 1][1], int(qnty)])

        agn = input("Do you want the bill [yes/no] ")
        if agn == "no":
            loop = 0
