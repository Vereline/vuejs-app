import axios from 'axios';
import store from '../store/index'
import {API_URL} from "./constants";

export default function login(username, password) {
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
  axios(options)
    .then(response => {
      console.log(response.data);
      store.commit('setToken', response.data['token']);
    })
    .catch(error => console.log(error));
}
