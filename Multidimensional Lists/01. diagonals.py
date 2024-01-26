n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
primary_sum = [matrix[r][r] for r in range(n)]
secondary_sum = [matrix[r][n- r - 1] for r in range(n)]


print(f"Primary diagonal: {', '.join(str(x) for x in primary_sum)}. Sum: {sum(primary_sum)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_sum)}. Sum: {sum(secondary_sum)}")
