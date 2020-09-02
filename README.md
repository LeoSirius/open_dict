# Open Dict

`Open Dict` is a web dictionary service.

Database using MongoDB. If the word to search is in database, api return the meaning in database, else return meaning from web by scraper.

Currently only support [bing dict search](https://cn.bing.com/dict/search), and language is English only.

## Get started

> notice the trailing slash

### Get one word

```sh
curl http://api.opendict.top/api/words/leo/
```

response

```json
{
  "name":"leo",
  "meanings":[
    {"pos":"n.","meaning":"黄道第五宫；狮子宫；狮子（星）座"},
    {"pos":"网络","meaning":"狮子座；利奥；里奥"}
  ]
}
```

### Get words in batch

```sh
curl http://api.opendict.top/api/words-batch/?word=love&word=and&word=peace
```

response

```json
{
  "word_list":[
    {
      "name":"love",
      "meanings":[
        {
          "pos":"n.",
          "meaning":"爱；爱情；热爱；恋爱"
        },
        {
          "pos":"v.",
          "meaning":"爱；喜欢；热爱；喜爱"
        },
        {
          "pos":"网络",
          "meaning":"爱心；真爱"
        }
      ]
    },
    {
      "name":"and",
      "meanings":[
        {
          "pos":"conj.",
          "meaning":"与；和；而；又"
        },
        {
          "pos":"n.",
          "meaning":"附加条件；附加细节"
        },
        {
          "pos":"网络",
          "meaning":"并且；而且；及"
        }
      ]
    },
    {
      "name":"peace",
      "meanings":[
        {
          "pos":"n.",
          "meaning":"和平；平静；宁静；和睦"
        },
        {
          "pos":"网络",
          "meaning":"平和；安宁；静谧"
        }
      ]
    }
  ]
}
```

## TODO

- unitest
- api rate limit
- multiple word scraper
