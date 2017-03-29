## 基本数据结构
- `slice` 在容量满时，新建`slice`，容量为原来两倍。原先的指针还是引用的原始底层 `array`

## 内存泄露
- 未关闭的 `http.Response.Body`

## 死锁
- `channel` 死锁
- `goroutine` 不阻塞的时候不会让出CPU，必要的时候显式调用 `runtime.Gosched()`
