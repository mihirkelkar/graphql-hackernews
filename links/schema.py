import graphene

from graphene_django import DjangoObjectType

from .models import Link

class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    heading = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        heading = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, heading, description):
        link = Link(url=url, heading=heading, description=description)
        link.save()

        return CreateLink(
                    id=link.id,
                    url=link.url,
                    heading=link.heading,
                    description=link.description
                )


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()
