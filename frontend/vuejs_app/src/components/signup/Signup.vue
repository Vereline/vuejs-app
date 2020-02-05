<template>
  <div>
    <b-modal id="login-modal" ref="login-modal" hide-footer>
    <template v-slot:modal-title>
      <div class="text-uppercase">Sign up</div>
    </template>
    <div class="modal-container">
      <div class="modal-body mb-2">
        <b-form>
          <b-form-group
            label="Username"
            label-for="login-username"
            :invalid-feedback="invalidUsername"
            :state="state"
          >
            <b-form-input
              id="login-username"
              placeholder="Enter your username"
              type="email"
              v-model.trim="username"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Email"
            label-for="login-email"
            :invalid-feedback="invalidEmail"
            :state="state"
          >
            <b-form-input
              id="login-email"
              placeholder="Enter your email"
              type="email"
              v-model.trim="email"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="First name"
            label-for="login-first-name"
            :state="state"
          >
            <b-form-input
              id="login-first-name"
              placeholder="Enter your first name"
              type="text"
              v-model.trim="firstName"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Last name"
            label-for="login-last-name"
            :state="state"
          >
            <b-form-input
              id="login-last-name"
              placeholder="Enter your last name"
              type="text"
              v-model.trim="lastName"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Password"
            label-for="login-password"
            :invalid-feedback="invalidPassword"
            :state="state"
          >
            <b-form-input
              id="login-password"
              placeholder="Enter your password"
              type="password"
              v-model.trim="password"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Confirm Password"
            label-for="login-confirm-password"
            :invalid-feedback="invalidPassword"
            :state="state"
          >
            <b-form-input
              id="login-confirm-password"
              placeholder="Confirm your password"
              type="password"
              v-model.trim="confirmPassword"
            >
            </b-form-input>
          </b-form-group>
          <b-container class="bv-example-row w-100">
            <b-row>
              <b-col cols="8">
                <b-link class="float-left mt-3"><router-link to="/login">Already have an account? Log In.</router-link></b-link>
              </b-col>
              <b-col>
                <b-button class="btn-success float-right mt-1" title="Login" v-on:click="signupUser">
                  Sign up
                </b-button>
              </b-col>
            </b-row>
          </b-container>
        </b-form>
      </div>
    </div>

  </b-modal>
  </div>
</template>

<script>
    export default {
      name: "Signup",
      methods: {
        signupUser() {

        },
        invalidUsername() {

        },
        invalidEmail() {

        },
        invalidPassword() {

        },
      },
      data() {
        return {
            username: '',
            email: '',
            firstName: '',
            lastName: '',
            password: '',
            confirmPassword: '',
        }
      }
    }
</script>

<style scoped>

</style>
