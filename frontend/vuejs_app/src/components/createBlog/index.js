import gql from "graphql-tag"

export const BLOG_CREATE = gql`mutation createBlog($title:String!, $fullText: String!, $authorId: Int!) {
      createBlogPost(title: $title, fullText: $fullText, authorId: $authorId) {
        blogPost {
          title
          id
          fullText
          author {
            id
          }
        }
        ok
    }
}`;

// export const inputData = {
//   "title": "something to do",
//   "fullText": "fullText for task",
//   "authorId": 1
// }

export const BLOG_UPDATE = gql`mutation updateBlog($title:String!, $fullText: String!, $id: String!) {
      updateBlogPost(title: $title, fullText: $fullText, id: $id) {
        blogPost {
          id
          title
          fullText
          author {
            id
          }
        }
        ok
    }
}`;


// {
//   "id": 2,
//   "title": "something to do1",
//   "fullText": "fullText for task1"
// }
