import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        word = "Hello"
        self.assertEqual(hw1.vowel_count(word), 2)
    def test_vowel_count2(self):
        word = "Counted vOwELs"
        self.assertEqual(hw1.vowel_count(word), 5)

    # Part 2
    def test_short_lists1(self):
        list = [[1,2,3],[1,2],[3,4],[1,2,3,4,5],[9,8]]
        result = [1,2,3,4,9,8]
        self.assertEqual(hw1.short_lists(list), result)
    def test_short_lists2(self):
        list = [[1,2],[1,2],[3,4],[],[9,8]]
        result = [1,2,1,2,3,4,9,8]
        self.assertEqual(hw1.short_lists(list), result)
    # Part 3
    def test_ascending_Pairs1(self):
        list = [[1,2,3],[1,2],[3,4],[1,2,3,4,5],[9,8]]
        result = [[1,2,3],[1,2],[3,4],[1,2,3,4,5],[8,9]]
        self.assertEqual(hw1.ascending_pairs(list), result)
    def test_ascending_Pairs2(self):
        list = [[1,2,3],[1,2],[10,3],[5,2,10,4,5],[9,8]]
        result = [[1,2,3],[1,2],[3,10],[5,2,10,4,5],[8,9]]
        self.assertEqual(hw1.ascending_pairs(list), result)
    # Part 4
    def test_add_Prices1(self):
        price1 = data.Price(2, 55)
        price2=data.Price(4, 55)
        result = data.Price(7,10)
        self.assertEqual(hw1.add_Prices(price1, price2), result)
    def test_add_Prices2(self):
        price1 = data.Price(2, 10)
        price2=data.Price(4, 55)
        result = data.Price(6,65)
        self.assertEqual(hw1.add_Prices(price1, price2), result)
    # Part 5
    def test_rectangle_area1(self):
        point1 = data.Point(0, 2)
        point2 = data.Point(10, -1)
        rectangle = data.Rectangle(point1, point2)
        self.assertEqual(hw1.rectangle_area(rectangle), 30)
    def test_rectangle_area2(self):
        point1 = data.Point(0, 4)
        point2 = data.Point(8, 0)
        rectangle = data.Rectangle(point1, point2)
        self.assertEqual(hw1.rectangle_area(rectangle), 32)
    # Part 6
    def test_books_by_author1(self):
        book1 = data.Book(['Terry Pratchett','Neil Gaiman' ], 'Good Omens')
        book2 = data.Book(['Janine Pearson', 'Neil Gaiman'], 'Happy Times')
        self.assertEqual(hw1.books_by_author('Neil Gaiman',[book1, book2]), [book1, book2])
    def test_books_by_author2(self):
        book1 = data.Book(['Terry Pratchett', 'Neil Gaiman'], 'Good Omens')
        book2 = data.Book(['Janine Pearson', 'Neil Gaiman'], 'Happy Times')
        book3 = data.Book(["George Orwell","Neil Gaiman" ,"JK Rowling"],'Percy Jackson')
        book4 = data.Book(["William Golding", "Mark Williams"],'Lord of the Flies')
        self.assertEqual(hw1.books_by_author('Neil Gaiman', [book1, book2, book3, book4]), [book1, book2, book3])

    # Part 7
    def test_circle_bound1(self):
        #Test x bigger than y
        point1 = data.Point(10, 5)
        point2 = data.Point(18, 0)
        center = data.Point(14, 2.5)
        rectangle = data.Rectangle(point1, point2)
        result = data.Circle(center, 4)
        self.assertEqual(hw1.circle_bound(rectangle), result)
    def test_circle_bound2(self):
        #Test y bigger than x
        point1 = data.Point(0, 8)
        point2 = data.Point(4, 0)
        center = data.Point(2, 4)
        rectangle = data.Rectangle(point1, point2)
        result = data.Circle(center, 4)
        self.assertEqual(hw1.circle_bound(rectangle), result)
    # Part 8
    def test_below_pay_average1(self):
        person1 = data.Employee("Brennan",20)
        person2 = data.Employee("Ben",50)
        person3 = data.Employee("Jack",30)
        list_empl = [person1, person2, person3]
        result = ["Brennan", "Jack"]
        self.assertEqual(hw1.below_pay_average(list_empl), result)
    def test_below_pay_average_empty(self):
        list_empl = []
        result = None
        self.assertEqual(hw1.below_pay_average(list_empl), result)



if __name__ == '__main__':
    unittest.main()
