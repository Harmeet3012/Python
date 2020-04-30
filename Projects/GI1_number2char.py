lt20 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',
        'fifteen','sixteen','seventeen','eighteen','nineteen']

mul10 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']

def two(num):
    if num<20:
        print(lt20[num%20],end=' ')
    else:
        if num%10==0:
            print(mul10[int(num/10)-2],end=' ')
        else:
            print(mul10[int(num/10) - 2],lt20[num%10],end=' ')

def three(num):
    if num%100==0:
        print(lt20[int(num / 100)],'Hundred')
    else:
        print(lt20[int(num/100)],'Hundred',end=' ')
        two(num%100)

def four(num):
    if num%1000==0:
        print(lt20[int(num/1000)],'Thousand',end=' ')
    else:
        print(lt20[int(num / 1000)],'Thousand',end=' ')
        if num%1000<100:
            two(num%1000)
        else:
            three(num%1000)

def fivesix(num):
    dig=int(num/1000)
    if dig<100:
        two(dig)
    else:
        three(dig)
    if num%1000==0:
        print('Thousand')
    elif num%1000<99:
        print('Thousand', end=' ')
        two(num%1000)
    else:
        print('Thousand', end=' ')
        three(num%1000)

def million(num):
    dig=int(num/1000000)
    if dig<100:
        two(dig)
    else:
        three(dig)
    if num%1000000==0:
        print("Million")
    elif num%1000000<100:
        print('Million',end=' ')
        two(num%1000000)
    elif num%1000000>=100 and num%1000000<1000:
        print('Million', end=' ')
        three(num%1000000)
    elif num%1000000>=1000 and num%1000000<10000:
        print('Million', end=' ')
        four(num%1000000)
    else:
        print('Million', end=' ')
        fivesix(num%1000000)
