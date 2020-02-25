<template>
  <b-modal id="login-modal" ref="login-modal" hide-footer>
    <template v-slot:modal-title>
      <div class="text-uppercase">Login</div>
    </template>
    <div class="modal-container">
      <div class="modal-body mb-2">
        <b-form>
          <b-form-group
            label="Username or email"
            label-for="login-username"
            :invalid-feedback="invalidUsername"
            :valid-feedback="validUsername"
            :state="validateUsername"
          >
            <b-form-input
              id="login-username"
              placeholder="Enter your username or email"
              type="email"
              v-model.trim="username"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Password"
            label-for="login-password"
            :invalid-feedback="invalidPassword"
            :valid-feedback="validPassword"
            :state="validatePassword"
          >
            <b-form-input
              id="login-password"
              placeholder="Enter your password"
              type="password"
              v-model.trim="password"
            >
            </b-form-input>
          </b-form-group>
          <b-container class="bv-example-row w-100">
            <b-row>
              <b-col cols="8">
                <b-link class="float-left mt-3"><router-link to="/signup">Don't have an account? Sign Up.</router-link></b-link>
              </b-col>
              <b-col>
                <b-button class="btn-success float-right mt-1" title="Login" v-on:click="loginUser">
                  Login
                </b-button>
              </b-col>
            </b-row>
          </b-container>
        </b-form>
      </div>
    </div>
  </b-modal>
</template>

<script>
  import login from "./index"
  export default {
    name: "LoginModal",
    methods: {
      loginUser() {
        login(this.username, this.password).then((data) => {
        if (data.status === 200) {
          this.closeModal()
        }
        else if (data.status === 400) {
          this.errorMessage = data.errorMessage;
        }
        });
      },
      closeModal(e) {
        this.$refs['login-modal'].hide()
      },
    },
    computed: {
      validateUsername() {
        return this.username.length > 0
      },
      validatePassword() {
        return this.password.length > 0
      },
      invalidUsername() {
        return 'It shouldn\'t be empty at least.'
      },
      invalidPassword() {
        return 'It shouldn\'t be empty at least.'
      },
      validUsername() {
        return 'Looks good!'
      },
      validPassword() {
        return 'Looks good!'
      },
    },
    data () {
      return {
        username: '',
        password: '',
        errorMessage: '',
      }
    }
  }
</script>

<style scoped>

</style>
