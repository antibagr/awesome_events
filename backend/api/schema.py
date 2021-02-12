import graphene
from graphql.execution.base import ResolveInfo
from graphene_django.debug import DjangoDebug


# class Mutation(graphene.ObjectType):
#     pass


class Query(graphene.ObjectType):

    test = graphene.String()

    def resolve_test(self, info: ResolveInfo) -> str:
        return "API works"

    debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(query=Query, mutation=None)
