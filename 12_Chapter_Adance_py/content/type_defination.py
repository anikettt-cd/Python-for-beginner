age : int = 25




def greeting(name: str, age : int) -> str:
    return (f"hello, {name}. you are {age} years old.")

print(greeting("aniket", 33))




# Advance type definition
from typing import List, Tuple, Dict, Set, Optional, Union

numbers : list[int] = [1,2,3,4,5]

person : tuple[str, int] = ("aniket", 25)

scores: Dict[str, int] = {"maths": 90, "science": 85}

idebntifiers : Union[str,int] = {"id1", "id2", "id3"}

print(numbers, person, scores, idebntifiers)
