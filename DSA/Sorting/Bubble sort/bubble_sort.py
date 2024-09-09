def bubble_sort(elements):
    size=len(elements)

    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if elements[j]>elements[j+1]:
                tmp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=tmp
                swapped=True

        if not swapped:
            break

if __name__=="__main__":
    elements1 = [5,9,2,1,67,34,88,34]
    elements2 = [1,2,3,4,2]
    elements3 = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements1)
    print(elements1)

    bubble_sort(elements2)
    print(elements2)

    bubble_sort(elements3)
    print(elements3)


