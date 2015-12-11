# ParseDataURI #

This light tool is not an robust way to cover all data uri string but most cases.

You could use it to parse a data uri string or compose a data uri string by providing necessary data. The default value of mimetype is `text/plain` and the default charset is `us-ascii`. Please refer to [Request for Comments (RFC) 2397](http://www.rfc-base.org/rfc-2397.html) to see more details.

### How to use ###

#### Parse ####
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

#### Formatter ####

```
#!python
In [1]: from parse_data_uri import DataURI

In [2]: DataURI.formatter(data='Parse data uri tool')
Out[2]: 'data:text/plain;charset=us-ascii;base64,UGFyc2UgZGF0YSB1cmkgdG9vbA=='

In [3]: DataURI.formatter(charset='utf-8', data='Parse data uri tool')
Out[3]: 'data:text/plain;charset=utf-8;base64,UGFyc2UgZGF0YSB1cmkgdG9vbA=='

```