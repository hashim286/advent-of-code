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


    def create_page_order(pages): 
        def iterate_pages(page, page_order): 
            # checks if we recursed at all
            recursed = False
            pages_first = rules_dict.get(page)
            if pages_first is None and page not in page_order and not recursed: 
               # if the current num has no restrictions on it and it is not in the ordered list and we did not recurse, we can add it otthe page_order list
               page_order.append(page)
               return page_order, recursed

            for page_restriction in pages_first: 
                # if the restriction is not in our ordered list and it is in our instructions we check to see if it has any restrictions to place it correctly by recalling this function
                if page_restriction not in page_order and page_restriction in pages: 
                    page_order = iterate_pages(page_restriction, page_order)[0]

                    # because we recursed, we track it here as "True" 
                    recursed = True
                else: 
                    continue
            if page not in page_order: 
                page_order.append(page) 

            return page_order, recursed

        page_order = []
        recursed = False
        for page in pages: 
            update_status = iterate_pages(page, page_order)
            # if update_status[1] was True meaning we did recurse, we track it outside of the function so it stays permanent
            if update_status[1]: 
                recursed = True

        return page_order, recursed


def main(): 
    incorrect_lists = []
    middle_num_total = 0
    for update in updates:           
        pages = update.split(",")

        # update_status is a tuple containing a list and a boolean 
        update_status = create_page_order(pages)
        # if the boolean variable was True, it means the list recursed and had to perform a reordering so we can count it as incorrect
        if update_status[1]:
            incorrect_lists.append(update_status[0])

    # calculating the middle number
    for incorrect_list in incorrect_lists: 
        half_length = math.floor(len(incorrect_list) / 2)    
        middle_num = int(incorrect_list[half_length])
        middle_num_total += middle_num                 

    print(middle_num_total)

main()
