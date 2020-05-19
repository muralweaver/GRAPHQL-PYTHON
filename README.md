# Graphql-python

Learning all around GraphQL to go from zero to production.



Sample code
```
# QUERY
query {
  links {
    id
    description
    url
  }
}

# MUTATIONS
mutation{
  createLink(
    url: "#",
    description: "#"
  ){
    id
    url
    description
  }
}
```


## Useful Links
- [How To GraphQL](https://www.howtographql.com/)
