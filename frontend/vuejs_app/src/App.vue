<template>
  <div id="app">
    <div id="main-page">
    <!-- Navbar -->
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#" class="text-uppercase">Elven Scroll</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#" class="text-uppercase">Heroes</b-nav-item>
          <b-nav-item href="#" class="text-uppercase">Locations</b-nav-item>
          <b-nav-item href="#" class="text-uppercase">Items</b-nav-item>
          <b-nav-item href="#" class="text-uppercase">Events</b-nav-item>
          <b-nav-item href="#" class="text-uppercase">Blog</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">CZ</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>

          </b-nav-item-dropdown>
          <b-nav-item href="#" disabled>Log In</b-nav-item>
          <b-nav-item href="#" disabled>Sign Up</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

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
              <img class="img-fluid" src="https://via.placeholder.com/500" alt="">
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
              <img class="img-fluid" src="https://via.placeholder.com/500" alt="">
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
</style>
