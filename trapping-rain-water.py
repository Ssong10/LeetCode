class Solution:
    def trap(self, height: List[int]) -> int:
        heights = [0] * (max(height)+1)
        if not height:
            return 0
        tmp = height[0]
        result = 0
        for i in range(len(height)):
            h = height[i]
            if tmp < h:
                x, y =0 , 0
                for hi in range(tmp+1,h+2):
                    if x < heights[hi]:
                        x = heights[hi]
                        y = hi
                print(i,i-x,y-tmp)
                result += (i-x)*(y-tmp)
            heights[h] = i+1
            tmp = h
        return result