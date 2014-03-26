import time

data = {}
start_time = {}

def tic(name=None):
    assert(name not in start_time)
    start_time[name] = time.time()

def toc(name=None):
    duration = time.time() - start_time[name]
    data.setdefault(name, []).append(duration)
    del start_time[name]
    return duration

def clear():
    data.clear()
    start_time.clear()

def dump():
    print('{:>20} {:>10} {:>12} {:>12} {:>12} {:>12}'.format('name', 'num_calls', 'cum_time', 'avg_time', 'min_time', 'max_time'))
    for name, times in sorted(data.items(), key=lambda (k, v): -sum(v)):
        num_calls = len(times)
        cum_time = sum(times)
        avg_time = sum(times) / len(times) 
        min_time = min(times)
        max_time = max(times)
        print '{name:>20s} {num_calls:10} {cum_time:12.6f} {avg_time:12.6f} {min_time:12.6f} {max_time:12.6f}'.format(**locals())

if __name__ == '__main__':
    tic('all')
    tic()
    time.sleep(0.1)
    print toc()

    for i in range(3):
        tic('foo1')
        tic('foo2')
        time.sleep(0.1)
        tic('bar')
        time.sleep(0.1)
        toc('bar')
        toc('foo2')
        toc('foo1')
    toc('all')
    dump()
