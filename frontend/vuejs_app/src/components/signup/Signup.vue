<template>
  <div>
    <b-modal id="signup-modal" ref="signup-modal" hide-footer>
    <template v-slot:modal-title>
      <div class="text-uppercase">Sign up</div>
    </template>
    <div class="modal-container">
      <div class="modal-body mb-2">
        <b-form>
          <b-form-group
            label="Username"
            label-for="signup-username"
            :invalid-feedback="invalidUsername"
            :state="state"
          >
            <b-form-input
              id="signup-username"
              placeholder="Enter your username"
              type="text"
              v-model.trim="username"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Email"
            label-for="signup-email"
            :invalid-feedback="invalidEmail"
            :state="state"
          >
            <b-form-input
              id="signup-email"
              placeholder="Enter your email"
              type="email"
              v-model.trim="email"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="First name"
            label-for="signup-first-name"
            :state="state"
          >
            <b-form-input
              id="signup-first-name"
              placeholder="Enter your first name"
              type="text"
              v-model.trim="firstName"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Last name"
            label-for="signup-last-name"
            :state="state"
          >
            <b-form-input
              id="signup-last-name"
              placeholder="Enter your last name"
              type="text"
              v-model.trim="lastName"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Password"
            label-for="signup-password"
            :invalid-feedback="invalidPassword"
            :state="state"
          >
            <b-form-input
              id="signup-password"
              placeholder="Enter your password"
              type="password"
              v-model.trim="password"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            label="Confirm Password"
            label-for="signup-confirm-password"
            :invalid-feedback="invalidPassword"
            :state="state"
          >
            <b-form-input
              id="signup-confirm-password"
              placeholder="Confirm your password"
              type="password"
              v-model.trim="confirmPassword"
            >
            </b-form-input>
          </b-form-group>
          <b-container class="bv-example-row w-100">
            <b-row>
              <b-col cols="8">
                <b-link class="float-left mt-3"><router-link to="/signup">Already have an account? Log In.</router-link></b-link>
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
