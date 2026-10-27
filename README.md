# DAA Algorithm Performance Analyzer

A Python mini-project for Design and Analysis of Algorithms (DAA). It compares the execution time of:
- Bubble Sort
- Merge Sort
- Quick Sort
- Linear Search
- Binary Search

The program exports benchmark results to CSV and creates Matplotlib comparison graphs.

## Requirements
- Python 3.10 or newer
- pip

## Run
Open a terminal in this project folder and run:

```bash
pip install -r requirements.txt
python main.py
```

For a small demonstration of each algorithm:

```bash
python demo.py
```

## Output files
After running `main.py`, the `outputs/` folder contains:
- `sorting_results.csv`
- `searching_results.csv`
- `sorting_comparison.png`
- `searching_comparison.png`

## Algorithm summary
| Algorithm | Typical time complexity | Notes |
|---|---|---|
| Bubble Sort | O(n²) average/worst | Simple; inefficient on large inputs |
| Merge Sort | O(n log n) | Divide-and-conquer; uses extra memory |
| Quick Sort | O(n log n) average, O(n²) worst | In-place partitioning in this implementation |
| Linear Search | O(n) | Works on unsorted or sorted data |
| Binary Search | O(log n) | Requires sorted data |

## Notes
Execution times depend on the computer and current system load. Run the program more than once for more reliable comparisons. Do not report a single timing as a universal result.
