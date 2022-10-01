import unittest
from pagination import pagination


class PaginationTest(unittest.TestCase):

    def test_total_pages_is_valid(self):
        total_pages_test = pagination(current_page=18, total_pages=0, boundaries=5, around=2)
        self.assertEqual(total_pages_test, [1])
    
    def test_current_page_is_valid(self):
        negative_current_page = pagination(current_page=-5, total_pages=5, boundaries=5, around=2)
        greater_current_page = pagination(current_page=18, total_pages=5, boundaries=5, around=2)
        self.assertEqual(negative_current_page, [1, 2, 3, 4, 5])
        self.assertEqual(greater_current_page, [1, 2, 3, 4, 5])
    
    def test_boundaries_is_valid(self):
        boundaries_test = pagination(current_page=18, total_pages=20, boundaries=-1, around=2)
        self.assertEqual(boundaries_test, ['...', 16, 17, 18, 19, 20])

    def test_around_is_valid(self):
        around_test = pagination(current_page=18, total_pages=20, boundaries=2, around=-1)
        self.assertEqual(around_test, [1, 2, '...', 18, 19, 20])

    def test_if_current_page_and_around_are_inside_right_boundarie(self):
        pagination_test = pagination(current_page=18, total_pages=20, boundaries=5, around=2)        
        self.assertEqual(pagination_test, [1, 2, 3, 4, 5, '...', 16, 17, 18, 19, 20])

    def test_if_current_page_and_around_are_inside_left_boundarie(self):
        pagination_test = pagination(current_page=2, total_pages=20, boundaries=5, around=2)        
        self.assertEqual(pagination_test, [1, 2, 3, 4, 5, '...', 16, 17, 18, 19, 20])
    
    def test_placeholder_when_current_page_and_around_are_inside_boundaries(self):
        pagination_test_right = pagination(current_page=2, total_pages=30, boundaries=3, around=2)
        pagination_test_left = pagination(current_page=28, total_pages=30, boundaries=5, around=2)
        self.assertEqual(pagination_test_right, [1, 2, 3, 4, '...', 28, 29, 30])
        self.assertEqual(pagination_test_left, [1, 2, 3, 4, 5, '...', 26, 27, 28, 29, 30])

    def test_if_pagination_returns_total_pages_when_boundaries_comprehend_all_pages(self):
        pagination_test = pagination(current_page=2, total_pages=20, boundaries=10, around=2)        
        self.assertEqual(pagination_test, [page for page in range(1, 21)])

    def test_if_current_page_and_around_are_centralized(self):
        pagination_test = pagination(current_page=10, total_pages=20, boundaries=2, around=2)        
        self.assertEqual(pagination_test, [1, 2, '...', 8, 9, 10, 11, 12, '...', 19, 20])
    
    def test_placeholder_when_current_page_and_around_are_centralized(self):
        pagination_test = pagination(current_page=10, total_pages=20, boundaries=2, around=2)
        self.assertEqual(pagination_test, [1, 2, '...', 8, 9, 10, 11, 12, '...', 19, 20])        

    def test_if_current_page_and_around_exceed_left_boundarie(self):
        pagination_test = pagination(current_page=3, total_pages=20, boundaries=5, around=3)        
        self.assertEqual(pagination_test, [1, 2, 3, 4, 5, 6, '...', 16, 17, 18, 19, 20])
    
    def test_if_current_page_and_around_exceed_right_boundarie(self):
        pagination_test = pagination(current_page=17, total_pages=20, boundaries=5, around=3)        
        self.assertEqual(pagination_test, [1, 2, 3, 4, 5, '...', 14, 15, 16, 17, 18, 19, 20])
    
    def test_if_pagination_deletes_until_len_pages_when_bounderies_is_zero(self):
        pagination_test = pagination(current_page=1, total_pages=15, boundaries=0, around=1)
        self.assertEqual(pagination_test, [1, 2, '...'])

    def test_if_pagination_deletes_from_first_index_until_current_page_plus_around_when_bounderies_is_zero(self):
        pagination_test = pagination(current_page=7, total_pages=15, boundaries=0, around=2)
        self.assertEqual(pagination_test, ['...', 5, 6, 7, 8, 9, '...'])

    def test_if_pagination_inserts_placeholder_to_last_index_when_bounderies_is_zero(self):
        pagination_test = pagination(current_page=3, total_pages=15, boundaries=0, around=2)
        self.assertEqual(pagination_test, [1, 2, 3, 4, 5, '...'])

    def test_if_pagination_inserts_placeholder_to_first_index_when_bounderies_is_zero(self):
        pagination_test = pagination(current_page=14, total_pages=15, boundaries=0, around=2)
        self.assertEqual(pagination_test, ['...', 12, 13, 14, 15])

    def test_if_pagination_inserts_placeholder_to_first_and_last_index_when_bounderies_is_zero(self):
        pagination_test = pagination(current_page=7, total_pages=15, boundaries=0, around=2)
        self.assertEqual(pagination_test, ['...', 5, 6, 7, 8, 9, '...'])

if __name__ == '__main__':       
    unittest.main()    
