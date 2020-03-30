<template>
  <b-modal id="login-modal"
           ref="login-modal"
           v-model="openedLoginModal"
           hide-footer
           @close="handleClose"
  >
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
              v-model="$v.username.$model"
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
              v-model="$v.password.$model"
              v-model.trim="password"
            >
            </b-form-input>
          </b-form-group>
          <b-container class="bv-example-row w-100">
            <b-alert v-if="errorMessage" variant="danger" show dismissable>
              <strong>An error occurred!</strong><p>{{errorMessage}}</p>
            </b-alert>
            <b-row>
              <b-col cols="8">
                <b-link class="float-left mt-3"><a v-on:click="switchToSignup">Don't have an account? Sign Up.</a></b-link>
<!--                <b-link class="float-left mt-3"><router-link to="/signup">Don't have an account? Sign Up.</router-link></b-link>-->
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
  import { validationMixin } from "vuelidate";
  import { required, minLength } from "vuelidate/lib/validators";

  import {login, getProfileData} from "./index"
  import store from '../../store';

  export default {
    name: "LoginModal",
    mixins: [validationMixin],
    methods: {
      loginUser() {
        // validate before login
        this.$v.$touch();
        if (this.$v.$anyError) {
          return;
        }

        login(this.username, this.password).then((data) => {
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
        // this.$refs["login-modal"].hide()
        store.commit('setCloseLoginModal');
      },
      switchToSignup(e){
        store.commit('setCloseLoginModal');
        store.commit('setOpenSignupModal');
        // this.$refs["login-modal"].hide();
        // this.$refs["signup-modal"].show();
      },
      handleClose(bvModalEvt) {
        // Prevent modal from closing
        bvModalEvt.preventDefault();
        store.commit('setCloseLoginModal');
      }
    },
    computed: {
      validateUsername() {
        return this.username.length >= 5
      },
      validatePassword() {
        return this.password.length >= 5
      },
      invalidUsername() {
        if (this.username.length <= 0)
          return "It shouldn\'t be empty at least.";
        return "Minimum length should be at least 5 symbols"
      },
      invalidPassword() {
        if (this.password.length <= 0)
          return "It shouldn\'t be empty at least.";
        return "Minimum length should be at least 5 symbols"
      },
      validUsername() {
        return "Looks good!"
      },
      validPassword() {
        return "Looks good!"
      },
      openedLoginModal() {
        return this.$store.state.openedLoginModal
      },
    },
    data () {
      return {
        username: "",
        password: "",
        errorMessage: "",
        // isOpen: false,
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
      }
    },
  }
</script>

<style scoped>

</style>
