class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Negative ya 0 values ko positive (>= 1) banane ke liye shift karte hain
        min_val = min(nums)
        arr = [x - min_val + 1 for x in nums]
        max_val = max(arr)

        # Rolling hash ke liye base aur mod
        base = max_val + 100
        mod = 1_000_000_007

        power = [1] * (n + 1)
        prefix = [0] * (n + 1)

        for i in range(n):
            power[i + 1] = (power[i] * base) % mod
            prefix[i + 1] = (prefix[i] * base + arr[i]) % mod

        def get_subarray_hash(start: int, length: int) -> int:
            end = start + length
            return (prefix[end] - prefix[start] * power[length]) % mod

        def has_unique_subarray(length: int) -> bool:
            count = {}
            for i in range(n - length + 1):
                h = get_subarray_hash(i, length)
                count[h] = count.get(h, 0) + 1

            for freq in count.values():
                if freq == 1:
                    return True

            return False

        low, high = 1, n
        answer = n

        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
        