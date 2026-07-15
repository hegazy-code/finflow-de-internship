Why ThreadPoolExecutor and not ProcessPoolExecutor?
The ingestion functions spend most of their time reading files, writing files, and downloading data. These are I/O-bound operations, so ThreadPoolExecutor is more appropriate. ProcessPoolExecutor creates separate Python processes with additional startup and memory overhead. I would switch to ProcessPoolExecutor only if the ingestion pipeline became CPU-bound, for example when performing heavy calculations 

What would happen if you used ProcessPoolExecutor here instead, and in what scenario would you switch to it for ingestion?
The program would still work if I replaced ThreadPoolExecutor with ProcessPoolExecutor because each ingestion function is independent. However, ProcessPoolExecutor creates separate Python processes, each with its own memory and interpreter. This introduces additional startup and communication overhead. Since the ingestion pipeline mainly waits for file and network I/O rather than performing heavy calculations, using ProcessPoolExecutor would usually provide little or no performance improvement and could even make the execution slower.

