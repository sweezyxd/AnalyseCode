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

![image](https://user-images.githubusercontent.com/98488748/218310382-27b9a6d8-48a4-48b6-b111-0f8eee18b1dc.png)

Result: ```(0.45505857467651367, 'Function')```

Usage of save():

![image](https://user-images.githubusercontent.com/98488748/218310557-4a7e6108-da52-4f9c-b6e0-9a8fe1a82f95.png)

Result:

![Capture](https://user-images.githubusercontent.com/98488748/218310570-926ece65-c501-4458-b0ad-f21d4dd75954.PNG)

Usage of load():


