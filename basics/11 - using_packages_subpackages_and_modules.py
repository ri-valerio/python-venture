#!/usr/bin/python




# import your module like this
import some_package.some_subpackage.bazinga_module

some_package.some_subpackage.bazinga_module.func_from_bazinga_module()


# or like this
import some_package.some_subpackage.bazinga_module as something

something.func_from_bazinga_module()


# import a specific module inside some packages
from some_package.another_subpackage import bazinga_module

bazinga_module.func_from_bazinga_module()


# or import the function directly
from some_package.another_subpackage.bazinga_module import func_from_bazinga_module

func_from_bazinga_module()


# or like this
from some_package.another_subpackage.bazinga_module import func_from_bazinga_module as my_hacky_func

my_hacky_func()
