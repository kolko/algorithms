# -*- coding: utf-8 -*-
import unittest
import random
from itertools import takewhile

#TODO: Galloping

def sort(array):
    array = list(array)
    array_len = len(array)
    minrun = get_minrun(array_len)
    # print(minrun)
    #make_run_list
    run_list = make_run_list(array, array_len, minrun)
    run_list = sort_run_list(array, run_list)
    merge_run_list(array, run_list, merge_function)
    return array

def get_minrun(array_len):
    if array_len < 64:
        return array_len
    r = 0
    while array_len >= 64:
        r |= array_len & 1
        array_len >>= 1
    return array_len + r

def make_run_list(array, array_len, minrun):
    if array_len == 0:
        yield 0, 0
        return
    if array_len == 1:
        yield 0, 1
        return
    position = 0
    while position < array_len-1:
        if position == array_len-1:
            #последний элемент
            yield position, 1
        if array[position] <= array[position+1]:
            takewhile_lambda = lambda pos: array[pos[1]-1] <= array[pos[1]] or pos[0] < minrun-1
        else:
            takewhile_lambda = lambda pos: array[pos[1]-1] > array[pos[1]] or pos[0] < minrun-1

        run_length = len(list(takewhile(takewhile_lambda, list(enumerate(range(position+1, array_len)))))) + 1

        yield position, run_length
        position += run_length

def sort_run_list(array, run_list):
    for start_pos, length in run_list:
        for pos in range(start_pos+1, start_pos+length):
            cur_item = array[pos]
            prev_pos = pos - 1
            while (prev_pos >= start_pos) and (array[prev_pos] > cur_item):
                array[prev_pos+1] = array[prev_pos]
                array[prev_pos] = cur_item
                prev_pos -= 1

        yield start_pos, length

def merge_run_list(array, run_list, merge_fun):
    stack = []
    for run_item in run_list:
        stack.append(run_item)
        if len(stack) < 3:
            continue
        x, y, z = stack[-3:]
        # X > Y + Z
        # Y > Z
        while (x[1] <= y[1] + z[1]) or (y[1] <= z[1]):
            if z[1] < x[1]:
                stack.pop()
                stack.pop()
                merge_fun(array, y, z)
                stack.append((y[0], y[1]+z[1]))
            else:
                stack.pop()
                stack.pop()
                stack.pop()
                merge_fun(array, x, y)
                stack.append((x[0], x[1]+y[1]))
                stack.append(z)
            if len(stack) < 3:
                break
            x, y, z = stack[-3:]
    # assert len(stack) <= 3
    # print(len(stack))
    # print(stack)
    while len(stack) != 1:
        y = stack.pop()
        x = stack.pop()
        merge_fun(array, x, y)
        stack.append((x[0], x[1]+y[1]))

def merge_function(array, first_item, second_item):
    # print(first_item, second_item)
    assert first_item[0] < second_item[0]
    assert first_item[0] + first_item[1] == second_item[0]
    # print(first_item[1], second_item[1])
    pos_f, pos_s = first_item[0], second_item[0]
    len_f, len_s = first_item[1], second_item[1]
    end_f, end_s = pos_f + len_f, pos_s + len_s
    #TODO: if len_f <= len_s:
    for f_item in list(array[pos_f:pos_f+len_f]):
        if (pos_s == end_s) or (f_item <= array[pos_s]):
            array[pos_f] = f_item
            pos_f += 1
        else:
            while f_item > array[pos_s]:
                array[pos_f] = array[pos_s]
                pos_f += 1
                pos_s += 1
                if pos_s == end_s:
                    break
            array[pos_f] = f_item
            pos_f += 1


class TestRunList(unittest.TestCase):
    # def setUp(self):
    #     pass
    # random.shuffle(self.seq)
    def _get_run_list(self, array, custom_minrun=None):
        array_len = len(array)
        minrun = custom_minrun or get_minrun(array_len)
        # print(minrun)
        return list(make_run_list(array, array_len, minrun))

    def test_run_list1(self):
        array = [1,2,3,4,5,6,7,8]*10
        self.assertEqual(self._get_run_list(array), [(0, 40), (40, 40)])

    def test_run_list2(self):
        array = [1,2,3,4,5,3,4,9,7,6,5,4,3,2,1]
        self.assertEqual(self._get_run_list(array, custom_minrun=1), [(0, 5), (5, 3), (8, 7)])

    def test_run_list3(self):
        array = [1,2,3,1,8,2,3,2,1,2,3]
        self.assertEqual(self._get_run_list(array, custom_minrun=3), [(0, 3), (3, 4), (7, 3)])

    def test_random(self):
        for _ in range(10):
            array = [random.randrange(10000) for _ in range(random.randrange(100))]
            run_list = list(self._get_run_list(array))
            length_from_run_list = sum([x[1] for x in run_list])
            self.assertEqual(len(array), length_from_run_list, 'Error run_list {0} for array {1}'.format(run_list, array))


class TestSortRunList(unittest.TestCase):
    def _get_sorted_run_list(self, array, custom_minrun=None):
        array_len = len(array)
        minrun = custom_minrun or get_minrun(array_len)
        # print(minrun)
        return list(sort_run_list(array, make_run_list(array, array_len, minrun))), array

    def test_random(self):
        for _ in range(10):
            array = [random.randrange(10000) for _ in range(random.randrange(100))]
            run_list, new_array = list(self._get_sorted_run_list(array))
            for start_pos, len in run_list:
                sub_array = new_array[start_pos:start_pos+len]
                self.assertEqual(sub_array, sorted(sub_array), 'Unsorted subarray {0}'.format(sub_array))


class TestSort(unittest.TestCase):
    def test_random(self):
        for _ in range(100):
            array = [random.randrange(10000) for _ in range(random.randrange(10))]
            sorted_array = sort(array)
            self.assertEqual(sorted(array), sorted_array)

if __name__ == '__main__':
    unittest.main()