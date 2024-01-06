class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        xor = xor_result ^ k  
        different_bits = 0
        while xor:
            different_bits += xor & 1  
            xor >>= 1  
        return different_bits
        
        