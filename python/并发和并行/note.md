# 并发（Concurrency）
    - 同一时刻只允许一个线程执行
    - 通常应用于I/O操作频繁的场景
# 并行（Parallelism）
    - 同一时刻最多可以所有处理器一起工作
    - 通常应用于CPU heavy
> 在python中两者编码方式差不多。

# Futures模块
    - 位于concurrent.futures库和asyncio，都标识带有延迟的操作。
    - 作为用户，实际上是去schedule这些Futures的执行。
    - Executor类：执行executor.submit(func) 时，它便会安排里面的 func() 函数执行，并返回创建好的 future 实例，以便你之后查询调用。
    - Futures 中的方法 done()表示相对应的操作是否完成——True 表示完成，False 表示没有完成，done() 是 non-blocking 的，会立即返回结果。
    - Futures 中的方法 add_done_callback(fn)，表示 Futures 完成后，相对应的参数函数 fn，会被通知并执行调用。
    - Futures 中的方法 result()，它表示当 future 完成后，返回其对应的结果或异常。
    -  Futures 中的方法 as_completed(fs)，是针对给定的 future 迭代器 fs，在其完成后，返回完成后的迭代器。
    
# 全局解释锁
    - 导致python中同一个时刻只允许一个线程运行
    - I/O被block时，全局解释锁会被释放