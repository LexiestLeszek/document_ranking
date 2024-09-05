import sys
from heapq import heappush, heappop

def main_func():
    input = sys.stdin.readline

    n = int(input())
    ai = list(map(int, input().split()))
    d = int(input())
    fi = [list(map(int, input().split())) for _ in range(d)]
    
    relevance = [sum(f*a for f, a in zip(doc, ai)) for doc in fi]
    
    # Create a max heap of (relevance, index) pairs
    heap = [(-r, i+1) for i, r in enumerate(relevance)]
    heap.sort()  # Convert to max heap

    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            k = query[1]
            if k >= d:
                result = [idx for _, idx in heap]
            else:
                result = [idx for _, idx in heap[:k]]
            print(' '.join(map(str, result)))
            
        elif query[0] == 2:
            i, j, v = query[1:]
            old_value = fi[i-1][j-1]
            fi[i-1][j-1] = v
            relevance[i-1] += (v - old_value) * ai[j-1]
            
            # Update the heap
            for idx, (r, doc_idx) in enumerate(heap):
                if doc_idx == i:
                    heap[idx] = (-relevance[i-1], doc_idx)
                    break
            heap.sort()  # Re-sort the heap

if __name__ == "__main__":
    main_func()
