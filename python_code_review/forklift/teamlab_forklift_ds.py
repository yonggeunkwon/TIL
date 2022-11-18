# 모듈 import 파트
from dataclasses import dataclass
from datetime import datetime
from email.errors import StartBoundaryNotFoundDefect
from platform import node
from typing import Any
import csv

# Test를 위한 Mock Function 파트


# Class 파트
class Node:
    def __init__(self, data : Any = None, next : 'Node' = None) -> None:
        self._data = data
        self._next = None

class ForkliftNode(object):
    def __init__(self, forklift_name : str = None, location_x : float = None, location_y :float = None, iot_datetime : datetime = None) -> None:
        self._forklift_name = forklift_name
        self._location_x = location_x
        self._location_y = location_y
        self._iot_datetime = iot_datetime
        self.next = None
    
    @property
    def forklift_name(self):
        return self._forklift_name
    
    @property
    def location_x(self):
        return self._location_x

    @property
    def location_y(self):
        return self._location_y

    @property
    def iot_datetime(self):
        return self._iot_datetime

    @property
    def next(self):
        return self._next

    @forklift_name.setter
    def forklift_name(self, value : str) -> None:
        self._forklift_name = value

    @location_x.setter
    def location_x(self, value : float) -> None:
        self._location_x = value

    @location_y.setter
    def location_y(self, value : float) -> None:
        self._location_y = value

    @iot_datetime.setter
    def iot_datetime(self, value : datetime) -> None:
        self._iot_datetime = value

    @next.setter
    def next(self, value: 'ForkliftNode') -> None:
        self._next = value

    def __add__(self, other) -> None:
        self._next = other

    def __str__(self) -> str:
        return_str = f"Forklift name : {self.forklift_name}\n" f"x coordination : {self.location_x}\n" f"y coordination : {self.location_y}\n" f"Timestamp  : {self.iot_datetime}"
        return return_str

    def __repr__(self) -> str:
        return_str = f"Forklift name : {self.forklift_name}\n" f"x coordination : {self.location_x}\n" f"y coordination : {self.location_y}\n" f"Timestamp  : {self.iot_datetime}"
        return return_str
        

     
class LinkedListBag(object):
    def __init__(self, first_node : ForkliftNode = None) -> None:
        super().__init__()
        self._head = first_node  
        self._tail = first_node 
        if first_node is None:
            self._size = 0
        else:
            self._size = self.count()

    def count(self) -> int:
        counter = 0
        cur_node = self._head
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
        return counter
        
    def append(self, new_node : ForkliftNode) -> bool:
        try:
            if self._size == 0:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                self._tail = new_node
            self._size += 1
            return True
        except Exception as e:
            print(e)
            return False

    def insert(self, index_number : int, new_node : ForkliftNode) -> bool:
        try:
            index_counter = 0
            cur_node = self._head
            if index_number == 0:
                new_node.next = self._head
                self._head = new_node
                self._size += 1
                return True

            while cur_node is not None:
                if index_counter == index_number:
                    pred_node.next = new_node
                    new_node.next = cur_node
                    self._size += 1
                    return True
                else:
                    index_counter += 1
                    pred_node = cur_node 
                    cur_node = cur_node.next
        except Exception as e:
            print(e)
            return False

    def remove(self, target_value : datetime) -> bool:
        cur_node = self._head
        pred_node = cur_node 
        while cur_node is not None:
            if cur_node.iot_datetime == target_value:
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            else:
                pred_node = cur_node 
                cur_node = cur_node.next
        return False        

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)


class _BagIterator(object):
    def __init__(self, head_node : ForkliftNode) -> None:
        super().__init__()
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

#데이터 셋을 입력 받으면 각 지게차 별로 데이터를 이차원 list로 변환하여 반환
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
    fork_id_list = []
    row_data = []
    fork_list_stop = []

    f = open(filename, 'r', encoding='utf-8')
    csv_reader = csv.reader(f)

    for row in csv_reader:
        row_data.append(row)

    if len(row_data) == 0:
        dataset = {}

    else:
        if row_data[0][0] == "id":
            row_data.pop(0)
            dataset = {}
        else:
            dataset = {}
            
    for i in range(len(row_data)):
        if row_data[i][1] in fork_id_list:
            pass
        else:
            fork_id_list.append(row_data[i][1])

    for i in range(len(fork_id_list)):
        dataset[fork_id_list[i]] = []   

    for i in range(len(fork_id_list)):    
        for j in range(len(row_data)):
            if fork_id_list[i] == row_data[j][1]:
                fork_list_stop.append(row_data[j][3])
                fork_list_stop.append(row_data[j][4])
                fork_list_stop.append(row_data[j][2])
                dataset[fork_id_list[i]].append(fork_list_stop)
                fork_list_stop = []
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
    sorted_dataset = {}
    for key in dataset.keys():
        sorted_dataset[key] = sorted(dataset[key], key = lambda l : l[2])
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
    sorted_dataset = sort_dataset(sorted_dataset)
    for key in sorted_dataset.keys():
        value = LinkedListBag()
        for x_coordination, y_coordination, fork_datetime in sorted_dataset[key]:
            value.append(ForkliftNode(key, float(x_coordination), float(y_coordination), datetime.strptime(fork_datetime, "%Y-%m-%d %H:%M:%S.%f")))
        linkedlist_bag_dict[key] = value
    return linkedlist_bag_dict

def main():
    DATASET_FILENAME = "forklist_move.csv"
    dataset = load_dataset(DATASET_FILENAME)
    sorted_result = sort_dataset(dataset)
    result = build_linkedlistbag(dataset)
    # print(build_linkedlistbag(sorted_result) == build_linkedlistbag(dataset))
    # print(build_linkedlistbag(sorted_result))
    print(build_linkedlistbag(dataset))
    for key in dataset.keys():
        for node in result[key]:
            print(node)
    # print(sorted_result)
    # result = build_linkedlistbag(sorted_dataset=sorted_result)
    # print(result)
    # print(build_linkedlistbag(result))
    # print(result.keys())
    # node_info = sort_dataset(dataset)[forklift_name][0]
    # node = ForkliftNode(forklift_name, node_info[0], node_info[1], node_info[2])
    # print(node)

if __name__ == "__main__":
    main()
