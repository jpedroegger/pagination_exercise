def modify_based_on_page_position(pages, current_page, total_pages, boundaries, around):
    if (current_page+around) < (total_pages-boundaries) and (current_page-around) > (boundaries):
        del pages[current_page+around:-boundaries]
        pages.insert(-boundaries, "...")
        del pages[boundaries:(current_page-around-1)]
        pages.insert(boundaries, "...")    
    elif (current_page+around) < (total_pages-boundaries):
        del pages[current_page+around:-boundaries]
        pages.insert(-boundaries, "...")    
    elif (current_page-around) > (boundaries):
        del pages[boundaries:(current_page-around-1)]
        pages.insert(boundaries, "...")        

def modify_when_no_boundaries(pages, current_page, total_pages, around):
    del pages[(current_page+around):len(pages)]
    if around < current_page:
        if (current_page - around) > pages[0]:
            del pages[0:current_page-around-1]
            pages.insert(0, "...")
    if (current_page + around) < total_pages:
        pages.insert(len(pages),"...")

def variable_isvalid(current_page, total_pages, boundaries, around):
    if total_pages < 1:
        total_pages = 1        
    if current_page < 1:
        current_page = 1
    elif current_page > total_pages:
        current_page = total_pages
    if boundaries < 0:
        boundaries = 0
    if around < 0:
        around = 0

    return current_page, total_pages, boundaries, around

def pagination(current_page, total_pages, boundaries, around):    

    valid_variables = variable_isvalid(current_page, total_pages, boundaries, around)
    current_page, total_pages, boundaries, around = valid_variables
    pages = list(range(1, total_pages+1))    
    if boundaries >= (current_page+around) or (total_pages-boundaries) < (current_page-around):
        if total_pages / 2 <= boundaries:
            [print(page, end=" ") for page in pages]  
            return pages
        del pages[boundaries:-boundaries]
        pages.insert(boundaries, "...")
    else:
        if boundaries != 0:
            modify_based_on_page_position(pages, current_page, total_pages, boundaries, around)
        else:
            modify_when_no_boundaries(pages, current_page, total_pages, around)

    [print(page, end=" ") for page in pages]  
    return pages


if __name__ == '__main__':  
    pagination(6, 20, 2, 1)