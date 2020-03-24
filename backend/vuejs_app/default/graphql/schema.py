from graphene import Mutation, Boolean, String
from graphene_file_upload.scalars import Upload


class UploadMutation(Mutation):
    class Arguments:
        file = Upload(required=True)
        id = String()

    success = Boolean()

    def mutate(self, info, id, file, **kwargs):
        # do something with your file
        return UploadMutation(success=True)
