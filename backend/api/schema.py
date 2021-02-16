
from typing import Optional


import graphene
from graphql.execution.base import ResolveInfo
from graphene_django.debug import DjangoDebug

from graphene_django import DjangoObjectType, DjangoListField


from .models import User, Place, Topic, Event, EventFilter


class PlaceType(DjangoObjectType):

    class Meta:
        model = Place
        fields = '__all__'


class TopicType(DjangoObjectType):

    class Meta:
        model = Topic
        fields = '__all__'


class EventType(DjangoObjectType):

    class Meta:
        model = Event
        fields = '__all__'


class FilterType(DjangoObjectType):

    events = DjangoListField(EventType)

    class Meta:
        model = EventFilter
        fields = '__all__'

    def resolve_events(self, *args, **kw):
        return []



class UserType(DjangoObjectType):

    filters = DjangoListField(FilterType)

    last_seen = graphene.DateTime()
    online = graphene.Boolean()

    def resolve_last_seen(self, info):
        return self.last_seen()

    def resolve_online(self, info):
        return self.online()

    def resolve_filters(self, info):
        return self.filters.all()

    class Meta:
        model = User
        fields = ('id', 'ip')

# class Mutation(graphene.ObjectType):
#     pass


class Query(graphene.ObjectType):

    users = DjangoListField(UserType)
    places = DjangoListField(PlaceType)
    topics = DjangoListField(TopicType)
    events = DjangoListField(EventType)

    test = graphene.String()
    get_user = graphene.Field(UserType, ip = graphene.String(), id = graphene.ID())


    def resolve_get_user(self, info: ResolveInfo, ip: Optional[str] = None, id: Optional[str] = None):
        if ip:
            user, _ = User.objects.get_or_create(ip=ip)
            return user
        elif id:
            return User.objects.get(id=id)
        return None


    def resolve_test(self, info: ResolveInfo) -> str:
        return "API works"

    debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(query=Query, mutation=None)
