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

  export default {
    name: "createBlog",
    props: {
      author: String,
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
  }
</script>

<style scoped lang="scss">

</style>
