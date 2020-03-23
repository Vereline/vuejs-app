import gql from "graphql-tag"

// export const COMMENT_ADD = gql`mutation addComment($text: String, $blogPostId: Int, $authorId: Int) {
//   addComment(input: {
//     text: $text,
//     blogPost: {
//         id: $blogPostId
//       }
//     author: {
//         id: $authorId
//       }
//   }) {
//     ok
//     comment{
//       id
//       text
//       author {
//         id
//         firstName,
//         lastName
//       }
//       blogPost: {
//         id
//       }
//     }
//   }`;

// export const COMMENT_UPDATE = gql`mutation updateComment($text: String, $blogPostId: Int, $authorId: Int) {
//   updateComment(id:1, input: {
//     text: $text,
//     blogPost: {
//         id: $blogPostId
//       }
//     author: {
//         id: $authorId
//       }
//   }) {
//     ok
//     comment{
//       id
//       text
//       author {
//         id
//         firstName,
//         lastName
//       }
//       blogPost: {
//         id
//       }
//     }
//   }`;
