# Python

### Regular Expression

The regular expression is helpful to search a particular pattern from a string. Many languages and tools have the capability of searching a string with regular expressions. In python, you use the `re` module to make use of regular expressions. The basic concept and usage are the same as other languages like Perl, but there's something different. I'm preferably focusing on such a topic here.

One of the most powerful features of regex would be expressing something repeated. They have some special characters to describe repeated characters, which are often referred to as metacharacters.

- `?`: matches zero or one repetition of the preceding expression. For instance, `a?b` matches both `ab` and `b`.
- `*`: matches zero or more repetitions of the preceding expression.
- `+`: matches one or more repetitions of the preceding expression.

Beginning and end of a line:

Some metacharacters stand for the beginning and end of lines: `^` and `$`. The former represents the beginning and the latter the end. For example, `^foo` will match `foobar` but won't match `barfoo` because the second string does not contain `foo` at its beginning.

Predefined character class:
- `\d`: matches any digits. equivalent to `[0-9]`.
- `\s`: matches any whitespaces, including newlines.
- `\S`: matches any non-whitespaces.
- `\w`: matches any alphanumerics characters. equivalent to `[0-9a-zA-Z_]`.

Let's move on to using regex in Python.  Unlike grep and Perl, you need to compile the pattern string before searching for the matches with regex. `re.compile` method compiles a given pattern into a regular expression object, which has some matching methods such as `match`, `search`, and `findall`. These three methods may look similar to one another, but they behave fully differently.

- `search`: It looks for the location that matches the given pattern from the beginning, and it returns the corresponding match object once it finds a match. If it finds nothing, None object will be returned.
- `match`: Only if some characters at the beginning of the string match the given pattern, it returns the corresponding match object. 

```python
>>> import re
>>> p = re.compile(r'[a-z]+[0-9]+')
>>> print(p.search('123abc456'))
<re.Match object; span=(3, 9), match='abc456'>
>>> print(p.match('123abc456'))
None
```

To obtain a specific part of the matching string, you can use the `group` method. You can extract matching subgroups, which are defined with parentheses. For example, `r'(\d+)-(\w+)'` has two subgroups: `(\d+)` and `(\w)`. The matching subgroups can be referred to by calling `m.group(1)` and `m.group(2)`, respectively.

```python
>>> p = re.compile(r'(\d+)-(\w+)')
>>> m = p.match('000-abc123')
>>> m.group(1)
'000'
>>> m.group(2)
'abc123'
```

Also, Python has a more convenient and intuitive way to extract subgroups. The `(?P<name>...)` syntax provides you with named subgroups. It means you can access the subgroups with names instead of indexes.

```python
>>> p = re.compile(r'(?P<number>\d+)-(?P<name>\w+)')
>>> m = p.match('000-abc123')
>>> m.group('number')
'000'
>>> m.group('name')
'abc123'
```

See also: 
- [re - Regular Expression operations](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

### Matplotlib

[Matplolib](https://matplotlib.org/) may be the most common library for data visualization within the Python ecosystem. You can easily connect what you calculated using your own Python code with data visualization process. I'll show some examples and tips on visualizing data with matplotlib.

The below code is the simplest usage of matplotlib. `matplotlib.pyplot` is an easy-to-use interface to Matplotlib. 

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.,2.*np.pi)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```
