# sample_project
Sample python package that has one function which creates a log entry.

### Installation
```txt
pip install git+https://github.com/mrjeffwagner/sample_project.git@master
```

### Usage
After install, run wagner command on cli or import package for use in another python project.

```text
>>> wagner
Wagner command is working!!!
>>> wagner --version
Version 0.1
>>> wagner -h
usage: wagner [-h] [-v]

Wagner help

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  The version of the wagner application.
```

```python
from wagner import main
main.report("Sample Log Message")
```

Output:

```text
2021-11-30 15:00:57.998: Sample Log Message
```

### Uninstall
```text
pip uninstall wagner
```
