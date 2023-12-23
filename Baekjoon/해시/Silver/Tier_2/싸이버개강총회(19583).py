import sys
from datetime import datetime

party_start, party_end, streaming_end = sys.stdin.readline().split()

enter_set = set()
out_set = set()

p_start = datetime.strptime(party_start, "%H:%M")
p_end = datetime.strptime(party_end, "%H:%M")
s_end = datetime.strptime(streaming_end, "%H:%M")

while True:
    Str = sys.stdin.readline().rstrip()
    if Str == '':
        break
    enterTime, nickname = Str.split()

    enter = datetime.strptime(enterTime, "%H:%M")

    if enter <= p_start:
        enter_set.add(nickname)
    if p_end <= enter and enter <= s_end:
        out_set.add(nickname)

print(len((enter_set & out_set)))
