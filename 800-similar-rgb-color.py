class Solution:
    def similarRGB(self, color: str) -> str:
        nums = ['#']

        for i in [1, 3, 5]:
            x = int(color[i:i + 2], 16)

            q, r = divmod(x, 17)
            if r > 8:
                q += 1

            num = 17 * q
            nums.append(f'{num:02x}')

        return ''.join(nums)
