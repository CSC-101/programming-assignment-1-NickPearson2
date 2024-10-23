import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(string: str) -> int:
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        if letter.lower() in vowels_list:
            count += 1
    return count

# Part 2
def short_lists(theList: list[list[int]]) -> list[int]:
    new_list = []
    for i in theList:
        if(len(i) == 2):
            for j in range(len(i)):
                new_list.append(i[j])
    return new_list


# Part 3
def ascending_pairs(theList: list[list[int]]) -> list[list[int]]:
    new_list = []
    for i in theList:
        if(len(i) == 2):
            if(i[0] > i[1]):
                temp = i[1]
                i[1] = i[0]
                i[0] = temp
                new_list.append(i)
            else:
                new_list.append(i)
        else:
            new_list.append(i)

    return new_list

# Part 4
def add_prices(price1: data.Price, price2: data.Price) -> data.Price:
    if(price1.cents + price2.cents >= 100):
        new_price = data.Price(price1.dollars + price2.dollars +1, price1.cents + price2.cents -100)
        return new_price
    new_price = data.Price(price1.dollars + price2.dollars, price1.cents + price2.cents)
    return new_price
# Part 5
def rectangle_area(rectangle: data.Rectangle) -> int:
    length = abs(rectangle.top_left.x - rectangle.bottom_right.x)
    height = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    area = length * height
    return area


# Part 6
def books_by_author(name:str, list:list[data.Book]) -> list[data.Book]:
    book_list = []
    for book in list:
        for author in book.authors:
            if(author == name):
                book_list.append(book)
    return book_list

# Part 7
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    #Find center point for circle
    center_x = abs((rectangle.top_left.x - rectangle.bottom_right.x)/2) + abs(rectangle.top_left.x)
    center_y = abs((rectangle.top_left.y - rectangle.bottom_right.y)/2) + abs(rectangle.bottom_right.y)
    center_point = data.Point(center_x, center_y)
    #Find radius based on which side is longer
    if(abs((rectangle.top_left.x - rectangle.bottom_right.x)) > abs((rectangle.top_left.y - rectangle.bottom_right.y))):
        radius = abs((rectangle.top_left.x - rectangle.bottom_right.x)/2)
    else:
        radius = abs((rectangle.top_left.y - rectangle.bottom_right.y)/2)

    circle = data.Circle(center_point,radius)
    return circle

# Part 8
def below_pay_average(list:list[data.Employee])->list[str]:
    total_pay = 0
    name_list = []
    if(list == []):
        return None
    for employee in list:
        total_pay += employee.pay_rate
    avg_pay = total_pay/len(list)
    for employee in list:
        if(employee.pay_rate < avg_pay):
            name_list.append(employee.name)
    return name_list