class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # The Counter class is used to count the frequency of each element in the nums list.
        #This line creates a dictionary-like object count where keys are elements from the nums list, 
        #and values are their corresponding frequencies.
        count = Counter(nums)
        


        # This line creates a list of tuples, where each tuple contains the negative frequency of an element and the element itself.
        #The negative frequency is used because Python's heapq module provides a min heap implementation, 
        #and we want to extract elements with higher frequencies first.
        heap = [(-freq, num) for num, freq in count.items()]
        

        #The heapify function from the heapq module rearranges the elements in the list heap to satisfy the heap property. 
        #After this operation, heap[0] will contain the smallest element.
        heapq.heapify(heap)
        

        #This line iteratively pops the smallest element from the min heap k times.
        #Each popped element is a tuple containing the negative frequency and the corresponding element.
        #We retrieve only the element ([1]) from each tuple and store it in the result list.
        result = [heapq.heappop(heap)[1] for _ in range(k)]

        return result
        '''

        hash={}
        for n in nums:
            if n in hash:
                hash[n]+=1
            else:
                hash[n]=hash.get(n,0)+1
        



        # Sort the dictionary items based on values in descending order
        sorted_items = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        


        top_k_items = sorted_items[:k]  # Extract the k highest key-value pairs
        top_k_keys = [item[0] for item in top_k_items]  # Extract keys from the key-value pairs

        return top_k_keys
        '''
