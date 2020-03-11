<template>
  <b-container class="mt-2">
    <h1>Blog</h1>
    <!-- blog card -->
    <b-card class="text-left news-card"
            v-for="(newsItem, key) in blogPosts">
      <b-card-body>
      <b-card-title>
        <strong>{{ newsItem.title }}</strong>
      </b-card-title>
      <b-card-sub-title class="mb-2 text-muted text-right">{{ formatDate(newsItem.createdAt) }}</b-card-sub-title>
      <b-card-text class="news-card__text">
         {{ formatFullText(newsItem.fullText) }}
      </b-card-text>
      <b-button variant="success" class="float-right">
        <router-link :to="{ name: 'BlogDetail', params: { blogId: newsItem.id }}">
          View full
        </router-link>
      </b-button>
      </b-card-body>
    </b-card>

    <b-button variant="success" class="mt-3 float-right">
      <router-link :to="{ name: 'CreateBlog' }">
       Create Blog
      </router-link>
    </b-button>

  </b-container>
</template>

<script>
   import { ALL_BLOG_POSTS } from "./index"

    export default {
      name: "Blog",
      data() {
        return {
          blogPosts: [
            {
              title: "",
              fullText: "",
              createdAt: "",
              id: 1,
            },
          ],
          maxLength: 150,
        }
      },
      methods: {
        formatFullText(fullText) {
          return fullText.length <= this.maxLength ? fullText: fullText.toString().substring(0, this.maxLength) + "..."
        },
        formatDate(date){
            return date.toString().split('T')[0];
        },

      },
      apollo: {
        blogPosts: {
          query: ALL_BLOG_POSTS
        }
      },
    }
</script>

<style scoped lang="scss">
  .news-card {
    margin-bottom: 10px;

    .news-card__text {
      text-indent: 30px;
      text-align: justify;
    }
  }

 a {
   text-decoration: none;
   color: #fff;

   &:hover, &:active {
     text-decoration: none;
     color: #fff;
   }
 }
</style>
