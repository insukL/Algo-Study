# 문제

안드로메다 유치원 익스프레스반에서는 다음 주에 율동공원으로 소풍을 갑니다. 원석 선생님은 소풍 때 학생들을 두 명씩 짝을 지어 행동하게 하려고 합니다. 그런데 서로 친구가 아닌 학생들끼리 짝을 지어 주면 서로 싸우거나 같이 돌아다니지 않기 때문에, 항상 서로 친구인 학생들끼리만 짝을 지어 줘야 합니다.

각 학생들의 쌍에 대해 이들이 서로 친구인지 여부가 주어질 때, 학생들을 짝지어줄 수 있는 방법의 수를 계산하는 프로그램을 작성하세요. 짝이 되는 학생들이 일부만 다르더라도 다른 방법이라고 봅니다. 예를 들어 다음 두 가지 방법은 서로 다른 방법입니다.

- (태연,제시카) (써니,티파니) (효연,유리)
- (태연,제시카) (써니,유리) (효연,티파니)
  

# 입력  

- 첫 줄에는 테스트 케이스의 수 C (C <= 50)
- 각 테스트 케이스의 첫 줄에는 학생의 수 n (2 <= n <= 10) 과 친구 쌍의 수 m (0 <= m <= n*(n-1)/2)
- 이후 m 개의 정수 쌍으로 서로 친구인 두 학생의 번호
- 번호는 모두 0 부터 n-1 사이의 정수이고, 같은 쌍은 입력에 두 번 주어지지 않는다.
  

# 출력  

- 각 테스트 케이스마다 한 줄에 모든 학생을 친구끼리만 짝지어줄 수 있는 방법의 수

# 풀이  
순서쌍을 2차원 배열에 기록하고 각 원소를 선택하는 방식으로 완전 탐색
  

# 풀면서 생각해야 하는 부분  

중복이 발생하기 때문에 같은 답 중에 순서가 정해지도록 해야 한다.  
그래서 풀이는 아직 짝이 정해지지 않은 학생 중 가장 순서가 빠른 학생을 탐색하여 답의 순서가 사전 순서가 되도록 한다.