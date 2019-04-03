def solution(A, K):
   if len(A) == 0:
        return A
   K = K % len(A)
   return A[-K:] + A[:-K]
