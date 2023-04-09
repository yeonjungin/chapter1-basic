# 격자 : n * m
# 서로 겹치치 않는 두 직사각형을 적절하게 잡아, 두 직사각형 안에 적힌 숫자들의 총 합을 최대로 하는 프로그램 작성
# 경계는 닿아도 된다. 
# 직사각형 가로와 세로 길이가 같아선 안된다. 
# 직사각형 최대 크기 (가로 N, 세로 M)
# 1,2 / 1,3 / 1,4
# w <=m, h<=n
# 첫번쨰 직사각형을 만든다.
# 방문처리 
# 두번째 직사각형을 만든다. 
import sys
n,m=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
result=-sys.maxsize

def rec_sum(x1,y1,x2,y2):
    val=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            val+=array[i][j]
    return val

def overlap(x1,y1,x2,y2,ex1,ey1,ex2,ey2):
    clear_visited()
    draw(x1,y1,x2,y2)
    draw(ex1,ey1,ex2,ey2)
    if chekc2():
      if chekc2():
        retrun False
      retrun False
    if check():
      if check_melon():
        if check_melon2():
            return False
        return True
    return False

def draw(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            visited[i][j]+=1

def check():
    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                return True
    return False

def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j]=0

def make_rec(x1,y1,x2,y2):
    #move_num=[w1,h1,w2,h2] # w1,h1,w2,h2
    # 1번째 직사각형 합계
    val=rec_sum(x1,y1,x2,y2)

    # 2번째 직사각형 합계
    temp=-sys.maxsize
    for ex1 in range(n):
        for ey1 in range(m):
            for ex2 in range(ex1,n):
                for ey2 in range(ey1,m):
                    if not overlap(x1,y1,x2,y2,ex1,ey1,ex2,ey2):
                        # print("x1 : ", x1, " y1 : ", y1, " x2 : ", x2, " y2 : ", y2)
                        # print("ex1 : ",ex1, " ey1 : ",ey1, " ex2 : ",ex2," ey2 : ",ey2)
                        # print(rec_sum(ex1,ey1,ex2,ey2), " temp :", temp)
                        temp=max(temp,rec_sum(ex1,ey1,ex2,ey2))
                        
    if temp==-sys.maxsize:
        return -sys.maxsize
    val+=temp
    return val

# 1번쨰 직사각형
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1,n):
            for y2 in range(y1,m):
                result=max(result,make_rec(x1,y1,x2,y2))
print(result)