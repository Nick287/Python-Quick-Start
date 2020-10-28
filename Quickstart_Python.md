## Python Quick Start
1. The purpose of this document is for developers without Python experience to quickly learn and use in the project, accelerate the construction of the fast development environment and promote team cooperation. So this document does not cover Python programming language learning itself so assume you have basic programming background. 

2. this document cover setup Python development environment and how to use pytest do unit test then how to use behave test
   1. If you have a Python development environment that you can use directly, I'm using VS code [here](https://code.visualstudio.com/)
   2. please flow this [tutorial](https://code.visualstudio.com/docs/python/python-tutorial) to setup your python dev environment
      1. [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
      2. [Python SKD](https://www.python.org/downloads/) Please note your version of Windows (Windows x86-64), automatic downloading is not recommended, because the last time I downloaded the x86 version automatically and my computer was on x64 CPU, I had a long search problem.
      3. just follow the document creat your first python app which is "hello world"

3. For beginners of Python, one problem that has wasted me a lot of time is the references to different py files, because Python doesn't have namespace like Java or C#, so to know how to references to methods or classes are very important.
   1. Here I recommend the simplest way its add the __ init __.py file with each file directory that means to create a package base on the .py file in this folder. 
   2. some referance [Modules](https://docs.python.org/3/tutorial/modules.html) and [How to create a Python Package with __ init __.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)
   ![Image of init](img\Pythoninit.png)

4. Python unit test (pytest)
   1. Unit testing is a key part of software development, and the first time I did it in Python is with Pytest, which was very easy to use, so the next i will talk about Pytest from my experence.
   2. pytest env
      1. install pytest
         -  ```pip install -U pytest```
      2.  Verify the installation
          -  ```pytest --version```
      ![pytest --version](img\pytest_v.PNG)
      3. pytest official document
         - [Full pytest documentation](https://docs.pytest.org/en/latest/contents.html)
  
   3. In the PyTest framework, there are the following constraints
      1. All UT file names need to be in either the test_*.py or *_test.py format.
      2. In a UT file, the Test class starts with Test and cannot have an init method (note: when defining a class, you need to start with T, otherwise Pytest won't run the class)
      3. In a test class, you can include one or more functions beginning with Test_
      4. When the Pytest command is executed, test functions that match the above constraints are automatically searched from the current directory and subdirectories for execution.
   4. there is an simple code you can download it and run this pytest and the file structure seems like this：
   - ![pytest_structure.PNG](img\pytest_structure.PNG)
   - The test code is very simple which two functions addition and a doubling named **test.py** 
   ```python
         def func(x):
            return x + 1

         def funcdouble(x):
            return x * 2
   ```
    - pytest file under the tests forlder named **test_function.py** there import two function from test.py file and define 2 functions est_plus() and test_double()
   ```python
         from projectcode.test import func, funcdouble

         def test_answer():
            assert func(4) == 5

         def test_double():
            assert funcdouble(4) == 7
   ```
    - run pytest command 
   
   ```
   python -m pytest
   ```
    - Because I made a mistake in writing double as results so this is going to result in one failure and one pass
 ![testresult.png](img\testresult.png)

     - if you can correct my mistake that change the double function result from 7 to 8, then run Pytest again and you will get two passes.
      - ![testresult2.png](img\testresult2.png)


behave test
1. behave 的作用
2. behave 的环境安装
3. behave 框架推荐