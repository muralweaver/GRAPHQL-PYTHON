# Graphql-python

Learning about the Python library for developing a GraphQL server – Graphene – together with Django and Graphene-Django.

> GraphQL is a strongly typed query language that describes how to request data. GraphQL declares everything as a graph. You request what you want, and then you will get what you expected. Nothing more, nothing less.


<!--
QUERY
```
query {
  links {
    id
    description
    url
  }
}

query {
  users {
    id
    username
    email
  }
}
```
MUTATIONS
```
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

mutation{
  createUser(username:"hellographql", email:"hello@example.com", password:"chroot") {
    user{
      id
      email
      username
    }
  }
}
```
-->

## Useful Links
- [How To GraphQL](https://www.howtographql.com/)
