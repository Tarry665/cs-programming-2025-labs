
def add_m():
    try:
        n = int(input("Введите размер матрицы: "))
        
        if n <= 2:
            print("Error!")
            return
        
        print("Введите первую матрицу:")
        m1 = [list(map(int, input().split())) for _ in range(n)]
        
        print("Введите вторую матрицу:")
        m2 = [list(map(int, input().split())) for _ in range(n)]
        
        print("Результат:")
        for i in range(n):
            print(' '.join(str(m1[i][j] + m2[i][j]) for j in range(n)))
            
    except:
        print("Error!")
add_m()