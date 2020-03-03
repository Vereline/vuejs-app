<template>
  <div class="media mb-1 text-left">
    <img class="d-flex mr-3 rounded-circle author-photo" src={{author.photo}} alt="Author photo"/>
      <div class="media-body card">
        <div class='card-header d-flex justify-content-between'>
          <router-link :to="{ name: 'CreateBlog', params: {id: author.id }}">
            <h5 class="mt-0">{{author.username}}</h5>
          </router-link>
          <p class="text-muted text-right small">{{ convertDateFormat(comment.createdAt) }}</p>
        </div>
        <div class='card-body'>
          <p class="text-justify">{{comment.text}}</p>
        </div>
      </div>
  </div>
</template>

<script>
  export default {
    name: "comment",
    data() {
      return {
        comment: {
            text: "",
            createdAt: "",
        },
        newsId: "",
        author: {
          photo: "",
          username: "",
          id: "",
        },
      }
    },
    methods: {
      convertDateFormat(date) {
        return date.toString().split('T')[0];
      },
    },
  }
</script>

<style scoped lang="scss">
  .author-photo {
    width: 50px;
    height: 50px;
  }
</style>
