

def remove_duplicates(values: list[Hashable]) -> list[Hashable]:
    """Return values without duplicates, keeping their first-seen order.

    Task: walk through the list and keep a value only the first time it occurs.
    """


def count_occurrences(values: list[Hashable]) -> dict[Hashable, int]:
    """Count how often each value appears in the list.

    Task: build a mapping whose keys are values and whose values are counts.
    """



def filter_valid_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep records with a positive integer id, non-empty name, and non-negative amount.

    Task: reject incomplete or incorrectly typed records before processing them.
    """



def calculate_total_and_average(values: list[Number]) -> tuple[Number, float | None]:
    """Return the total and average; the average is None when no values are supplied.

    Task: sum the numbers, then divide by the number of values safely.
    """



def group_by_category(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group records by their required ``category`` field.

    Task: create one list per category and append each matching record to it.
    """



def find_minimum_and_maximum(values: list[Number]) -> tuple[Number | None, Number | None]:
    """Return the smallest and largest value, or (None, None) for an empty list.

    Task: compare all values while handling the empty-list case.
    """
    


def transform_records(
    records: list[dict[str, Any]], transform: Callable[[dict[str, Any]], dict[str, Any]]
) -> list[dict[str, Any]]:
    """Apply a transformation function to every dictionary in the list.

    Task: use a list comprehension (or loop) to produce a transformed record per input.
    """
    



if __name__ == "__main__":
        """Run sample inputs and print their expected outputs."""
    values = [3, 1, 3, 2, 1]
    print("remove_duplicates:", remove_duplicates(values))
    print("expected:           [3, 1, 2]")

    print("count_occurrences:", count_occurrences(values))
    print("expected:          {3: 2, 1: 2, 2: 1}")

    records = [
        {"id": 1, "name": "Ada", "amount": 12.5, "category": "books"},
        {"id": 0, "name": "", "amount": 5, "category": "books"},
        {"id": 2, "name": "Lin", "amount": 8, "category": "games"},
    ]
    print("filter_valid_records:", filter_valid_records(records))
    print("expected:             [{'id': 1, ...}, {'id': 2, ...}]")

    print("calculate_total_and_average:", calculate_total_and_average([10, 20, 30]))
    print("expected:                    (60, 20.0)")

    print("group_by_category:", group_by_category(records))
    print("expected:          {'books': [first, second], 'games': [third]}")

    print("find_minimum_and_maximum:", find_minimum_and_maximum([8, 3, 12, 5]))
    print("expected:                 (3, 12)")

    transformed = transform_records(
        records,
        lambda record: {**record, "name": record["name"].upper()},
    )
    print("transform_records:", transformed)
    print("expected:          records with names 'ADA', '', and 'LIN'")
