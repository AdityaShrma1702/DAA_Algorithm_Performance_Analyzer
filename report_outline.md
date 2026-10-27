# DAA Mini Project Report: Algorithm Performance Analyzer

## Abstract
This project implements and compares three sorting algorithms—Bubble Sort, Merge Sort and Quick Sort—and two searching algorithms—Linear Search and Binary Search. The program measures execution time for different input sizes, saves results to CSV files, and visualizes comparisons using Matplotlib graphs.

## Objectives
1. Implement the selected sorting and searching algorithms.
2. Validate outputs against expected results.
3. Measure execution time for increasing input sizes.
4. Export benchmark data to CSV.
5. Plot the measured times for comparison.

## Methodology
- Generate test inputs.
- Run each algorithm using `time.perf_counter()`.
- Validate sorting results against Python's built-in sorted output.
- Record size, algorithm name, and execution time.
- Save CSV output and create graphs.

## Expected observations
Bubble Sort generally grows much more slowly in performance as input size increases because its average and worst-case complexity is O(n²). Merge Sort is O(n log n). Quick Sort is O(n log n) on average, though its worst case is O(n²). Linear Search is O(n); Binary Search is O(log n) on sorted input.

## Results
Insert the generated CSV tables and graphs from the `outputs/` folder after running the project on your own computer. Actual execution times vary by device and system load.

## Conclusion
The project demonstrates that algorithm choice affects execution time and scalability. It also provides practical experience with implementation, empirical benchmarking, CSV data handling, and graph visualization.
