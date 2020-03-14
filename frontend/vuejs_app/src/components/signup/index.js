import axios from 'axios';
import store from '../../store';
import {API_URL} from "../../constants";

export function signup(signupData) {
  const url = 'accounts/signup';
  const options = {
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
    data: signupData,
    url: `${API_URL}/${url}/`,
  };

  return axios(options)
    .then(response => {
      store.commit('setToken', response.data['token']);
      store.commit('setIsLogin');
      return {status: response.status, errorMessage: ''};
    })
    .catch(error => {
      return {
        status: error.response.status,
        errorMessage: error.response.request.responseText,
       };
    })
}
