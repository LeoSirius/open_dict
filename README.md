# Open Dict

`Open Dict` is a web dictionary service.

Database using MongoDB. If the word to search is in database, api return the meaning in database, else return meaning from web by scraper.

Currently only support [bing dict search](https://cn.bing.com/dict/search), and language is English only.

## Sample

> notice the trailing slash

```
curl http://host-domain/leo/
```

response

```
{"name":"leo","meanings":[{"pos":"n.","meaning":"黄道第五宫；狮子宫；狮子（星）座"},{"pos":"网络","meaning":"狮子座；利奥；里奥"}]}
```
