def oxford_comma(items):
    if isinstance(items, list) and len(items) == 1:
        return items[0]
    elif isinstance(items, list) and len(items) ==2:
        new_list = " and ".join(items)
        return new_list
    elif isinstance(items, list) and len(items) >= 3:
        last_item = items[-1]
        remaining_items = ", ".join(items[:-1])
        final_list = f"{remaining_items}, and {last_item}"
        return final_list
