<template>
  <b-container
    v-on:add-comment="addComment"
    v-on:update-comment="updateComment">
    <b-row>
      <div class="col-lg-8">
        <h1>{{ blogPost.title }}</h1>
        <p class="lead">
          By <router-link :to="{ name: 'PersonProfile', params: {id: blogPost.author.id }}">
          {{ formatAuthorName(blogPost.author.firstName, blogPost.author.lastName) }}
        </router-link>
        </p>
        <hr/>
        <p class="text-right">Posted on {{convertDateFormat(blogPost.createdAt)}}</p>
        <p class="text-right">Updated on {{convertDateFormat(blogPost.updatedAt)}}</p>
        <hr/>
        <div>
          <div v-if="blogPost.image">
            <img class="img-fluid rounded" :src="convertImgSrc(blogPost.image)" alt="Title Image" />
          </div>
        </div>
        <p class="lead main-text mt-4">{{ blogPost.fullText }}</p>
        <hr/>
        <h4 class="text-uppercase mb-3">Comments</h4>
        <div v-for="(comment, key) in blogPost.comments">
          <comment v-bind:comment="comment"
                   v-bind:blog-post-id="id"
                   v-bind:author="comment.author">
          </comment>
        </div>

        <!-- Comment form -->
        <comment-form class="mt-4" v-bind:blog-post-id="id"></comment-form>
      </div>
    </b-row>
  </b-container>
</template>

<script>
  import { BLOG_DETAIL } from "./index"
  import { API_URL } from "../../constants"
  import Comment from "../comment/Comment";
  import commentForm from "../commentForm/commentForm";

  export default {
    name: "blogDetail",
    components: {commentForm, Comment},
    //   beforeRouteEnter (to, from, next) {
    //   next(vm => {
    //     vm.id = to.params.id
    //   })
    // },
    data() {
      return {
        id: this.$route.params.blogId,
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
            photo: "",
          },
          comments: [
            {
              id: "",
              text: "",
              createdAt: "",
              updatedAt: "",
              author: {
                id: "",
                firstName: "",
                lastName: "",
                photo: "",
              },
            },
          ],
        },
      }
    },
    methods: {
      convertDateFormat(date) {
        if (date)
          return date.toString().split('T')[0];
        return ""
      },
      convertImgSrc(imagePath) {
        if (imagePath)
          return API_URL + '/media/' + imagePath;
        return ""
      },
      formatAuthorName(firstName, lastName) {
        return firstName + ' ' + lastName
      },
      addComment(commentData) {
        debugger;
        this.data.comments = [...this.data.comments, commentData];
      },
      updateComment(commentData) {
        this.data.comments = [...this.data.comments, commentData];
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
