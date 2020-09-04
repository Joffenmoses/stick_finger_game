
hand = [0, 1, 1, 1, 1]
flag = True
count = 0
p1_c = p2_c = 'True'
print(hand[1], hand[2])
print(hand[3], hand[4])

def p1_own(s_h, t_h):
    global p1_oc
    if s_h in (1, 2) and t_h in (1, 2):
        transfer = int(input('how much to transfer'))
        hand[t_h] += transfer
        hand[s_h] -= transfer
        p1_oc = 'True'
    return p1_oc

def p2_own(s_h, t_h):
    global p2_oc
    if s_h in (3, 4) and t_h in (3, 4):
        transfer = int(input('how much to transfer'))
        hand[t_h] += transfer
        hand[s_h] -= transfer
        p2_oc = 'True'
    return p2_oc

while flag:
    count += 1
    p1_oc = p2_oc = 'None'
    if count % 2 != 0:
        print('1st Players turn')
    else:
        print('2nd Players turn')
    select_hand = int(input('select your hand'))
    transfer_hand = int(input('which hand you want to transfer'))
    p1_own(select_hand, transfer_hand)
    p2_own(select_hand, transfer_hand)
    if p1_oc != p1_c and p2_oc != p2_c:
        hand[transfer_hand] += hand[select_hand]
    if hand[transfer_hand] > 4:
        hand[transfer_hand] -= 5
    print(hand[1], hand[2])
    print(hand[3], hand[4])
    if hand[1] == 0 and hand[2] == 0:
        print('Player 2 Wins!!')
        flag = False
    if hand[3] == 0 and hand[4] == 0:
        print('Player 1 Wins!!')
        flag = False
