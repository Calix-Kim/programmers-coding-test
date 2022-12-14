def solution(n):
    # My solution
    return sum([x for x in range(1, n+1) if n%x==0])

    # Better solution (n/2보다 큰 수는 검사할 필요없음) -> 사실 sqrt(n)까지만 검사해도 가능
    # return n + sum([x for x in range(1, n//2+1) if n%x==0])