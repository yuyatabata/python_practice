"""
# 標準入力取得
## 文字列
 =  sys.stdin.readline().rstrip() # 標準入力
 =  list(sys.stdin.readline().rstrip()) #１文字ずつリスト化
 
## 数値
 =  int(sys.stdin.readline())
 =  map(int, sys.stdin.readline().split()) #別の変数へ入力
 =  list(map(int, sys.stdin.readline().split()))
 =  [list(map(int,list(sys.stdin.readline().split()))) for i in range(N)] #複数行読み込み
"""
