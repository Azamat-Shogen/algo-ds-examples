def suggestion_product(products, search_word):
    res = []
    products.sort()  # Sort the products lexicographically
    l, r = 0, len(products) - 1

    for i in range(len(search_word)):
        char = search_word[i]

        # Narrow down the search window
        while l <= r and (len(products[l]) <= i or products[l][i] != char):
            l += 1
        while l <= r and (len(products[r]) <= i or products[r][i] != char):
            r -= 1

        # Collect suggestions from the current window
        res.append([])
        remain = r - l + 1  # Calculate the size of the current window

        for j in range(min(3, remain)):  # Add up to 3 products
            res[-1].append(products[l + j])

    return res


products_list = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
print(suggestion_product(products_list, 'mouse'))
