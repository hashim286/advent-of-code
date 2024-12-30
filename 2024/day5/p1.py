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
    # create a rules dictionary to track the numbers which have restrictions
    rules_dict = {}
    for instruction in instructions:
        # split on the | character, in this case the index 1 will be the number which has a restriction applied where the first number must appear before index 1
        orders = instruction.split("|")
   
        # if orders[1] (the restriction number) is not in our dictionary already, we create a new key and set the value to the index 0 number which is its first restriction
        if rules_dict.get(orders[1]) is None: 
            rules_dict[orders[1]] = [orders[0]]

        # if the number already has a restriction, we append the index 0 on as a new restriction to its existing restriction list
        else: 
            rules_dict.get(orders[1]).append(orders[0])

    def verify_order(pages): 
        # I thought the recursion was already gonna happen in p1 so I created an inner function before realizing I didn't need it for p1 yet
        # this inner function takes the current page we are looping through and the pages list which is our current set of instructions
        def check_page_order(page, pages): 
            # checking to see if this page has a restriction by querying the dictionary for the key being the page
            pages_first = rules_dict.get(page)

            # if no restriction exists then we can just add the number and remove it so we know we encountered it already
            if pages_first is None:
               pages.remove(page)
               return True
               
            # if page restrictions exist, we check to see if those page restrictions are in our current list already. If it is not, we continue and check the next restriction. If the restriction does exist in our list, it means we did not encounter it yet since it hasn't been removed and that this list is out of order
            for page_restriction in pages_first: 
                # if a restriction exists in our list, then we have not encountered it yet which means that our current page is out of order and we can return False
                if page_restriction in pages: 
                    return False
                else: 
                    continue
                
            # if we made it here, we didn't break meaning the list is in order so far and we can remove this page and return True
            pages.remove(page)
            return True

        while True: 
            try: 
                # as long as this is True, we can continue to check each page in the list. We use index 0 here since pages are always removed if they do not fail a restriction check so we are checking the 'next' item in the list every time at the new index 0 
                is_ordered = check_page_order(pages[0], pages)

            # if we get an index error, we checked the whole list and every page was removed meaning it was all in order and we can return True
            except IndexError: 
                return True
            if not is_ordered:
                return False


def main(): 
    ordered_pages = []
    middle_num_total = 0
    for update in updates:           
        pages = update.split(",")
        
        # create a copy of our pages list since we will be mutating this list and want to maintain a clean copy if it passes so we can append it into the ordered_pages list
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
