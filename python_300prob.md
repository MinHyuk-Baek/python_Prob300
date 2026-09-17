## 126번 
```
a = input("address num:")
num = int(a[2])

if num in (0,1,2):
    print(a[2])
    print("gangbuk")

elif num in (3,4,5):
    print("dobong")
    print(a[2])
else :
    print("nowon")
    print(a[2])
```
<br>

- a의 index를 뽑아내서 직접 비교하고자 
if n[2] == 0 or n[2] == 1 or n[2] == 2 
와 같은 조건을 내세웠음.

-  a[2] 자체를 int화 해서 더 간단하고 짧게 나타낼 수 있음을 알게 되었다.
 
---

## 180번

```
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in range(5): 
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)
```
<br>
- list(volatility)를 사용할 생각이었는데, int가 반복자로 사용될 수 없는 오류가 발생하게 되어서
애초에 빈 리스트로 지정해 준다음, append를 사용해 요소들을 삽입해주었음.

---
## 194번

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = [[],[],[]]

for i in data :
	for j in i :
		a = j +  j * 0.00014
		result.append(a) 
print(result)

<br>
  
  - 이 코드의 결과로는 수수료가 곱해진 값들이 1차원 배열로 정렬되어 나타나게 되었고, 여기서 더 나아가야 했던 점은 3 x 4 배열로 다시 쪼개서 할당해주어야 했던 점이었다.

 - 이를 해결하기 위해 근본적으로 print(i) 와 print(j)를 추가해 주어 각 값이 어떤 값을 나타내고 반복이 어떻게 돌아가는지 다시한번 확인해 보았고, 그 결과 i는 data 리스트 속의 한개의 리스트를, j는 i가 갖고온 리스트 속에서의 요소 하나씩의 값을 불러오고 있는 것을 확인할 수 있었다.

 - 그렇다면, 3개씩 끊어서 다시 배열에 넣기만 하면 해결되는 문제임을 알아차릴 수 있고, 이를 구현하기 위해 sub = [] 이라는 서브의 빈 list를 하나 생성해 주어  i 가 반복되고 있는 구문 속에 넣어주어 i가 다음 리스트를 지칭할 때 다음 리스트로 생성되게끔 해주면 된다는 것을 알 수 있었다. 또한, 이렇게 생성된 sub list를 result에 대입해 주고자 append를 사용한 구문을 한 개 더 추가해 주었으며 그 결과는 다음과 같았다.

```
result = []
for i in data :
	sub = []
	for j in i :
		a = j + j * 0.00014
		sub.append(a)
	result.append(sub)
print(result)
```

