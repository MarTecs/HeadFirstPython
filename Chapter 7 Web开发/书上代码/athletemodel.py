import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    # Not shown here as it has not changed since the last chapter.
    pass


def put_to_store(file_list):
    """
    启动网页将文本数据转换为字典中，然后保存为一个pickle文件
    :param file_list:
    :return:
    """
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath  # 每个选手的名字作为字典的键，"值"是AthleteList对象实例
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        # 不要忘记用try/except来保护文件IO代码
        print("File error (put_and_store):" + str(ioerr))
    return all_athletes


def get_from_store():
    """
    这个web运行时，pickle文件中的数据可以作为一个字典供应用使用
    将pickle转换为字典
    :return:
    """
    all_athletes = {}
    try:
        with open("athletes.pickle", "rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store):' + str(ioerr))

    return all_athletes




