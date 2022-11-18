import csv

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
    dataset = {}
    two_dimension_row_data = []

    with open (filename, "r") as csvfile:  # with문을 나올 때 close를 자동으로 불러주기 위해 with open 으로 파일 읽기
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')  # delimiter 옵션으로 파일 내에서 구분자가 무엇인지 선언한다, quotechar 으로 둘러싸이는 구분자를 선언한다. 
        for row in csv_reader:
            two_dimension_row_data.append(row)  #two_dimension_row_data에 각각의 열을 2차원 리스트로 저장

    for data in two_dimension_row_data[1:]:  # data에 row를 한 줄씩 넣어주기
        fork_id, in_dt, emp_x, emp_y = data[1:]  # fork_id, in_dt, emp_x, emp_y에 데이터 언패킹
        if fork_id not in dataset:
            dataset[fork_id] = []
        dataset[fork_id].append([emp_x, emp_y, in_dt])
        
    return dataset

DATASET_FILENAME = "forklist_move.csv"
dataset = load_dataset(DATASET_FILENAME)
print(dataset)