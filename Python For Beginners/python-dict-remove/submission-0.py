from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for x in range(len(keys)):
        if keys[x] in my_dict:
            my_dict.pop(keys[x])
        else:
            my_dict.pop(keys[x],0)
    return my_dict

# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
