n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
primary_sum = [matrix[r][r] for r in range(n)]
secondary_sum = [matrix[r][n- r - 1] for r in range(n)]

print(abs(sum(primary_sum) - sum(secondary_sum)))

#for i in range(n):
#   primary_sum += matrix[i][i]
#   secondary_sum += matrix[i][n - i - 1]
