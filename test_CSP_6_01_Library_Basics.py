from CSP_6_01_Library_Basics import process_expenses, analyze_scores, sanitize_usernames, identify_outliers, search_and_report

def test_process_expenses():
    prices = [100, 200, 50]
    result = process_expenses(prices)

    result = [round(x, 2) for x in result]

    assert result == [115.0, 230.0, 57.5]


def test_analyze_scores(monkeypatch):
    inputs = iter(["80", "90", "100"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    highest, avg = analyze_scores(3)

    assert highest == 100
    assert avg == 90


def test_sanitize_usernames():
    usernames = ["  Alice ", "BOB", " ChArLiE  "]
    result = sanitize_usernames(usernames)

    assert result == ["alice", "bob", "charlie"]


def test_identify_outliers():
    nums = [50, 120, 30, 200, 99]
    result = identify_outliers(nums)

    assert result == [120, 200]


def test_search_and_report_sorted(monkeypatch):
    items = [" apple", "banana ", " cherry", "date "]

    monkeypatch.setattr("builtins.input", lambda _: "banana")

    result = search_and_report(items)

    assert result == 1


def test_search_and_report_unsorted(monkeypatch):
    items = ["banana", "apple", "date", "cherry"]

    monkeypatch.setattr("builtins.input", lambda _: "date")

    result = search_and_report(items)

    assert result == 2


def test_search_not_found(monkeypatch):
    items = ["apple", "banana", "cherry"]

    monkeypatch.setattr("builtins.input", lambda _: "orange")

    result = search_and_report(items)

    assert result == -1
