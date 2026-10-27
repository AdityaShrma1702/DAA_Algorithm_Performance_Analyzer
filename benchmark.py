import csv
import random
import time
from pathlib import Path
import matplotlib.pyplot as plt
from algorithms import bubble_sort, merge_sort, quick_sort, linear_search, binary_search

def timed_call(function, *args):
    start = time.perf_counter()
    function(*args)
    return time.perf_counter() - start

def benchmark_sorting(sizes):
    rows = []
    funcs = [("Bubble Sort", bubble_sort), ("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]
    for size in sizes:
        data = [random.randint(0, size * 10) for _ in range(size)]
        expected = sorted(data)
        for name, func in funcs:
            elapsed = timed_call(func, data)
            if func(data) != expected:
                raise AssertionError(f"{name} produced incorrect output")
            rows.append({"size": size, "algorithm": name, "time_seconds": elapsed})
    return rows

def benchmark_searching(sizes):
    rows = []
    for size in sizes:
        data = list(range(size))
        target = data[-1] if data else 0
        for name, func in [("Linear Search", linear_search), ("Binary Search", binary_search)]:
            elapsed = timed_call(func, data, target)
            if func(data, target) != (size - 1 if size else -1):
                raise AssertionError(f"{name} produced incorrect output")
            rows.append({"size": size, "algorithm": name, "time_seconds": elapsed})
    return rows

def save_results(rows, filename):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["size", "algorithm", "time_seconds"])
        writer.writeheader()
        writer.writerows(rows)

def _plot(rows, algorithms, filename, title):
    plt.figure(figsize=(9, 5))
    for algorithm in algorithms:
        selected = [r for r in rows if r["algorithm"] == algorithm]
        plt.plot([r["size"] for r in selected],
                 [r["time_seconds"] for r in selected], marker="o", label=algorithm)
    plt.xlabel("Input size (n)")
    plt.ylabel("Execution time (seconds)")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(filename, dpi=160)
    plt.close()

def plot_sorting(rows, filename):
    _plot(rows, ["Bubble Sort", "Merge Sort", "Quick Sort"], filename,
          "Sorting Algorithm Performance Comparison")

def plot_searching(rows, filename):
    _plot(rows, ["Linear Search", "Binary Search"], filename,
          "Searching Algorithm Performance Comparison")
