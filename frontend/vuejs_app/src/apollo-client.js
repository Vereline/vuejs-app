import Vue from 'vue'
import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'

import {API_URL} from "./constants";

const httpLink = new HttpLink({
  // You should use an absolute URL here
  uri: API_URL + '/graphql',
});

// Create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true,
});

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
});

// Install the vue plugin
Vue.use(VueApollo);

export default apolloProvider
