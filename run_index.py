

if __name__ == '__main__':
    import time
    print('running index, time: ', time.strftime('%Y-%m-%d %H:%M:%S'))

    from graphrag.index.__main__ import run_index
    print('running index2, time: ', time.strftime('%Y-%m-%d %H:%M:%S'))
    run_index()
    print('end index, time: ', time.strftime('%Y-%m-%d %H:%M:%S'))
