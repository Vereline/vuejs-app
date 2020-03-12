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
  </b-container>
</template>

<script>
  import { PERSON_PROFILE } from './index'
  import { API_URL } from "../../constants"


  export default {
    name: "personProfile",
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
      }
    },
    methods: {
      convertDateFormat(date) {
        return date.toString().split('T')[0];
      },
      formatUserName(firstName, lastName) {
        return firstName + ' ' + lastName;
      },
      convertImgSrc(imagePath) {
        if (imagePath)
          return API_URL + '/media/' + imagePath;
        return ""
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

</style>
