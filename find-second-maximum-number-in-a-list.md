# find-second-maximum-number-in-a-list HackerRank Question
```
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(set(arr))

    # Get the second-to-last element (second-largest number)
    
    print(sorted_arr[-2])
    ```
