from random import shuffle

from generate_data import generate


def quick_sort_it(data):
    len_data = len(data)
    if len_data > 0:
        quick_sort(data, 0, len_data - 1)


def quick_sort(data, start, end):
    if start > end:
        return

    previews_start = start
    previews_end = end
    pivot = data[start]

    while previews_start < previews_end:
        while previews_start < previews_end and data[previews_end] > pivot:
            previews_end = previews_end - 1

        if previews_start < previews_end:
            data[previews_start] = data[previews_end]
            previews_start = previews_start + 1

        while previews_start < previews_end and data[previews_start] <= pivot:
            previews_start = previews_start + 1

        if previews_start < previews_end:
            data[previews_end] = data[previews_start]
            previews_end = previews_end - 1

        data[previews_start] = pivot

    quick_sort(data, start, previews_start - 1)
    quick_sort(data, previews_start + 1, end)


if __name__ == "__main__":
    data = generate(50)
    shuffle(data)
    print(data, "\n")
    quick_sort_it(data)
    print(data)
