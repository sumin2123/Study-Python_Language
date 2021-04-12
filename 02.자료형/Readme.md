
## 리스트 

#### 리스트 기본 구조
##### [값, 값, 값]

![리스트 이미지](https://user-images.githubusercontent.com/77951853/114337102-7162ec80-9b8b-11eb-9edd-ca8c9302b2b0.png)

![리스트 기본 구조](https://user-images.githubusercontent.com/77951853/114341192-25687580-9b94-11eb-8c07-93d105f50303.png)

--------------------------------------------------
####  값 추가하기 
.append() → 메소드(특정기능을 수행하는 함수) \
리스트의 뒤에 추가할값을 붙여준다

![리스트에 값 추가하기](https://user-images.githubusercontent.com/77951853/114341337-7f693b00-9b94-11eb-868a-1536fcb5444c.png)

#### 리스트.append(추가할_값) 

![값 추가하기](https://user-images.githubusercontent.com/77951853/114341801-8775aa80-9b95-11eb-8b32-36ca760c8675.png)

--------------------------------------------------
####  값에 접근하기
앞에서부터 차례로 0부터 시작해서 주소가 주어진다./
그 값을 가져오거나, 지우거나, 바꿀 수 있다.

![값에 접근하기](https://user-images.githubusercontent.com/77951853/114342774-6b730880-9b97-11eb-8517-5dc4279b084d.png)

#### 리스트[접근할 _ 인덱스]

![값에 접근해 변경하기](https://user-images.githubusercontent.com/77951853/114342851-9fe6c480-9b97-11eb-870d-22a10177fac2.png)


--------------------------------------------------
####  값을 제거하기
del 이라는 키워드를 이용해서 제거를 해준다. \
주의) 하트2를 제거할 시 클로버3은 앞으로 땡겨져 2번 인덱스에서 1번인덱스로 변경된다.

![값을 제거하기](https://user-images.githubusercontent.com/77951853/114343302-8e51ec80-9b98-11eb-8a98-8674ee8d8bfd.png)

#### del.리스트[제거할 _ 인덱스]

![값을 제거하고 출력](https://user-images.githubusercontent.com/77951853/114343311-9447cd80-9b98-11eb-924f-b233f9e22bfe.png)


--------------------------------------------------
## Q. '콜라맛','포도맛'사탕을 candies에 추가하고, '박하맛' 사탕을 제거하세요.
```python
candy0 = '딸기맛'
candy1 = '레몬맛'
candy2 = '수박맛'
candy3 = '박하맛'
candy4 = '우유맛'
candy5 = '땅콩맛'

print(candy0) #딸기맛
print(candy1) #레몬맛
print(candy2) #수박맛
print(candy3) #박하맛
print(candy4) #우유맛
print(candy5) #땅콩맛

candies = [candy0, candy1,candy2,candy3,candy4,candy5]
print(candies)

candies.append('콜라맛')
candies.append('포도맛')
print(candies)

del candies[3]
print(candies)

```

![박하맛 정답](https://user-images.githubusercontent.com/77951853/114344507-ebe73880-9b9a-11eb-89f8-5afe1ae556a5.png)










