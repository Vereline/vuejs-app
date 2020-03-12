<template>
  <div id="comment-item" class="media mb-1 text-left">
    <img class="d-flex mr-3 rounded-circle author-photo" :src="convertImgSrc(author.photo)" alt="Author photo"/>
      <div class="media-body card">
        <div class='card-header d-flex justify-content-between'>
          <router-link :to="{ name: 'PersonProfile', params: {id: author.id }}">
            <h5 class="mt-0">{{formatAuthorName(author.firstName, author.lastName)}}</h5>
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
  import { API_URL } from "../../constants"

  export default {
    name: "Comment",
    props: {
      comment: {
        text: String,
        createdAt: String,
      },
      newsId: String,
      author: {
        photo: String,
        firstName: String,
        lastName: String,
        id: String,
      },
    },
    data() {
      return {
        comment: {
            text: "",
            createdAt: "",
        },
        newsId: "",
        author: {
          photo: "",
          firstName: "",
          lastName: "",
          id: "",
        },
      }
    },
    methods: {
      convertDateFormat(date) {
        return date.toString().split('T')[0];
      },
      formatAuthorName(firstName, lastName) {
        return firstName + ' ' + lastName
      },
      convertImgSrc(imagePath) {
        return API_URL + '/media/' + imagePath
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
