import gql from "graphql-tag"

const addComment = gql`mutation addComment {
  addComment(input: {
    text: "Cast Away",
    post: {
        id: 3
      }
    author: {
        id: 3
      }
  }) {
    ok
    comment{
      id
      text
      author {
        id
        firstName,
        lastName
      }
      post: {
        id
      }
    }
  }
`;

const updateComment = gql`
mutation updateComment {
  updateComment(id:1, input: {
    text: "Cast Away",
    post: {
        id: 3
      }
    author: {
        id: 3
      }
  }) {
    ok
    comment{
      id
      text
      author {
        id
        firstName,
        lastName
      }
      post: {
        id
      }
    }
  }
`;
