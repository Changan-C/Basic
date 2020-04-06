def my_abs(x):
    '''
    自定义abs函数
    :param x: int or flaat
    :return: abs值
    '''
    if not isinstance(x, (int,float)):
        raise TypeError('only int and float allowed')
    if x>=0:
        return x
    else:
        return -x