

if __name__ == '__main__':
    import time
    print('running query, time: ', time.strftime('%Y-%m-%d %H:%M:%S'))

    from graphrag.query.__main__ import run_query
    print('running query2, time: ', time.strftime('%Y-%m-%d %H:%M:%S'))
    run_query()
    print('end query, time: ', time.strftime('%Y-%m-%d %H:%M:%S'))
