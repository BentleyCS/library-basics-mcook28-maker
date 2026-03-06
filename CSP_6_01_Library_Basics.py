from analytics import get_average, get_highest, apply_markup, clean_text, filter_threshold


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    return [apply_markup(price, 0.15) for price in rawPrices]


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    scores = []
    for i in range(n):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)
    return get_highest(scores), get_average(scores)


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
# and all letters lower case.
def sanitize_usernames(usernames):
    return clean_text(usernames)


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(numbers):
    return filter_threshold(numbers, 100)


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
# Sanitize the list to only be lower case words with no extra spaces
# Then return the location of the word using binary search if the list is in order and linear search if it is not.
# example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items):
    sanitized = clean_text(items)
    target = input("Enter item to search for: ").strip().lower()

    is_sorted = sanitized == sorted(sanitized)

    if is_sorted:
        # Binary search
        low, high = 0, len(sanitized) - 1
        while low <= high:
            mid = (low + high) // 2
            if sanitized[mid] == target:
                return mid
            elif sanitized[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    else:
        # Linear search
        for i, item in enumerate(sanitized):
            if item == target:
                return i
        return -1