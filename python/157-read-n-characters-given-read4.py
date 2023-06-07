class Solution:
    def read(self, buf, n):
        buf4 = [' '] * 4
        total = 0

        for _ in range(0, n, 4):
            cnt = read4(buf4)
            cnt = min(cnt, n - total)
            new_total = total + cnt
            buf[total: new_total] = buf4[:cnt]
            total = new_total
            if cnt < 4:
                break

        return total
