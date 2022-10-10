def check_which_pages_should_be_inserted_in_pageslist(pages, current_page, total_pages, boundaries, around):    
    if (current_page+around) >= (total_pages-boundaries) and (current_page-around-1) <= (boundaries):
        pages.extend(list(range(1, total_pages+1)))
    elif (current_page+around) < (total_pages-boundaries) and (current_page-around-1) > (boundaries):        
        pages.extend(list(range(1, boundaries+1)))
        pages.insert(boundaries, "...")
        pages.extend(list(range((current_page-around), (current_page+around+1))))
        pages.extend(list(range((total_pages-boundaries+1), (total_pages+1))))
        pages.insert(-boundaries, "...")
    elif (current_page+around) < (total_pages-boundaries):        
        pages.extend(list(range(1, current_page+around+1)))
        pages.extend(list(range((total_pages-boundaries+1), (total_pages+1))))
        pages.insert(-boundaries, "...")
    elif (current_page-around-1) > (boundaries):        
        pages.extend(list(range(1, boundaries+1)))
        pages.insert(boundaries, "...")              
        pages.extend(list(range((current_page-around), (total_pages+1))))

def check_which_pages_should_be_inserted_in_pageslist_if_boundaries_is_zero(pages, current_page, total_pages, around):    
    if (current_page+around) >= (total_pages) and (current_page-around) <= 1:
        pages.extend(list(range(1, total_pages+1)))
    elif (current_page+around) < (total_pages) and (current_page-around) > 1:                
        pages.insert(0, "...")
        pages.extend(list(range((current_page-around), current_page+around+1)))
        pages.insert(total_pages, "...")
    elif (current_page+around) < (total_pages):             
        pages.extend(list(range(1, current_page+around+1)))
        pages.insert(total_pages, "...")
    elif (current_page-around) > 1:                
        pages.insert(0, "...")
        pages.extend(list(range((current_page-around), (total_pages+1))))

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
    pages = []
    if boundaries >= (current_page+around) or (total_pages-boundaries+1) <= (current_page-around):
        if total_pages / 2 <= boundaries:
            pages.extend(list(range(1, total_pages+1)))
            print(*pages, end=" ")
            return pages
        pages.extend(list(range(1, boundaries+1)))
        pages.extend(list(range((total_pages-boundaries+1), (total_pages+1))))
        pages.insert(boundaries, "...")
    else:
        if boundaries != 0:
            check_which_pages_should_be_inserted_in_pageslist(pages, current_page, total_pages, boundaries, around)
        else:
            check_which_pages_should_be_inserted_in_pageslist_if_boundaries_is_zero(pages, current_page, total_pages, around)        

    print(*pages, end=" ")  
    return pages
    

if __name__ == '__main__':
    pagination(1, 1, 1, 1)