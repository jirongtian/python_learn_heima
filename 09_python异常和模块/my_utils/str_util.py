"""
字符串相关工具模块
"""


def str_reverse(s):
    """
    功能是反转字符串
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    功能是按照给定的下标完成给定字符串的切片
    :param s: 将被切片的字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 字符串切片
    """
    return s[x:y:]


if __name__ == '__main__':
    print(str_reverse("hello"), substr("hello", 1, 3))