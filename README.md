# AnalyseCode
Provides you the ability to compare code scripts and functions runtime using matplotlib.

# Usage

First You'll have to download the script and put it in your project directory, after that you can import it in your script by using:

```import Analysis```

after that you can use the different it offers:

```count(function)``` ==> Gives you the time it takes the function given to run.

```save(function, filename)``` ==> Runs the function then saves the runtime the given filename.

```load(filename)``` ==> Loads the filename and returns the function's runtime info.

```bar(functions)``` ==> Shows an analysis of the functions runtime.

# Examples

Usage of count():

```
from analysis import *

def Function():
    x = 0
    for n in range(10000000):
        x = x + 1

count(Function)
```

Result: ```(0.45505857467651367, 'Function')```

Usage of save():

```
from analysis import *

def Function():
    x = 0
    for n in range(10000000):
        x = x + 1
        
save(Function, "FunctionName")
```

Result:

![Capture](https://user-images.githubusercontent.com/98488748/218310570-926ece65-c501-4458-b0ad-f21d4dd75954.PNG)

Usage of load():

```
from analysis import *


def Function():
    x = 0
    for n in range(10000000):
        x = x + 1


print(load("FunctionName"))
```
Result: ```(0.45505857467651367, 'Function')```

Finally, Usage of bar():

```
from analysis import *

def For():
    x = 0
    for n in range(10000000):
        x = x + 1

def While():
    x = 0
    while x < 10000000:
        x = x + 1

bar(For, While)
```

Result:

![Figure_1](https://user-images.githubusercontent.com/98488748/218310954-31d20a9c-a69f-44d2-b00e-3c459ea1ca50.png)


