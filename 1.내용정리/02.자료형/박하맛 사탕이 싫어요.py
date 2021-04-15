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
