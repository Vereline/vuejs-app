import gql from "graphql-tag"

export const BLOG_CREATE = gql`mutation createBlog($title:String, $fullText: String) {
      createBlog(title: $title, fullText: $fullText) {
        blogPost {
            title
            fullText
        }
        ok
    }
}`;

export const BLOG_UPDATE = gql`mutation updateBlog($id: String, author: Int) {
  updateBlog(id: $id, author: $author) {
    blogPost {
      id
      author
      title
      fullText
    }
    ok
  }`;


// {
//   "title": "something to do",
//   "fullText": "fullText for task"
// }


// {"id": "2", "author": true}
