def subsets(numbers):
        if numbers == []:
            return [[]]
        x = subsets(numbers[1:])
        return x + [[numbers[0]] + y for y in x]

   def sized_subsets(set, element_number):
       return [x for x in subsets(set) if len(x) == element_number]
