def findContentChildren(greed,size):

    greed.sort()
    size.sort()

    child_i=0
    content_children=0

    for cookie_size in size:
        if child_i <len(greed) and cookie_size >= greed[child_i]:
            content_children+=1
            child_i+=1

        elif child_i==len(greed):
            break

    return content_children



print(findContentChildren([1,2,3],[1,2]))
