<template>
  <b-container>
    <b-jumbotron class="mt-3">
      <b-row>
        <div class="col-md-4 col-xs-12 col-sm-6 col-lg-4">
          <img :src="convertImgSrc(user.photo)" alt="stack photo" class="img img-fluid rounded"/>
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

    <b-container >
      <image-loader v-model="profileImage" v-on:toggle-loaded-new-image="toggleLoadedNewImage">
        <div slot="activator">
          <p>Click to add profile photo</p>
          <div   v-if="!profileImage"
                 class="m-1 empty-image">
            <span>Click to add profile photo</span>
          </div>
          <b-img height="150px" width="150px"
                 v-else
                 :src="profileImage.imageURL"
                 class="mb-3 profile-image-picker"
                 alt="profileImage">
          </b-img>
        </div>
      </image-loader>
      <div v-if="profileImage && loadedNewImage && savedImage === false">
        <b-button type="submit"
                  class="btn btn-success"
                  v-on:click="uploadProfileImage"
                  :loading="savingImage">
          Save profile photo
        </b-button>
      </div>
    </b-container>
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
        debugger;
        this.savingImage = true;
        // here apollo mutation
        this.$apollo
        .mutate({
          client: 'apolloFileClient',
          mutation: UPLOAD_PROFILE_IMAGE,
            variables: {
              file: this.profileImage.imageURL,
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

    &:hover {
      cursor: pointer;
    }
  }

  .profile-image-picker:hover {
    cursor: pointer;
  }

</style>
