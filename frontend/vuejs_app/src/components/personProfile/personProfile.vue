<template>
  <b-container>
    <b-jumbotron class="mt-3">
      <b-row>
        <div class="col-md-4 col-xs-12 col-sm-6 col-lg-4">
          <b-container class="text-center">
            <image-loader v-model="profileImage"
                          v-on:toggle-loaded-new-image="toggleLoadedNewImage"
                          loadEvent="toggle-loaded-new-image">
              <div slot="activator">
                <div   v-if="!profileImage"
                       class="m-1 empty-image"
                       v-bind:style="{backgroundImage: 'url(' + backgroundPhoto + ')'}"
                >
<!--                  <span>Click to add profile photo</span>-->
                </div>
                <p v-if="!profileImage" class="text-center">Click to add profile photo</p>
                <div   v-else
                       class="m-1 empty-image"
                       v-bind:style="{backgroundImage: 'url(' + profileImage.imageURL + ')'}"
                >
                </div>
<!--                <b-img height="150px" width="150px"-->
<!--                       v-else-->
<!--                       :src="profileImage.imageURL"-->
<!--                       class="mb-3 profile-image-picker"-->
<!--                       alt="profileImage">-->
<!--                </b-img>-->
              </div>
            </image-loader>

            <div v-if="profileImage && loadedNewImage && savedImage === false">
              <b-button type="submit"
                        class="btn btn-success mt-3"
                        v-on:click="uploadProfileImage"
                        :loading="savingImage">
                Save profile photo
              </b-button>
            </div>
          </b-container>
<!--          <img :src="convertImgSrc(user.photo)" alt="stack photo" class="img img-fluid rounded"/>-->
        </div>
        <div class="col-md-8 col-xs-12 col-sm-6 col-lg-8">
          <b-container>
            <h2 class="center-block">{{ formatUserName(user.firstName, user.lastName) }}</h2>
          </b-container>
          <hr>
            <ul class="container details">
              <li><p><span style="width:50px;"></span>{{"Date of join: " + convertDateFormat(user.birthDate)}}</p></li>
              <li><p><span style="width:50px;"></span><a :href="`mailto:${user.email}`">{{user.email}}</a></p></li>
              <li><p><span style="width:50px;"></span>{{"Birth date: " + convertDateFormat(user.birthDate)}}</p></li>
              <li><p><span style="width:50px;"></span>{{"Activity: " +  (user.isActive ? "Active user" : "Not Active user") }}</p></li>
          </ul>
        </div>
      </b-row>
    </b-jumbotron>
  </b-container>
</template>

<script>
  import { PERSON_PROFILE } from './index'
  import { API_URL } from "../../constants"
  import ImageLoader from "../imageLoader/imageLoader";
  import { UPLOAD_PROFILE_IMAGE } from "../imageLoader";


  export default {
    name: "personProfile",
    components: {ImageLoader},
    data() {
      return {
        id: this.$route.params.id,
        user: {
          id: "",
          firstName: "",
          lastName: "",
          birthDate: "",
          photo: "",
          dateJoined: "",
          isActive: "",
          email: "",
        },
        profileImage: null,
        loadedNewImage: false,
        savingImage: false,
        savedImage: false
      }
    },
    computed: {
      backgroundPhoto() {
        return this.convertImgSrc(this.user.photo)
      },
    },
    watch:{
      profileImage: {
        handler: function() {
          this.savedImage = false
        },
        deep: true
      }
    },
    methods: {
      toggleLoadedNewImage(value) {
        this.loadedNewImage = value
      },
      convertDateFormat(date) {
        if (date)
          return date.toString().split('T')[0];
        return "No date"
      },
      formatUserName(firstName, lastName) {
        return firstName + ' ' + lastName;
      },
      convertImgSrc(imagePath) {
        if (imagePath)
          return API_URL + '/media/' + imagePath;
        return ""
      },
      uploadProfileImage() {
        this.savingImage = true;
        // here apollo mutation
        this.$apollo
        .mutate({
          client: 'apolloFileClient',
          mutation: UPLOAD_PROFILE_IMAGE,
            variables: {
              file: this.profileImage.imageFile,
              id: this.id,
            },
        }).then(response => {
          if (response.data['success'])
            this.savedProfileImage()
          }
        );
      },
      savedProfileImage() {
        this.savingImage = false;
        this.savedImage = true
      },
    },
    apollo: {
      user: {
        query: PERSON_PROFILE,
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
  .empty-image {
    display: flex;
    border-radius: 5%;
    background-color: #ecf0f1;
    width: 150px;
    height: 150px;
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

  .profile-image-picker:hover {
    cursor: pointer;
  }

</style>
