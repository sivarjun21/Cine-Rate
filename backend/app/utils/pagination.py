from math import ceil


def paginate(
    items: list,
    page: int = 1,
    page_size: int = 10
):
    total_items = len(items)

    total_pages = ceil(
        total_items / page_size
    )

    start = (page - 1) * page_size

    end = start + page_size

    paginated_items = items[start:end]

    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "data": paginated_items
    }