<template>
  <b-container>
    <b-jumbotron class="mt-3">
      <b-row>
        <div class="col-md-4 col-xs-12 col-sm-6 col-lg-4">
          <img src="https://www.svgimages.com/svg-image/s5/man-passportsize-silhouette-icon-256x256.png" alt="stack photo" class="img"/>
        </div>
        <div class="col-md-8 col-xs-12 col-sm-6 col-lg-8">
          <b-container>
            <h2>John Doe</h2>
          </b-container>
          <hr>
            <ul class="container details">
              <li><p><span style="width:50px;"></span>+91 90000 00000</p></li>
              <li><p><span style="width:50px;"></span>somerandom@email.com</p></li>
              <li><p><span style="width:50px;"></span>Hyderabad</p></li>
              <li><p><span style="width:50px;"></span><a href="#">www.example.com</a></p></li>
          </ul>
        </div>
      </b-row>
    </b-jumbotron>
  </b-container>
</template>

<script>
  export default {
    name: "personProfile",
    data() {
      return {
        author: {
          photo: "",
          username: "",
          id: "",
          createdAt: "",
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

</style>
