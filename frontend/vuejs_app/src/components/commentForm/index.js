import gql from "graphql-tag"

export const COMMENT_ADD = gql`mutation addComment($text: String!, $blogPostId: String!, $authorId: String!) {
  createComment(text: $text, blogPost: $blogPostId, author: $authorId) {
    ok
    comment{
      id
      text
      author {
        id
        firstName,
        lastName
      }
      blogPost {
        id
      }
    }
  }
}`;

// {
//   "text": "something to comment",
//   "authorId": "2",
//   "blogPostId": "2"
// }

export const COMMENT_UPDATE = gql`mutation updateComment($text: String!, $id: String!) {
  updateComment(text: $text, id: $id) {
    ok
    comment{
      id
      text
      author {
        id
        firstName,
        lastName
      }
      blogPost {
        id
      }
    }
  }
}`;

// {
//   "text": "something to comment",
//   "id": "2"
// }
