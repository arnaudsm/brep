# BREP : Binary Search in plaintext and gzip files
Search large files in O(log n) time using binary search.  
We support plaintext and Gzipped files.

## Benchmark : 8x faster than `grep` on a 2GB dataset !
`brep` is usually faster than `grep` for >1GB datasets.

Check `tests/benchmark.py` to reproduce the results.
```
grep ^777 test.txt : 1.594 s (15 runs)
brep 777 test.txt : 206.8 ms (15 runs)
```

## Installation
`pip install brep` or `pip install .` from this repo

## Index your file
In order to conduct binary search, your file needs to be sorted.    
We recommend `GNU sort`, as it's multithreaded and supports large files.  
`LC_ALL=C sort -u -o output_file input_file`

BREP supports compressed file in the GZIP format.  
We recommend `pigz` for quick multicore compression :
`pigz file`

## Usage
Provide 1 prefix search term and 1 filepath  
`brep 77777 test/large.gz`

You can also search from our Python class  
```python
from brep import Search

for result in Search("77777", "test/large.gz"):
    print(result)
```

## Contribute
PRs are welcome!

Install dev dependencies: `pip install -e .[dev]`  
Test and lint before submitting: `pytest && flake8`  

## Todo
- Reimplement in Rust
- Faster gz size estimation
- Search multiple strings at once