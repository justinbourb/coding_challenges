def solution(A, K):
	n = len(A)
	search = range(n-1)
	for i in search:
		# check current num +1 < next num
		current = A[i] + 1
		next = A[i + 1]
		if (current < next):
			return False
		first = (A[0] == 1)
		last = (A[n-1] == K)
		both = (first and last )
	if not both:
		return False
	else:
		return True

print(solution([1,2,3], 2))