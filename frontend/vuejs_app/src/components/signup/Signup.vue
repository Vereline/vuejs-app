<template>
  <b-modal
    id="signup-modal"
    ref="signup-modal"
    v-model="openedSignupModal"
    hide-footer
    @close="handleClose"
  >
  <template v-slot:modal-title>
    <div class="text-uppercase">Sign up</div>
  </template>
  <div class="modal-container">
    <div class="modal-body mb-2">
      <b-form>
        <b-form-group
          label="Username"
          label-for="signup-username"
          :invalid-feedback="invalidItem"
          :valid-feedback="validItem"
          :state="validateUsername"
        >
          <b-form-input
            id="signup-username"
            placeholder="Enter your username"
            type="text"
            v-model="$v.username.$model"
            v-model.trim="username"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          label="Email"
          label-for="signup-email"
          :invalid-feedback="invalidItem"
          :valid-feedback="validItem"
          :state="validateEmail"
        >
          <b-form-input
            id="signup-email"
            placeholder="Enter your email"
            type="email"
            v-model="$v.email.$model"
            v-model.trim="email"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          label="First name"
          label-for="signup-first-name"
          :invalid-feedback="invalidItem"
          :valid-feedback="validItem"
          :state="validateFirstName"
        >
          <b-form-input
            id="signup-first-name"
            placeholder="Enter your first name"
            type="text"
            v-model="$v.firstName.$model"
            v-model.trim="firstName"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          label="Last name"
          label-for="signup-last-name"
          :invalid-feedback="invalidItem"
          :valid-feedback="validItem"
          :state="validateLastName"
        >
          <b-form-input
            id="signup-last-name"
            placeholder="Enter your last name"
            type="text"
            v-model="$v.lastName.$model"
            v-model.trim="lastName"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          label="Password"
          label-for="signup-password"
          :invalid-feedback="invalidItem"
          :valid-feedback="validItem"
          :state="validatePassword"
        >
          <b-form-input
            id="signup-password"
            placeholder="Enter your password"
            type="password"
            v-model="$v.password.$model"
            v-model.trim="password"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          label="Confirm Password"
          label-for="signup-confirm-password"
          :invalid-feedback="invalidConfirmPassword"
          :valid-feedback="validItem"
          :state="validateConfirmPassword"
        >
          <b-form-input
            id="signup-confirm-password"
            placeholder="Confirm your password"
            type="password"
            v-model="$v.confirmPassword.$model"
            v-model.trim="confirmPassword"
          >
          </b-form-input>
        </b-form-group>
        <b-container class="bv-example-row w-100">
          <b-alert v-if="errorMessage" variant="danger" show dismissable>
            <strong>An error occurred!</strong><p>{{errorMessage}}</p>
          </b-alert>
          <b-row>
            <b-col cols="8">
              <b-link class="float-left mt-3"><a v-on:click="switchToLogin">Already have an account? Log In.</a></b-link>
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
</template>

<script>
  import { validationMixin } from "vuelidate";
  import { required, minLength, sameAs } from "vuelidate/lib/validators";
  import store from '../../store';
  import {getProfileData} from "../login/index"
  import {signup} from "./index"

  export default {
    name: "SignupModal",
    mixins: [validationMixin],
    methods: {
      signupUser() {
        // validate fields before signup
        this.$v.$touch();
        if (this.$v.$anyError) {
          return;
        }

        let signupData = {
          username: this.username,
          email: this.email,
          first_name: this.firstName,
          last_name: this.lastName,
          password: this.password,
        };

        signup(signupData).then((data) => {
          if (data.status >= 200 && data.status < 300) {
            getProfileData().then((data) => {
              if (data.status >= 200 && data.status < 300) {
                this.errorMessage = "";
                this.closeModal()
              }
            })
          }
          else if (data.status === 400) {
            this.errorMessage = data.errorMessage;
          }
        });
      },
      closeModal(e) {
        store.commit('setCloseSignupModal');
      },
      switchToLogin(e){
        store.commit('setCloseSignupModal');
        store.commit('setOpenLoginModal');
      },
      handleClose(bvModalEvt) {
        // Prevent modal from closing
        bvModalEvt.preventDefault();
        store.commit('setCloseSignupModal');
      }
    },
    computed: {
      validateUsername() {
        return this.username.length >= 5
      },
      validateEmail() {
        return this.email.length >= 5
      },
      validateLastName() {
        return this.lastName.length >= 5
      },
      validateFirstName() {
        return this.firstName.length >= 5
      },
      validatePassword() {
        return this.password.length >= 5
      },
      validateConfirmPassword() {
          if (this.confirmPassword.length < 5) {
              return false
          }
        return this.password === this.confirmPassword
      },
      invalidItem() {
        return "Minimum length should be at least 5 symbols"
      },
      invalidConfirmPassword() {
        if (!this.confirmPassword) {
          return "It shouldn\'t be empty at least."
        }
        if (this.password !== this.confirmPassword) {
          return "Password and it\'s confirmations don\'t match."
        }
        return "Minimum length should be at least 5 symbols"
      },
      validItem() {
        return "Looks good!"
      },
      openedSignupModal() {
          return this.$store.state.openedSignupModal
      }

    },
    data() {
      return {
        username: "",
        email: "",
        firstName: "",
        lastName: "",
        password: "",
        confirmPassword: "",
        errorMessage: "",
      }
    },
    validations: {
      password: {
        required,
        minLength: minLength(5),
      },
      username: {
        required,
        minLength: minLength(5),
      },
      email: {
        required,
        minLength: minLength(5),
      },
      firstName: {
        required,
        minLength: minLength(5),
      },
      lastName: {
        required,
        minLength: minLength(5),
      },
      confirmPassword: {
        required,
        minLength: minLength(5),
        sameAsPassword: sameAs('password')
      },
    },
  }
</script>

<style scoped>

</style>
