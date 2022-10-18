import random
import sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = [random.choice(cards), random.choice(cards)]
me = [random.choice(cards), random.choice(cards)]

me_sum = 0
dealer_sum = 0


def dealer_sum_cal(dealer, dealer_sum):
    sum = 0
    for i in dealer:
        dealer_sum += i


def me_sum_cal(me, me_sum):
    for i in me:
        me_sum += i


def deal(me, dealer):
    me.append(random.choice(cards))
    print(f"You: {me}")
    sum = 0
    for a in me:
        sum += a
    if sum > 21:
        print("Bust: Dealer wins")
        print(f"dealer: {dealer}")
        print(f"You: {me}")
        sys.exit()


def stand(me, dealer):
    sum1 = 0
    sum2 = 0
    for a in dealer:
        sum1 += a
    for b in me:
        sum2 += b
    if 11 in dealer and sum1 > 21:
        dealer.remove(11)
        dealer.append(1)
    if 11 in me and sum2 > 21:
        me.remove(11)
        me.append(1)

    if sum1 > 21:
        print("Bust: You win")
        print(f"dealer: {dealer}")
        print(f"You: {me}")
    elif sum1 > sum2:
        print("Dealer wins")
        print(f"dealer: {dealer}")
        print(f"You: {me}")
    elif sum1 < 17:
        dealer.append(random.choice(cards))
        stand(me, dealer)
    elif sum1 < sum2:
        print("You win")
        print(f"dealer: {dealer}")
        print(f"You: {me}")
    else:
        print("Draw")
        print(f"dealer: {dealer}")
        print(f"You: {me}")

    sys.exit()

dealer_sum_cal(dealer, dealer_sum)
me_sum_cal(me, me_sum)

print(f"dealer : {dealer[0]}")
print(f"you : {me}")


def fun(me, dealer):
    a = input("Enter 'y' for deal or 'n' for stand ")
    if a == 'y':
        deal(me, dealer)
        fun(me, dealer)
    elif a == 'n':
        stand(me, dealer)
        fun(me, dealer)
    else:
        print("invalid input try again")
        fun(me, dealer)


fun(me, dealer)