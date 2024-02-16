from collections import deque

MAX_CAFFEINE = 300
stamats_coffeine = 0

mg_coffeine_stack = [int(x) for x in input().split(", ")]
nrg_drinks_deque = deque(int(x) for x in input().split(", "))

while mg_coffeine_stack and nrg_drinks_deque:
    last_mg_coff = mg_coffeine_stack.pop()
    first_nrg = nrg_drinks_deque.popleft()
    current_caffeine = last_mg_coff * first_nrg

    stamat_drank = MAX_CAFFEINE - stamats_coffeine

    if stamat_drank - current_caffeine >= 0:
        stamats_coffeine += current_caffeine
    else:
         nrg_drinks_deque.append(first_nrg)
         stamats_coffeine -= 30
         if stamats_coffeine < 0:
             stamats_coffeine = 0

if nrg_drinks_deque:
    print(f"Drinks left: {', '.join(str(x) for x in nrg_drinks_deque)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_coffeine} mg caffeine.")
