# ParseDataURI #

This light tool is not an robust way to cover all data uri string but most cases 

### How to use ###

```
#!shell
>>> pat = DataURI('data:text/plain;charset=utf-8;base64,UGFyc2UgZGF0YSB1cmkgdG9vbA==')
>>> pat.mimetype
'text/plain'
>>> pat.charset
'utf-8'
>>> pat.data
'Parse data uri tool'
```