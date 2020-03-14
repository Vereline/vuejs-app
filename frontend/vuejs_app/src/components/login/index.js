import axios from 'axios';
import store from '../../store';
// import gql from "graphql-tag";
import {API_URL} from "../../constants";

export function login(username, password) {
  const data = {
    'username_or_email': username,
    'password': password,
  };
  const url = 'accounts/token-auth';
  const options = {
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
    data: data,
    url: `${API_URL}/${url}/`,
  };

  return axios(options)
    .then(response => {
      store.commit('setToken', response.data['token']);
      store.commit('setIsLogin');
      // store.commit('setId');
      // store.commit('setUsername');
      return {status: response.status, errorMessage: ''};
    })
    .catch(error => {
      return {
        status: error.response.status,
        errorMessage: error.response.request.responseText,
       };
    })
}


export function getProfileData(){
  const url = 'accounts/profile';
  const options = {
    method: 'GET',
    headers: {
      'content-type': 'application/json',
      'Authorization': 'Bearer ' + store.state.token,
    },
    url: `${API_URL}/${url}/`,
  };

  return axios(options)
    .then(response => {
      store.commit('setId', response.data['id']);
      store.commit('setUsername', response.data['username']);
      store.commit('setFirstName', response.data['first_name']);
      store.commit('setLastName', response.data['last_name']);
      if (response.data['is_staff'])
        store.commit('setIsAdmin');
      return {status: response.status, errorMessage: ''};
    })
    .catch(error => {
      return {
        status: error.response.status,
        errorMessage: error.response.request.responseText,
       };
    })
}
