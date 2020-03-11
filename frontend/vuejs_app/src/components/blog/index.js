import gql from "graphql-tag"

export const ALL_BLOG_POSTS = gql`query allBlogPosts {
  blogPosts {
    id,
    title,
    fullText,
    author {
      id,
      firstName,
      lastName
    },
    createdAt,
    updatedAt
  }
}`;
