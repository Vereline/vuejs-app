// const BlogCreate = gql`mutation createBlog($title:String, $fullText: String) {
//       createBlog(title: $title, fullText: $fullText) {
//         task {
//             title
//             fullText
//         }
//         ok
//     }
// }`

// {
//   "title": "something to do",
//   "fullText": "fullText for task"
// }


// const BlogUpdate = gql`mutation updateBlog($id: String, author: Int) {
//   updateBlog(id: $id, author: $author) {
//     task {
//       id
//       author
//       title
//       fullText
//     }
//     ok
//   }`

// {"id": "2", "author": true}
