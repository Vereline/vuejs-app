import gql from 'graphql-tag'

export const PERSON_PROFILE = gql`query userDetailQuery($id: Int!) {
  user(id: $id) {
    id,
    firstName,
    lastName,
    birthDate,
    photo,
    dateJoined,
    isActive,
    email
  }
}`;

export const UPDATE_PERSON_PROFILE = ``;
