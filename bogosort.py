from random import randint

def shuffle(lst):
    old_lst = list(lst)
    new_lst = []
    while lst:
        rand_idx = randint(0, len(lst)-1)
        new_lst.append(lst.pop(rand_idx))
    return new_lst

def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def bogoSort(lst):
    i = 0
    print(f'{i}th iteration: {lst}')
    while not isSorted(lst):
        lst = shuffle(lst)
        i += 1
        print(f'{i}th iteration: {lst}')

if __name__=='__main__':
    lst = [5, 1, 3, 2, 4]
    bogoSort(lst)
