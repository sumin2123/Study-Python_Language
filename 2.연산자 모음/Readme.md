# 기본 연산자 
--------------------------------------------------------

## 1. 산술 연산자 (Arithmetic Operators):
 a = 10, b = 20, c =3 이라 가정.

* 더하기  ( + )   a + b = 30 
* 빼기   ( - )   a - b = -10  
* 곱하기 ( * )   a * b = 200  
* 나누기 ( / )   b / a = 2.0  
* 나머지 ( % )   b % a = 0  
* 제곱  ( ** )   a ** c = 1000  
* 몫    ( // )   a // c = 3
--------------------------------------------------------

## 2. 비교 연산자 (Comparison Operators):
 a = 10, b = 20 이라 가정.
 
 * ( == )  \
   (a == b) → false
 * ( != )  \
   (a != b) →  true
 * ( > )   \
   (a > b) →  false
 * ( < )   \
   (a < b) →  true
 * ( >= )  \
   (a >= b) →  false  - 왼쪽 값이 오른쪽 값보다 크거나 동일하다.
 * ( <= )  \ 
   (a <= b) →  true   - 왼쪽 값이 오른쪽 값보다 작거나 동일하다.

--------------------------------------------------------

## 3. 할당 연산자(Assignment Operators):
 a = 10, b = 20 이라 가정.
 
 * =	 \
  왼쪽 변수에 / 오른쪽 값을 할당한다 c = a + b → c = a + b
 * +=	 \
  왼쪽 변수에 / 오른쪽 값을 (더하고) 결과를 왼쪽변수에 할당	c += a → c = c + a
 * -=	 \
  왼쪽 변수에서 / 오른쪽 값을 (빼고) 결과를 왼쪽변수에 할당	c -= a → c = c - a
 * *=	\
  왼쪽 변수에 / 오른쪽 값을 (곱하고) 결과를 왼쪽변수에 할당	c *= a → c = c * a
 * /=	\
  왼쪽 변수에서 / 오른쪽 값을 (나누고) 결과를 왼쪽변수에 할당	c /= a → c = c / a
 * %=	\
  왼쪽 변수에서 / 오른쪽 값을 나눈 (나머지의 결과)를 왼쪽변수에 할당	c %= a → c = c % a
 * **=	\
  왼쪽 변수에 / 오른쪽 값만큼 (제곱)을 하고 결과를 왼쪽변수에 할당	c **= a → c = c ** a
 * //=	\
  왼쪽 변수에서 / 오른쪽 값을 (나눈 몫의 결과)를 왼쪽변수에 할당	c //= a → c = c // a

--------------------------------------------------------

## 4. 비트 연산자 (Bitwise Operators):
a = 60, b = 13 이라 가정.
a = 0011 1100
b = 0000 1101

* ( & )	= AND 연산. 둘다 참일때만 만족	 / (a & b) = 12 → 0000 1100
* ( | )	= OR 연산. 둘 중 하나만 참이여도 만족 /	(a | b) = 61 → 0011 1101
* ( ^ ) = XOR 연산. 둘 중 하나만 참일 때 만족 / (a ^ b) = 49 → 0011 0001
* ( ~ ) = 보수 연산 /	(~a) = -61 → 1100 0011
* ( << ) = 왼쪽 시프트 연산자. 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동 / a << 2 = 240 → 1111 0000
* ( >> ) = 오른쪽 시프트 연산자. 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동 / a >> 2 = 15 → 0000 1111

--------------------------------------------------------

## 논리 연산자 (Logical Operators):
a = True, b = False 이라 가정.

* ( and ) 
 =	논리 AND 연산. 둘다 참일때만 참	/ (a and b) = False
* ( or ) 
  = 논리 OR 연산. 둘 중 하나만 참이여도 참  / (a or b) = True
* ( not ) 
 = 논리 NOT 연산. 논리 상태를 반전  /  not(a and b) = True

--------------------------------------------------------

## 맴버 연산자 (Membership Operators):
a = 10, b = 10, list = [1, 2, 3, 4, 5] 라 가정.

*  ( in ) 
  = list 내에 포함되어 있으면 참  / (a in list) = False
*  ( not in ) 
  = 	list 내에 포함되어 있지 않으면 참  / (b not in list) = True

--------------------------------------------------------

## 식별 연산자 (Identity Operators):
두 개체의 메모리 위치를 비교.
a = 20, b = 20 이라 가정.

*  ( is ) 
   = 개체메모리 위치나 값이 같다면 참  / (a is b) = True
*  ( is not )
   = 개체메모리 위치나 값이 같지 않다면 참  / (a is not b) = False

--------------------------------------------------------

## 연산자 우선순위 (Operators Precedence):
가장 높은 우선 순위에서 가장 낮은 모든 연산자.

*  **   \
 =>	지수 (전원으로 인상)
*  ~  +  -  \
 => Complement, 단항 플러스와 마이너스 (마지막 두의 메서드 이름은 + @이며, - @)
*  ( *  /  %  // ) \
 => 	곱하기, 나누기, 나머지, 몫
*  ( +  - ) \ 
 => 덧셈과 뺄셈
* ( >>  <<  ) \  
  => 좌우 비트 시프트
*  &	  \
  => 비트 'AND' 
* ^ |   \
  => 비트 전용 'OR'와 정기적 인 'OR'
*  <=   <  >  >=  \
  => 비교 연산자
*  <>  ==  !=   \
  => 평등 연산자
*  =  %=  /=  //=  -=  +=  *=  **=   \
 => 할당 연산자
*  is  is not  \
 =>	식별 연산자
*  in  not in  \
 => 	맴버 연산자
*  not or and  \
 =>	논리 연산자
