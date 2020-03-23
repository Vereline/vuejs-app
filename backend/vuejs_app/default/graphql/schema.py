from graphene import Mutation, Boolean
from graphene_file_upload.scalars import Upload


class UploadMutation(Mutation):
    class Arguments:
        file = Upload(required=True)

    success = Boolean()

    def mutate(self, info, file, **kwargs):
        # do something with your file
        return UploadMutation(success=True)
