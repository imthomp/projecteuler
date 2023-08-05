def euler55():
    def is_palindrome(num):
        return list(str(num)) == list(reversed(str(num)))
    
    def reverse_and_add(num):
        return int("".join(reversed(str(num)))) + num
    
    def is_lychrel(num):
        for i in range(50):
            num = reverse_and_add(num)
            if is_palindrome(num):
                return False
        return True
    
    # lychrels_under_10k = 0
    # for i in range(10000):
    #     if is_lychrel(i):
    #         lychrels_under_10k += 1
    # return lychrels_under_10k

    lychrels_under_10k = len([i for i in range(10000) if is_lychrel(i)])
    return lychrels_under_10k