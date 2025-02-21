S = int(input())

# left, right = 1, S
# ans = 0
# while left <= right:
#     mid = (left + right) // 2
#     sum = (mid * (mid + 1)) // 2
#
#     if sum <= S:
#         ans = mid
#         left = mid + 1
#     else:
#         right = mid - 1
#
# print(ans)

import math

print(int((-1 + math.sqrt(1 + 8 * S)) / 2))