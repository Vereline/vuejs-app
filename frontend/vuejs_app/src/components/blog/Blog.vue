<template>
  <b-container class="mt-2">
    <h1>Blog</h1>
    <!-- blog card -->
    <b-card class="text-left news-card"
            v-for="(newsItem, key) in news">
      <b-card-body>
      <b-card-title>
        <strong>{{ newsItem.title }}</strong>
      </b-card-title>
      <b-card-sub-title class="mb-2 text-muted text-right">{{ newsItem.createdAt }}</b-card-sub-title>
      <b-card-text class="news-card__text">
         {{ formedDescription(newsItem.description) }}
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
    export default {
      name: "Blog",
      data() {
        return {
          news: [
            {
              title: "asd",
              description: "asdasdasdasdasd",
              createdAt: "23123123",
              id: 1,
            },
            {
              title: "asd",
              description: "asdasdasdasdasdrgsr tgdkrtg slrtihj srlt.ikh ujsrthyfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffioksdtrdkgfjth drktghj stguh s;etiugh seirugh srelefzedrgxergsergsxergxergxdrgxdrgxrdgiugh sdreiugth",
              createdAt: "23123123",
              id: 2,
            },
          ],
          maxLength: 150,
        }
      },
      methods: {
        formedDescription(description) {
          return description.length <= this.maxLength ? description: description.toString().substring(0, this.maxLength) + "..."
        },
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
