import math

with open("data.txt") as file: 
    data = file.read()
    parts = data.split("\n\n")
    instructions = parts[0]
    updates =  parts[1]
    
    instructions = instructions.split("\n")
    updates = updates.split("\n")
    # got a blank character at the end, used pop to get rid of the last item ''
    updates.pop()
    rules_dict = {}
    for instruction in instructions:
        orders = instruction.split("|")
        if rules_dict.get(orders[1]) is None: 
            rules_dict[orders[1]] = [orders[0]]

        else: 
            rules_dict.get(orders[1]).append(orders[0])

    def verify_order(pages): 
        def check_page_order(page, pages): 
            # checking to see if this page has a restriction
            pages_first = rules_dict.get(page)
            # if no restriction, remove page from list, return True
            if pages_first is None:
               pages.remove(page)
               return True
               
            # if page restrictions exist, we check to see if those page restrictions are in our list, if not then we continue until no pages are left, then we return True and remove the page
            for page_restriction in pages_first: 
                # if a restriction exists in our list, then we have not encountered it yet which means that our current page is out of order and we can return False
                if page_restriction in pages: 
                    return False
                else: 
                    continue

            pages.remove(page)
            return True

        while True: 
            try: 
                is_ordered = check_page_order(pages[0], pages)
            except IndexError: 
                return True
            if not is_ordered:
                return False


def main(): 
    ordered_pages = []
    middle_num_total = 0
    for update in updates:           
        pages = update.split(",")
        pages_copy = pages.copy()
        is_correct = verify_order(pages_copy)
        if is_correct: 
            ordered_pages.append(pages)
          
    for ordered_page in ordered_pages: 
        half_length = math.floor(len(ordered_page) / 2)
        middle_num = int(ordered_page[half_length])
        middle_num_total += middle_num 

    print(middle_num_total)


main()
