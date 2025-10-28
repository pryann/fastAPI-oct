# basic types: int, float, bool, str, list, dict, set, tuple


def summarize(a: int, b: int) -> int:
    return a + b


# list
# old syntax:
# from typing import List
# def get_short_strs(string_list: List[str], max_length:int) -> List[str]:
def get_short_strs(string_list: list[str], max_length: int) -> list[str]:
    return [s for s in string_list if len(s) <= max_length]


# tuple
def get_blue_value(rgb: tuple[int, int, int]) -> int:
    return rgb[2]


# dict
def get_first_name(names: dict[str, str]) -> str:
    return names.get("first_name", "")


# set: set[bytes]

# Other types
# UUID, datatime, datetime.date, datetime.time, datetime.timedelta, bytes, frozenset, Decimal


# union type
# old syntax
# from typing import Union
# def get_age(age: Union[str, int]) -> int:
def get_age(age: str | int) -> int:
    # in real life you need to handle the case where age is not a valid int
    # if isinstance(age, int):
    #   return age
    # else:
    #   return int(age)
    # if isinstance(age, int):
    #   return age
    # return int(age)
    return age if isinstance(age, int) else int(age)


# default value
def concat_user_name(first_name: str, last_name: str, title: str | None = None) -> str:
    full_name = f"{first_name} {last_name}"
    return full_name if title is None else f"{title} {full_name}"


# the default value is mutable, initialize only once, can lead to unexpected behavior
def add_item_to_basket(item: str, basket: list[str] | None = None) -> list[str]:
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print(add_item_to_basket("apple"))
print(add_item_to_basket("banana"))
print(add_item_to_basket("orange"))

# class types and Annotations will be covered later
