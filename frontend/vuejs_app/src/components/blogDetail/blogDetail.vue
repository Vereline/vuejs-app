<template>
  <b-container>
    <b-row>
      <div class="col-lg-8">
        <h1>{{ blogPost.title }}</h1>
        <p class="lead">
          By <router-link :to="{ name: 'PersonProfile', params: {id: blogPost.author.id }}">
          {{ formatAuthorName(blogPost.author.firstName, blogPost.author.lastName) }}
        </router-link>
        </p>
        <hr/>
          <p>Posted on {{convertDateFormat(blogPost.createdAt)}}</p>
          <hr/>
          <p>Updated on {{convertDateFormat(blogPost.updatedAt)}}</p>
          <div>
            <div>
              <img class="img-fluid rounded" :src="convertImgSrc(blogPost.image)" alt="Title Image" />
            </div>
          </div>
          <p class="lead main-text mt-4">{{ blogPost.fullText }}</p>
          <hr/>
          <Comment v-for="(comment, key) in comments"></Comment>

        <!-- Comment form -->
      </div>
    </b-row>
  </b-container>
</template>

<script>
  import { BLOG_DETAIL } from "./index"
  import { API_URL } from "../../constants"
  import Comment from "../comment/Comment";

  export default {
    name: "blogDetail",
    //   beforeRouteEnter (to, from, next) {
    //   next(vm => {
    //     vm.id = to.params.id
    //   })
    // },
    data() {
      return {
        id: this.$route.params.blogId,
        comments: {
          id: "",
          text: "",
          createdAt: "",
          updatedAt: "",
          author: {
            id: "",
            firstName: "",
            lastName: "",
          },
        },
        blogPost: {
          id: "",
          title: "",
          createdAt: "",
          updatedAt: "",
          fullText: "",
          image: "",
          author: {
            id: "",
            firstName: "",
            lastName: "",
          },
        },
      }
    },
    methods: {
      convertDateFormat(date) {
        return date.toString().split('T')[0];
      },
      convertImgSrc(imagePath) {
        return API_URL + '/media/' + imagePath
      },
      formatAuthorName(firstName, lastName) {
        return firstName + ' ' + lastName
      },
      addComment() {
        // push()
      },
    },
    apollo: {
      blogPost: {
        query: BLOG_DETAIL,
        variables () {
          return {
            id: this.id
          }
        }
      }
    },
  }
</script>

<style scoped lang="scss">
  .row {
    justify-content: center;
  }

  .news-detail {
    text-align: left;
  }

  .main-text {
    text-indent: 30px;
    text-align: justify;
  }
</style>
