import sys
from heapq import heappush, heappop

# Main function
def main():
    # Read input from stdin
    input = sys.stdin.readline

    # Number of attributes
    n = int(input())

    # Attribute weights
    ai = list(map(int, input().split()))

    # Number of documents
    d = int(input())

    # Document features
    fi = [list(map(int, input().split())) for _ in range(d)]

    # Calculate initial relevance scores
    relevance = [sum(f*a for f, a in zip(doc, ai)) for doc in fi]

    # Create a max heap of (negative relevance, index) pairs
    # Negative relevance is used to simulate a max heap
    heap = [(-r, i+1) for i, r in enumerate(relevance)]
    heap.sort()  # Convert to max heap

    # Number of queries
    q = int(input())

    # Process each query
    for _ in range(q):
        query = list(map(int, input().split()))

        # Query type 1: Get top k documents
        if query[0] == 1:
            k = query[1]
            if k >= d:
                result = [idx for _, idx in heap]
            else:
                result = [idx for _, idx in heap[:k]]
            print(' '.join(map(str, result)))

        # Query type 2: Update document feature
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

# Run the main function
if __name__ == "__main__":
    main()
