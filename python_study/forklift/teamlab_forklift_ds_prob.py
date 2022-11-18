# 모듈 import 파트
from datetime import datetime

# Test를 위한 Mock Function 파트


# Class 파트
class ForkliftNode(object):
    pass
     
class LinkedListBag():
    def __init__(self, first_node : Node = None) -> None:
        self._head = first_node  
        self._tail = first_node 
        if first_node is not None:
            self._size = 1
        else:
            self._size = 0
        
    def append(self, new_node : Node) -> None:
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1

    def insert(self, index_number : int, new_node : Node) -> bool:
        list_index = 0
        cur_node = self._head
        if index_number == 0:
            self._head = new_node
            new_node.next = cur_node
            self._size += 1
            return True

        while cur_node is not None:
            if list_index == index_number:
                pred_node.next = new_node
                new_node.next = cur_node
                self._size += 1
                return True
            list_index += 1
            pred_node = cur_node 
            cur_node = cur_node.next
        return False

    def remove(self, target_value : int) -> bool:
        cur_node = self._head
        pred_node = cur_node 
        while cur_node is not None:
            if cur_node.data == target_value:
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            pred_node = cur_node 
            cur_node = cur_node.next
        return False        

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)

class _BagIterator():
    def __init__(self, head_node : Node) -> None:
        self._cur_node = head_node
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node

# 실행 함수 파트

def load_dataset(filename : str):
    """ 데이터 셋을 입력 받으면 각 지게차 별로 데이터를 이차원 list로 변환하여 반환한다.
    
    Args:
        filename (str) : 지게차의 움직인 데이터를 포함한 파일명

    Returns:
        dataset (dict) : 지게차 이름을 key 값으로, 각 지게차별 정보를 이차원 list로 정리한 값
                         이차원 리스트 값은 아래와 같은 순서로 정돈된다.
                         [emp_x, emp_y, dt_in]
    
    Example:
    >>> import teamlab_forklift_ds as ds
    >>> filename = "forklist_move.csv"
    >>> ds.load_dataset(filename)
        {'TEAM10054239': 
         [['173753.462668852',
           '252318.443103598',
           '2019-06-01 08:30:50.651'],
          ['173725.558119309',
           '252342.150967047',
           '2019-06-01 08:30:50.619'],
          [### 나머지 출력부분은 생략됨]]
        }
    >>> result.keys()
    dict_keys(['TEAM10054239', 'TEAM1007B9625', 'TEAM10083967'])
    >>> len(result.keys())
    3
    """
    dataset = None
    return dataset

def sort_dataset(dataset : dict):
    """생성된 dataset을 넣었을 때 각 지게차별로 시간을 기준으로 sorting하여 값을 반환한다.

    Args:
        dataset (dict) : load_dataset 으로 생성된 dataset dict 파일

    Returns:
        sorted_dataset (dict) : 각 지게차별로 시간 순으로 정렬된 dataset dict 파일
    
    Example:
    >>> import teamlab_forklift_ds as ds
    >>> filename = "forklist_move.csv"
    >>> dataset = ds.load_dataset(filename)
    >>> sorted_result = ds.sort_dataset(dataset)
    >>> print(sorted_result)
        {'TEAM10054239': [['172978.787361283',
                           '252229.400114715',
                           '2019-06-01 08:30:48.797'],
                          ['172997.753770613',
                           '252211.490703829',
                           '2019-06-01 08:30:48.832'],
                          ['173021.175135472',
                           '252193.887723743',
                           '2019-06-01 08:30:48.860'],
                          ['173031.106644024',
                           '252176.916908881',
                           '2019-06-01 08:30:48.896'],
                          [### 나머지 출력부분은 생략됨]]
    """
    sorted_dataset = None
    return sorted_dataset

def build_linkedlistbag(sorted_dataset : dict):
    """이미 sorting된 dataset을 넣었을 때 각 지게차별로 LinkedListBag을 생성하여 반환한다.

    Args:
        dataset (dict) : load_dataset 으로 생성된 dataset dict 파일
                         만일 입력된 데이터셋이 sorting  되지 않았다면, sorting 하여 준다.                       

    Returns:
        linkedlistbag_dict (dict) : 각 지게차별로 생성된 LinkedListBag을 반환한다.
    
    Example:
    >>> sorted_result = ds.sort_dataset(result)
    >>> result = ds.build_linkedlistbag(sorted_result)
    >>> result.keys()
    dict_keys(['TEAM10054239', 'TEAM1007B9625', 'TEAM10083967'])
    >>> for node in result['TEAM10054239']:
            print(node)
        Forklift name : TEAM10054239
        x coordination : 172978.787361283
        y coordination : 252229.400114715
        Timestamp  : 2019-06-01 08:30:48.797000
        Forklift name : TEAM10054239
        x coordination : 172997.753770613
        y coordination : 252211.490703829
        Timestamp  : 2019-06-01 08:30:48.832000
        -------------------------- 생략 --------------
    """

    linkedlist_bag_dict = {}
    return linkedlist_bag_dict

def main():
    DATASET_FILENAME = ""
    dataset = load_dataset()

if __name__ == "__main__":
    main()
