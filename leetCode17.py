



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
      
        number_to_letters = {
          "2":"abc",
          "3":"def",
          "4":"ghi",
          "5":"jkl",
          "6":"mno",
          "7":"pqrs",
          "8":"tuv",
          "9":"wxyz"}
        

        output = []
        queue = deque([(0,"")])
        length = len(digits)
        

        while queue:
            index,string = queue.popleft()
            if index == length:
                output.append(string)
                continue
            for l in number_to_letters[digits[index]]:
                queue.append([index+1,string+l])
        return output
