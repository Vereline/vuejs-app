<template>
  <b-container class="mt-2">
    <h1>Create blog</h1>
    <!-- form starts here -->
    <b-form>
      <div class="field">
        <label class="label">Title</label>
        <div class="control">
          <b-input name="title"
                   class="input"
                   type="text"
                   placeholder="Title">
          </b-input>
        </div>
      </div>

      <image-loader></image-loader>

      <div class="field">
        <label class="label" for="description">Description</label>
        <div class="control">
          <b-textarea name="description"
                    id="description"
                    class="textarea"
                    placeholder="Description">
          </b-textarea>
        </div>
      </div>

      <b-button class="btn-success float-right mt-1" title="Login">
        Create blog
      </b-button>
    </b-form>
  </b-container>
</template>

<script>
  import { BLOG_CREATE, BLOG_UPDATE } from "./index"
  import ImageLoader from "../imageLoader/imageLoader";

  export default {
    name: "createBlog",
    components: {ImageLoader},
    props: {
      author: String,
      blogId: String,
    },
    computed: {

    },
    data() {
     return {
       formData: {
           title: "",
           description: "",
       },
     }
    },
    apollo: {

    },
    methods: {
      submitButton(){
        if (this.commentId)
          this.updateBlog();
        else
          this.addBlog();
      },
      addBlog() {
        this.$apollo
          .mutate({
            mutation: BLOG_CREATE,
            variables: {
              title: this.formData.title,
              fullText: this.formData.description,
              authorId: this.author
            }
          })
          .then(response => {
            let blogId = response.data["id"];
            // redirect to detail blog page
            this.$router.replace("blog/" + blogId);
          })
      },
      updateBlog() {
        this.$apollo
          .mutate({
            mutation: BLOG_UPDATE,
            variables: {
              title: this.formData.title,
              fullText: this.formData.description,
              id: this.blogId
            }
          })
          .then(response => {
            let blogId = response.data["id"];
            // redirect to detail blog page
            this.$router.replace("blog/" + blogId);
          })
      },
    },
   }
</script>

<style scoped lang="scss">

</style>
