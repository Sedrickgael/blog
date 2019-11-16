import graphene
import myblog.schema

class Query(myblog.schema.Query,graphene.ObjectType):

    pass
class Mutation(myblog.schema.RelayMutation,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query,mutation=Mutation)