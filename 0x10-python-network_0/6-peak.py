#!/usr/bin/python3
    """
    Class for finding a peak in a list of unsorted integers.
    """

    @staticmethod
    def find_peak(list_of_integers):
        """
        Finds the peak in a list of numbers.

        Args:
        - list_of_integers: A list of unsorted integers.

        Returns:
        - The peak element in the list.
        """
        length = len(list_of_integers)

        if length == 0:
            return None
        if length == 1:
            return list_of_integers[0]

        low, high = 0, length - 1

        while low < high:
            mid = (low + high) // 2

            if list_of_integers[mid] > list_of_integers[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return list_of_integers[low]
