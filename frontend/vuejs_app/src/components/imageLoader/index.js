import gql from "graphql-tag"


export const UPLOAD_BLOG_IMAGE = gql`
  mutation($file: Upload!, $id: Int!) {
    uploadBlogImage(file: $file, id: $id) {
      success
    }
  }
`;

export const UPLOAD_PROFILE_IMAGE = gql`
  mutation($file: Upload!, $id: Int!) {
    uploadProfilePhoto(file: $file, id: $id) {
      success
    }
  }
`;
