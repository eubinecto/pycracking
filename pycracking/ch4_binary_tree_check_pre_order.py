"""
LG AI Language Lab 코딩 테스트 - 풀지 못했던 문제 (두번째).
cracking the coding interview에 나온 문제는 아닌데... pre-order와 관련된 문제라, 여기에 추가해본다.
"""
import unittest
from typing import List

NULL = -1


def main(numbers: List[int]) -> bool:
    """
    check if the tree given in a list of integers
    is a valid binary tree by traversing in pre-order.
    """
    # (1) an empty tree
    if len(numbers) == 1 and numbers[0] == NULL:
        return True

    for i, n in enumerate(numbers):
        if n == NULL:
            if numbers[i - 1] != NULL:
                # (2) the left one  (n, -1)
                continue
            if i >= 2 and numbers[i - 2] != NULL \
                      and numbers[i - 1] == NULL:
                # (3) the right one (n, -1, -1)
                continue
            if i >= 4 and numbers[i - 4] != NULL \
                      and numbers[i - 3] != NULL \
                      and numbers[i - 2] == NULL \
                      and numbers[i - 1] == NULL:
                # (4) the right one, but that of the parent  (n, n, -1, -1, -1)
                continue
            if i >= 5 and numbers[i - 5] != NULL \
                      and numbers[i - 4] == NULL \
                      and numbers[i - 3] != NULL \
                      and numbers[i - 2] == NULL \
                      and numbers[i - 1] == NULL:
                # (5) the right one, but that of the parent of the parent  (n, -1, n, -1, -1, -1)
                continue
            # if none of the above, this tree is False
            return False
    return True


if __name__ == '__main__':
    # here are the test cases
    testcase = unittest.TestCase()
    # positive cases
    testcase.assertTrue(main([-1]))
    testcase.assertTrue(main([1, 2, -1, -1, -1]))
    testcase.assertTrue(main([1, 2, -1, 3, -1, -1, -1]))
    # negative cases
    testcase.assertFalse(main([-1, -1]))
    testcase.assertFalse(main([1, 2, -1, -1, -1, -1]))
    testcase.assertFalse(main([1, 2, -1, -1, 3, -1, -1, -1]))

"""
## 회고
### 왜 그때 당시에 풀지 못했나?
방금처럼 n == NULL일 때 어떤 패턴이 있는지를 case by case로 살펴보지 않았다. n == NULL과 같은 key condition 밑에 존재하는 
패턴을 분석하지 않았다. 바로 어 이건 스택이 필요하겠네? 하면서 데이터구조부터 생각했던 것이 화근이었다. 문제를 풀기 위해선 문제 자체에 집중하자.
### 액션 플랜
1. 데이터구조를 끼워맞추려고 하지말고 문제부터 먼저 이해한다.
2. 정 안되겠으면 brute force를 위한 패턴을 파악하라. 위 내 풀이처럼
"""
