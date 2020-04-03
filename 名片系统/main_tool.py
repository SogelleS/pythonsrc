card_list=[]

def puthelp():
    print('*'*50,'\n')
    print('1.新建名片\n2.显示全部\n3.查询名片\n0.退出\n')
    print('*'*50)
    return int(input('请选择>>'))

def addcard():
    '''新增名片'''

    print('-'*50)
    print('新增名片')
    temp = {'name': '','phone': '','QQ': '','Emile': ''}
    temp['name']=input('Enter name: ')

        #if temp['name']=='':
        #    break

    temp['phone'] = input('Enter phone: ')
    temp['QQ'] = input('Enter QQ: ')
    temp['Emile'] = input('Enter Emile: ')
    card_list.append(temp)
        #print(card_list)
        #print('Next please empty to quit')
        #if input('1 to add other to quit')!='1':
            #break



    print('-' * 50)

def showall():
    '''显示所有'''

    if len(card_list)==0:
        return
    print('-' * 50)
    print('显示所有名片')
    print('%s\t\t%s\t\t%s\t\t\t%s'%('name','phone','QQ','Emile'))
    print('-'*50)
    for card in card_list:

        print('%s\t\t'%card['name'],end='')
        print('%s\t\t'%card['phone'],end='')
        print('%s\t\t'%card['QQ'],end='')
        print('%s'%card['Emile'],end='')
        print()
    else:
        input('enter to quit')
    print('-' * 50)
    print('-' * 50)

def serchcard():
    '''搜索名片'''

    print('-' * 50)
    print('搜索名片')
    inter=input('enter name:')

    for find in card_list:
        if find['name']==inter:
            print('%s\t\t\t%s\t\t\t%s\t\t\t%s' % ('name', 'phone', 'QQ', 'Emile'))
            print('%s\t\t\t' % find['name'], end='')
            print('%s\t\t\t' % find['phone'], end='')
            print('%s\t\t\t' % find['QQ'], end='')
            print('%s' %find['Emile'])
            cho=input('enter you choice:(1修改2删除3返回):')
            if cho=='1':
                '''
                card_list.remove(find)
                temp = {'name': '', 'phone': '', 'QQ': '', 'Emile': ''}
                
                temp['name'] = input('Enter'' name: ')
                temp['phone'] = input('Enter phone: ')
                temp['QQ'] = input('Enter QQ: ')
                temp['Emile'] = input('Enter Emile: ')
                card_list.append(temp)
                '''
                find['name'] = change_card_val(find['name'], 'name')
                find['phone'] = change_card_val(find['phone'], 'phone')
                find['QQ'] = change_card_val(find['QQ'], 'QQ')
                find['Emile'] = change_card_val(find['Emile'], 'Emile')

            elif cho=='2':
                card_list.remove(find)
            elif cho=='3':
                return
            else:
                print('Error')
                return

    else:
        print('cant find')
        return
    print('-' * 50)


def change_card_val(dic_val,title):
    userin=input('enter:%s'%title)
    if userin=='':
        return dic_val
    else:
        return userin

