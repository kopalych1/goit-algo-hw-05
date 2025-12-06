

from random import randint


def binary_search_upper_bound(arr: list[float | int], val: float | int) -> tuple[int, float]:

    if not isinstance(arr, list):
        raise TypeError("Array must be a sorted list of numbers")

    if len(arr) and arr[0] == val:
        return (0, None)

    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= val:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return (iterations, upper_bound)



def main():

    def test(arr, input):
        print(input)
        print(binary_search_upper_bound(arr, input))
        print()

    array = [1.5, 2.3, 3.7, 4.2, 5.8, 7.1, 8.9, 10.5, 12.3, 15.7]
    print(array)

    test(array, 3.7)
    test(array, 4.0)
    test(array, 6.5)
    test(array, 1.0)
    test(array, 20.0)
    test(array, 8.9)

if __name__ == "__main__":
    main()
