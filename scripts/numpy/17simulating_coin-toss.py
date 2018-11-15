# https://scipython.com/book/chapter-6-numpy/examples/simulating-coin-tosses/

import numpy as np

res= ['H', 'T']
tosses= ''.join([res[i] for i in np.random.randint(2, size= 100)])
print(tosses)

head_seq = [len(s) for s in tosses.split('T') if s]
tail_seq = [len(s) for s in tosses.split('H') if s]
max_streak_len = max(max(head_seq), max(tail_seq))
head_seq_counts = [head_seq.count(i) for i in range(1,max_streak_len+1)]
tail_seq_counts = [tail_seq.count(i) for i in range(1,max_streak_len+1)]
max_streak_count = max(max(head_seq_counts), max(tail_seq_counts))
print(tosses)
print('{t:^{flen}} | i | {h:^{flen}}'.format(t='TAILS', h='HEADS',
                                           flen=max_streak_count))
print('-'*(max_streak_count*2+7))
for i in range(max_streak_len,0,-1):
    print('{tstreak:>{flen}s} |{i:^3d}| {hstreak:<{flen}s}'.format(
        tstreak='*'*tail_seq_counts[i-1], hstreak='*'*head_seq_counts[i-1],
        flen=max_streak_count, i=i))
