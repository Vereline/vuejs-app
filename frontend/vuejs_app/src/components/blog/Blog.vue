<template>
  <b-container class="mt-2">
    <h1>{{ $t("blogMessages.blogs") }}</h1>
    <div class="button-div" v-if="isAdmin" >
      <b-button variant="success" class="float-right">
        <router-link :to="{ name: 'CreateBlog' }">
         {{ $t("blogMessages.createBlog") }}
        </router-link>
      </b-button>
    </div>
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
          {{ $t("blogMessages.viewFull") }}
        </router-link>
      </b-button>
      </b-card-body>
    </b-card>

  </b-container>
</template>

<script>
   import $i18n from '../../locales';
   import { ALL_BLOG_POSTS } from "./index"

    export default {
      name: "Blog",
      $i18n,
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
        formatDate(date) {
          if (date)
            return date.toString().split('T')[0];
          return ""
        },
      },
      computed: {
        isAdmin() {
          return this.$store.state.isAdmin
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

  .button-div {
    width: 100%;
    height: 50px;
  }
</style>
