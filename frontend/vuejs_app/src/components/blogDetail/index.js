import gql from "graphql-tag"

export const BLOG_DETAIL = gql`query blogPostQuery($id: Int!) {
  blogPost(id: $id) {
    id,
    title,
    fullText,
    image,
    author {
      id,
      firstName,
      lastName
    },
    createdAt,
    updatedAt,
    comments {
      id,
      text,
      createdAt,
    	updatedAt,
      author {
        id,
        firstName,
        lastName
    	},
    }
  }
}`;
