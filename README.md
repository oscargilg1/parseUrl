# parseUrl

This tool can be used to create custom wordlists from an input file containing URLs. The tool can generate wordlists containing paths and GET parameters.

### TO DO:
Extract body parameters and links from HTTP requests/responses. 

### Usage
* Get a list of paths and save them in a file

```python parseUrls.py -i urls.txt -p -o outputfile.txt```

* Get a list of GET parameters and save them in a file, storing the values of the parameters is optional.


```python parseUrls.py -i urls.txt -q -o outputfile.txt```

 
