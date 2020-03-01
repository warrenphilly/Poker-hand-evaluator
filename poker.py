def evaluate(hand):
    rank = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K',
            14: 'A', }
    suit = {0: 'c', 1: 'd', 2: 'h', 3: 's'}


    myCheckRank = checkRank(hand,rank)
    myCheckSuit = checkSuit(hand,suit)
    total = count(myCheckRank,myCheckSuit)

    if total == 'full house':
        return 'Full house'
    elif total == '3':
        return 'Three of  kind'
    elif total == '4':
        return 'Four of a kind'
    elif total == '2':
        return 'Pair'
    elif total == 'flush':
        return 'Flush'

    else:
        num1 = 0
        num2 = 0


        increment = 0
        holder = 0
        length = len(rank)
        for i in (hand):
            holder = 2
            while holder < length:
                if hand[increment] == rank[holder]:
                   num1 = hand[increment]
                   holder = length
                else:
                    holder += 1
            increment += 1
            if num1 == 'T':
                num1 = int(10)
            if num1 == 'J':
                num1 = int(11)
            if num1 == 'Q':
                num1 = int(12)
            if num1 == 'K':
                num1 = int(13)
            if num1 == 'A':
                num1 = int(14)
            if int(num2) <= int(num1):
                num2 = int(num1)
        return rank[num2]

def count(myCheckRank,mycheckSuit):
    tally = 2
    full = 0
    house = 0
    answer = ''
    suit = mycheckSuit
    if suit == 5:
        answer ='flush'
    else:
        for i in range(13):
            if myCheckRank[tally] == 3:
                full = 3
            if myCheckRank[tally] == 4:
                answer = '4'
            if myCheckRank[tally] == 2:

                house = 2
            if full == 3 and house == 2:
                answer ='full house'
            elif myCheckRank[tally] == 3 and myCheckRank[tally] != 2:
                answer = '3'
            elif myCheckRank[tally] == 2 and myCheckRank[tally] != 3:
                answer =  '2'

            tally += 1
    return answer

def checkRank(hand,rank):
    check = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0,
            14: 0, }
    count = 0
    holder = 0
    length = len(rank)
    for i in (hand):
      holder = 2
      while holder < length:
          if hand[count] == rank[holder]:
              check[holder]+=1
              holder = length
          else:
              holder+=1
      count += 1
    return check

def checkSuit(hand,suit):
    check = {0: 0, 1: 0, 2: 0, 3: 0 }
    count = 0
    tally =0
    length = len(suit)
    for i in (hand):
      holder = 0
      while holder < length:
          if hand[count] == suit[holder]:
              check[holder]+=1
              holder = length
          else:
              holder+=1

      count += 1

    for i in range(4):
        if check[tally] == 5:
            return 5
        tally += 1





myHand = input('Please enter a your hand ')
print(evaluate(myHand))

