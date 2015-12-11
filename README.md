# ParseDataURI #

This light tool is not an robust way to cover all data uri string but most cases 

### How to use ###

```
#!python
In [1]: from parse_data_uri import DataURI

In [2]: pat = DataURI('data:text/plain;charset=utf-8;base64,UGFyc2UgZGF0YSB1cmkgdG9vbA==')

In [3]: pat.mimetype
Out[3]: 'text/plain'

In [4]: pat.charset
Out[4]: 'utf-8'

In [5]: pat.data
Out[5]: 'Parse data uri tool'
```