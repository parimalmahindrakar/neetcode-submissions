class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp_size = len(temperatures)
        response_list = [0] * temp_size

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                response_list[idx] = index - idx
            stack.append(index)
        
        return response_list
  