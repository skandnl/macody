class Stack:
    """
    최대 크기가 10인 스택 자료 구조를 구현합니다.
    """
    def __init__(self, max_size=10):
        self.items = []  # 스택 요소를 저장할 리스트
        self.max_size = max_size  # 스택의 최대 크기

    def push(self, item):
        """
        스택에 요소를 추가합니다 (최대 10개).
        """
        if len(self.items) < self.max_size:
            self.items.append(item)
            print(f"✅ PUSH: '{item}'이(가) 스택에 추가되었습니다.")
        else:
            print(f"⚠️ 경고: 스택이 가득 찼습니다. (최대 크기: {self.max_size}) '{item}'을(를) 추가할 수 없습니다.")

    def pop(self):
        """
        스택의 가장 마지막(Top) 요소를 제거하고 반환합니다.
        """
        if not self.empty():
            return self.items.pop()
        else:
            print("⚠️ 경고: 스택이 비어있습니다. 가져올 내용이 없습니다.")
            return None

    def peek(self):
        """
        스택의 가장 마지막(Top) 요소를 제거하지 않고 확인합니다.
        """
        if not self.empty():
            return self.items[-1]
        else:
            print("⚠️ 경고: 스택이 비어있습니다. 확인할 내용이 없습니다.")
            return None

    def empty(self):
        """
        스택이 비어있는지 (True) 확인합니다 (False).
        """
        return len(self.items) == 0

    def size(self):
        """
        현재 스택에 있는 요소의 개수를 반환합니다.
        """
        return len(self.items)

    def display(self):
        """
        현재 스택의 모든 요소를 표시합니다.
        """
        print(f"현재 스택 (크기: {self.size()}/{self.max_size}, TOP: {self.peek()}): {self.items}")

# 

---

## 💻 스택 동작 확인 예시

스택 구조가 **LIFO** 원칙에 따라 정상적으로 동작하는지 확인하기 위해 고유 번호가 포함된 내용을 사용해 보겠습니다.

### 1. 스택 초기화 및 `push()` 동작 확인

```python
# Stack 객체 생성 (최대 크기 10)
my_stack = Stack()

# 내용 입력 (PUSH)
print("### PUSH 동작 ###")
for i in range(1, 12):
    item = f"데이터-{i:02d}"  # 고유 번호 부여
    my_stack.push(item)
    if i < 11 and i % 3 == 0: # 중간에 스택 상태 확인
        my_stack.display() 

# 11번째 데이터는 최대 크기(10) 때문에 추가되지 않아야 함
my_stack.display()