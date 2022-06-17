price_per_one_page = float(input())
price_per_one_cover = float(input())
percent_discount_for_paper = int(input())
price_for_designer = float(input())
percent_of_whole_price = int(input())
book_pages = 899
book_covers = 2

sum_for_print = price_per_one_page * book_pages + price_per_one_cover * book_covers
price_after_discount = sum_for_print - (sum_for_print * percent_discount_for_paper / 100)
price_after_designer = price_after_discount + price_for_designer
final_price = price_after_designer - (price_after_designer * percent_of_whole_price / 100)

print(f"Avtonom should pay {final_price:.2f} BGN.")