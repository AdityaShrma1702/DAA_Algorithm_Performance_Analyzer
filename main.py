from algorithms import bubble_sort, merge_sort, quick_sort, linear_search, binary_search
from benchmark import benchmark_sorting, benchmark_searching, save_results, plot_sorting, plot_searching

def main():
    print("=" * 58)
    print("       DAA ALGORITHM PERFORMANCE ANALYZER")
    print("=" * 58)
    print("This project compares sorting and searching algorithms.")
    print("Algorithms: Bubble, Merge, Quick Sort; Linear, Binary Search")
    print()

    sizes = [100, 500, 1000, 2000, 5000]
    sorting_rows = benchmark_sorting(sizes)
    searching_rows = benchmark_searching([100, 1000, 5000, 10000, 50000])

    save_results(sorting_rows, "outputs/sorting_results.csv")
    save_results(searching_rows, "outputs/searching_results.csv")
    plot_sorting(sorting_rows, "outputs/sorting_comparison.png")
    plot_searching(searching_rows, "outputs/searching_comparison.png")

    print("Sorting benchmark results:")
    for row in sorting_rows:
        print(f"n={row['size']:>5} | {row['algorithm']:<12} | {row['time_seconds']:.6f} sec")
    print("\nSearching benchmark results:")
    for row in searching_rows:
        print(f"n={row['size']:>5} | {row['algorithm']:<12} | {row['time_seconds']:.8f} sec")
    print("\nDone! CSV files and graphs are saved in the outputs/ folder.")

if __name__ == "__main__":
    main()
