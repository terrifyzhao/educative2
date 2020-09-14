from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval_index = interval_index
        self.employee_index = employee_index
        self.interval = interval

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    result = []
    heap = []

    for i in range(len(schedule)):
        heappush(heap, EmployeeInterval(schedule[i][0], i, 0))

    pre_interval = heap[0].interval

    while heap:
        top_interval = heappop(heap)

        if pre_interval.end < top_interval.interval.start:
            result.append(Interval(pre_interval.end, top_interval.interval.start))

        pre_interval = top_interval.interval

        tmp_schedule = schedule[top_interval.employee_index]
        if len(tmp_schedule) > top_interval.interval_index + 1:
            heappush(heap, EmployeeInterval(tmp_schedule[top_interval.interval_index + 1], top_interval.employee_index,
                                            top_interval.interval_index + 1))

    return result


def main():
    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
