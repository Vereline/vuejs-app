<template>
  <b-container class="mt-2">
    <h1>{{ $t("createBlog.titleLabel") }}</h1>
    <!-- form starts here -->
    <b-form>
      <div class="field">
        <label class="label">{{ $t("createBlog.titleLabel") }}</label>
        <div class="control">
          <b-input name="title"
                   class="input"
                   type="text"
                   v-model="formData.title"
                   required
                   :placeholder='$t("createBlog.titlePlaceholder")'>
          </b-input>
        </div>
      </div>

      <b-container class="text-center">
        <image-loader v-model="blogImage"
                      v-on:toggle-loaded-new-blog-image="toggleLoadedNewImage"
                      loadEvent="toggle-loaded-new-blog-image">
          <div slot="activator">
            <div   v-if="!blogImage"
                   class="m-1 empty-image"
                   v-bind:style="{backgroundImage: 'url(' + backgroundPhoto + ')'}"
            >
            </div>
            <p v-if="!blogImage" class="text-center">{{ $t("createBlog.imageText") }}</p>
            <div   v-else
                   class="m-1 empty-image"
                   v-bind:style="{backgroundImage: 'url(' + blogImage.imageURL + ')'}"
            >
            </div>
          </div>
        </image-loader>

        <div v-if="blogImage && loadedNewImage && savedImage === false">
          <b-button type="submit"
                    class="btn btn-success mt-3"
                    v-on:click="uploadBlogImage"
                    :loading="savingImage">
            {{ $t("createBlog.uploadImageText") }}
          </b-button>
        </div>
      </b-container>


      <div class="field">
        <label class="label">{{ $t("createBlog.descriptionLabel") }}</label>
        <div class="control">
          <b-textarea name="description"
                    id="description"
                    class="textarea"
                    v-model="formData.description"
                    :placeholder='$t("createBlog.descriptionPlaceholder")'
                    required>
          </b-textarea>
        </div>
      </div>

      <b-button class="btn-success float-right mt-1"
                variant="success"
                v-on:click="submitButton"
      >
        {{ $t("createBlog.createButton") }}
      </b-button>
    </b-form>
  </b-container>
</template>

<script>
  import { BLOG_CREATE, BLOG_UPDATE } from "./index"
  import ImageLoader from "../imageLoader/imageLoader";
  import {API_URL} from "../../constants";
  import {UPLOAD_BLOG_IMAGE} from "../imageLoader";

  export default {
    name: "createBlog",
    components: {ImageLoader},
    props: {
      author: String,
      blogId: String,
    },
    computed: {
      backgroundPhoto() {
        return this.convertImgSrc(this.blog.photo)
      },
    },
    data() {
     return {
       formData: {
           title: "",
           description: "",
       },
       blog: {
         photo: "",
       },
       blogImage: null,
       savingImage: false,
       savedImage: false,
       loadedNewImage: false,
     }
    },
    apollo: {
    // here load blog in case I'm updating it
    },
    watch:{
      blogImage: {
        handler: function() {
          this.savedImage = false
        },
        deep: true
      }
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
              authorId: Number(this.$store.state.id),
            }
          })
          .then(response => {
            let blogId = response.data["createBlogPost"]["blogPost"]["id"];
            // redirect to detail blog page
            this.$router.push("blog/" + blogId);
          })
      },
      updateBlog() {
        this.$apollo
          .mutate({
            mutation: BLOG_UPDATE,
            variables: {
              title: this.formData.title,
              fullText: this.formData.description,
              id: this.blogId,
              authorId: Number(this.author),
            }
          })
          .then(response => {
            let blogId = response.data["updateBlogPost"]["blogPost"]["id"];
            // redirect to detail blog page
            this.$router.push("blog/" + blogId);
          })
      },
      uploadBlogImage() {
        this.savingImage = true;
        // here apollo mutation
        this.savingImage = true;
        // here apollo mutation
        this.$apollo
        .mutate({
          client: 'apolloFileClient',
          mutation: UPLOAD_BLOG_IMAGE,
            variables: {
              file: this.profileImage.imageFile,
              id: this.id,
            },
        }).then(response => {
          if (response.data['success'])
            this.savedBlogImage()
          }
        );
      },
      toggleLoadedNewImage(value) {
        this.loadedNewImage = value
      },
      savedBlogImage() {
        this.savingImage = false;
        this.savedImage = true
      },
      convertImgSrc(imagePath) {
        if (imagePath)
          return API_URL + '/media/' + imagePath;
        return ""
      },
    },
   }
</script>

<style scoped lang="scss">
  .empty-image {
    display: flex;
    border-radius: 12px;
    background-color: #ecf0f1;
    width: 100%;
    height: 300px;
    text-align: center;
    justify-content: center;
    align-items: center;
    vertical-align: middle;

    background-position:center center;
    background-repeat:no-repeat;
    background-size:cover;

    &:hover {
      cursor: pointer;
    }
  }
</style>
