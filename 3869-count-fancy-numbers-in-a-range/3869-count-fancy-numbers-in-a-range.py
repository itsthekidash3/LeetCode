#borrowed code from sandeep to get an understanding on how to solve the problem

@cache
def check(sm):
    s = str(sm)
    if all(int(x) < int(y) for x, y in pairwise(s)):
        return 1
    if all(int(x) > int(y) for x, y in pairwise(s)):
        return 1
    return 0


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        num2 = str(r)
        num1 = str(l).zfill(len(num2))
        n = len(num2)
        MI = [num1, "0" * n]
        MX = [num2, "9" * n]

        @cache
        def dp(i, mi_=0, mx_=0, sm=0, dir=0, limit=-1):
            if i == n:
                return 1
            mi = MI[mi_]
            mx = MX[mx_]
            cur_min = int(mi[i])
            cur_max = int(mx[i])
            ans = 0
            for dig in range(cur_min, cur_max + 1):
                next_mi_ = mi_ != 0 or dig != cur_min
                next_mx_ = mx_ != 0 or dig != cur_max
                next_dir = dir
                next_limit = -1 if limit == -1 and dig == 0 else dig
                flag = True
                if limit !=-1 and next_limit !=-1:
                    if dir == 1 and dig <= limit:
                        flag = False
                    if dir == -1 and dig >= limit:
                        flag = False
                    if dir == 0:
                        if dig < limit:
                            next_dir = -1
                        elif dig > limit:
                            next_dir = 1
                        else:
                            flag = False
                if flag:
                    ans += dp(i + 1, next_mi_, next_mx_, sm + dig, next_dir, next_limit)
                else:
                    ans += dp2(i + 1, next_mi_, next_mx_, sm + dig)
            return ans

        @cache
        def dp2(i, mi_=0, mx_=0, sm=0):
            if i == n:
                return check(sm)
            mi = MI[mi_]
            mx = MX[mx_]
            cur_min = int(mi[i])
            cur_max = int(mx[i])
            ans = 0
            for dig in range(cur_min, cur_max + 1):
                next_mi_ = mi_ != 0 or dig != cur_min
                next_mx_ = mx_ != 0 or dig != cur_max
                ans += dp2(i + 1, next_mi_, next_mx_, sm + dig)
            return ans

        ans = dp(0)
        dp.cache_clear()
        dp2.cache_clear()
        return ans