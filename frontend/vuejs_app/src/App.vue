<template>
  <div id="app">
    <div id="main-page">
    <!-- Navbar -->
      <router-view></router-view>

    <!-- Masthead with image -->
    <header class="masthead">
      <div class="container h-100">
        <div class="row h-100 align-items-end">
          <div class="col-12 text-center text-white ">
            <h2 class="display-4 text-uppercase">Vertically Centered Masthead Content</h2>
            <p class="lead">A great starter layout for a landing page</p>
          </div>
        </div>
      </div>
    </header>

    <!-- Table with pictures -->
    <section>
      <b-container>
        <b-row class="align-items-center">
          <b-col col lg="6"  class="order-lg-2">
            <div class="p-5">
              <b-img class="img-fluid table-img" src="https://via.placeholder.com/700" alt=""/>
            </div>
          </b-col>
          <b-col col lg="6"  class="order-lg-1">
            <div class="p-5">
              <h2 class="display-4 text-uppercase">Explore new imaginary world...</h2>
              <p class="text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod aliquid, mollitia odio veniam sit iste esse assumenda amet aperiam exercitationem, ea animi blanditiis recusandae! Ratione voluptatum molestiae adipisci, beatae obcaecati.</p>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section>
      <b-container>
        <b-row class="align-items-center">
          <b-col col lg="6">
            <div class="p-5">
              <b-img class="img-fluid table-img" src="https://via.placeholder.com/700" alt=""/>
            </div>
          </b-col>
          <b-col col lg="6">
            <div class="p-5">
              <h2 class="display-4 text-uppercase">Read and enjoy an exciting story!</h2>
              <p class="text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod aliquid, mollitia odio veniam sit iste esse assumenda amet aperiam exercitationem, ea animi blanditiis recusandae! Ratione voluptatum molestiae adipisci, beatae obcaecati.</p>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <!-- Footer -->
<!--    <footer class="footer text-center bg-light">-->
<!--      <b-container>-->
<!--        <b-row>-->

<!--          &lt;!&ndash; Footer Location &ndash;&gt;-->
<!--          <b-col class="col-lg-4 mb-5 mb-lg-0">-->
<!--            <h4 class="text-uppercase mb-4">Location</h4>-->
<!--            <p class="lead mb-0">2215 John Daniel Drive-->
<!--              <br>Clark, MO 65243</p>-->
<!--          </b-col>-->

<!--          &lt;!&ndash; Footer Social Icons &ndash;&gt;-->
<!--          <b-col class="col-lg-4 mb-5 mb-lg-0">-->
<!--            <h4 class="text-uppercase mb-4">Around the Web</h4>-->
<!--            <a class="btn btn-outline-light btn-social mx-1" href="#">-->
<!--              <i class="fab fa-fw fa-facebook-f"></i>-->
<!--            </a>-->
<!--            <a class="btn btn-outline-light btn-social mx-1" href="#">-->
<!--              <i class="fab fa-fw fa-twitter"></i>-->
<!--            </a>-->
<!--            <a class="btn btn-outline-light btn-social mx-1" href="#">-->
<!--              <i class="fab fa-fw fa-linkedin-in"></i>-->
<!--            </a>-->
<!--            <a class="btn btn-outline-light btn-social mx-1" href="#">-->
<!--              <i class="fab fa-fw fa-dribbble"></i>-->
<!--            </a>-->
<!--          </b-col>-->

<!--          &lt;!&ndash; Footer About Text &ndash;&gt;-->
<!--          <b-col col lg="4">-->
<!--            <h4 class="text-uppercase mb-4">About Freelancer</h4>-->
<!--            <p class="lead mb-0">Freelance is a free to use, MIT licensed Bootstrap theme created by-->
<!--              <a href="http://startbootstrap.com">Start Bootstrap</a>.</p>-->
<!--          </b-col>-->

<!--        </b-row>-->
<!--      </b-container>-->
<!--    </footer>-->

    <!-- Copyright Section -->
    <section class="copyright py-4 text-center text-white bg-primary">
      <b-container>
        <small>Now I dont have a Copyright &copy; Elven Scroll 2019</small>
      </b-container>
    </section>

    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style lang="scss">

  #app {

  }

  .masthead {
    height: 45vh;
    min-height: 500px;
    background-image: url('https://via.placeholder.com/1920x1080');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
  .table-img {
    min-width: 350px;
  }

</style>
