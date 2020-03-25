import Vue from 'vue'
import { ApolloClient } from 'apollo-client'
import { setContext } from 'apollo-link-context';
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import {createUploadLink} from "apollo-upload-client";
import VueApollo from 'vue-apollo'

import {API_URL} from "./constants";

import store from './store'

const httpLink = new HttpLink({
  // You should use an absolute URL here
  uri: API_URL + '/graphql',
});

const httpFileLink = new createUploadLink({
  // You should use an absolute URL here
  uri: API_URL + '/file-graphql',
});

const authLink = setContext((_, { headers }) => {
  // get the authentication token from local storage if it exists
  const token = store.state.token;
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      Authorization: token ? `Bearer ${token}` : "",
    }
  }
});


// Create the apollo client
const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
  connectToDevTools: true,
});

// Create the apollo client
const apolloFileClient = new ApolloClient({
  link: authLink.concat(httpFileLink),
  cache: new InMemoryCache(),
  connectToDevTools: true,
});

const apolloProvider = new VueApollo({
  clients: {
    apolloClient,
    apolloFileClient,
  },
  defaultClient: apolloClient,
});

// Install the vue plugin
Vue.use(VueApollo);

export default apolloProvider
