import os


def get_project_root():
    """获取工程所在的根目录
    :return:字符串格式的根目录
    os.path.abspath:获取当前文件的绝对路径
    os.path.dirname:获取当前文件/文件夹的上级目录"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_abs_path(relative_path:str) ->str:
    """
    传递相对路径，得到绝对路径
    :param relative_path:相对路径
    :return: 绝对路径
    """
    project_root = get_project_root()
    return os.path.join(project_root,relative_path)


if __name__ == '__main__':
    print(get_abs_path("config/config.txt"))