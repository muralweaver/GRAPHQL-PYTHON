from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


'''
In this mutation the server will receive a username, password and email, returning the created user information. 
Remember that on your last mutation – CreateLink – the mutation returned field by field, now, you are returning a full User, where the client can ask the fields it wants.
 '''


class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user


'''
The concept of authentication and authorization is enabled by default in Django using sessions.
Since most of the web apps today are stateless, we are going to use the django-graphql-jwt library to implement JWT Tokens in Graphene

Basically, when a User signs up or logs in, a token will be returned: a piece of data that identifies the User. 
This token must be sent by the User in the HTTP Authorization header with every request when authentication is needed.
'''
