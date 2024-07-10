Simple text to base64 encoder an decoder which add salt key and index parameters

You can use as a lib and by command line:

***
> python main.py -a encrypt -p abc -k xxx -i 1

> python main.py -a decrypt -p ZWl8fHxpZmc= -k xxx -i 1
***

The lib is composed by two functions located in cipher package

```
from cipher import salted


salted.b64_encode(payload: str, salt_key: str, salt_index: int | None = None)
salted.b64_decode(payload: str, salt_key: str, salt_index: int | None = None)
```