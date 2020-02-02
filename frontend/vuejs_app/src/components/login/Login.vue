<template>
  <b-modal id="login-modal" hide-footer title="Login" text-uppercase centered>
    <div class="modal-container">
      <div class="modal-body mb-2">
        <b-form>
          <b-form-input class="m-1" placeholder="Enter your username or email" type="email" v-model.trim="username"></b-form-input>
          <b-form-input class="m-1" placeholder="Enter your password" type="password" v-model.trim="password"></b-form-input>
          <div class="w-100">
          <b-button class="btn-success float-right mt-2" title="Login" v-on:click="loginUser">
            Login
          </b-button>
          </div>
        </b-form>
      </div>
      <div class="modal-footer mt-5">
        <b-link class="float-right"><router-link to="/signup">Don't have an account? Sign Up.</router-link></b-link>
      </div>
    </div>

  </b-modal>
</template>

<script>
  import login from "./index"
  export default {
    name: "LoginModal",
    methods: {
      loginUser: function () {
        login(this.username, this.password)
      },
    },
    data () {
      return {
        username: '',
        password: '',
      }
    }
  }
</script>

<style scoped>

</style>
