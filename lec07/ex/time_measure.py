from time import time, perf_counter, process_time, sleep

begin = [time(), perf_counter(), process_time()]
sleep(3)
end = [time(), perf_counter(), process_time()]
print("sleep(3):")
for b, e in zip(begin, end):
    print((e-b))
print("#"*20)

begin = [time(), perf_counter(), process_time()]
s = ""
for i in range(1000000):
    s+=str(i)
end = [time(), perf_counter(), process_time()]
print("str concate1")
for b, e in zip(begin, end):
    print((e-b))
print("#"*20)

begin = [time(), perf_counter(), process_time()]
s = "".join([str(i) for i in range(1000000)])
end = [time(), perf_counter(), process_time()]
print("str concate2")
for b, e in zip(begin, end):
    print((e-b))
print("#"*20)
