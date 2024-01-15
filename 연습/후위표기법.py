def to_postfix(expression: str) -> str: # 중위표기법을 후위 표기법으로 변환 
  op : dict[str, int] = {'+': 1, '-': 1, '*': 2, '/': 2}
  res : str = ""
  s = []

  for exp in expression:
    if exp.isnumeric(): # 숫자면 문자열에 추가
      res += exp
    elif exp in op: # 연산자이면
      while s and (op[exp] <= op[s[-1]]): #  빈 스택이 아니고, top의 우선순위가 높으면
        res += s.pop() # 문자열에 top 추가
      s.append(exp) # 현재 연산자를 리스트에 추가
      
  while s: # 스택을 비우자
    res += s.pop()
  return res

for expr in ("3 + 5 * 2", "3 * 5 + 2"):
  print(f"{expr} -> {to_postfix(expr)}")
