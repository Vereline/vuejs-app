<template>
  <b-container>
    <b-row class="justify-content-md-center">
      <div class="col-lg-8">
        <b-card-group deck>
          <b-card
            class="mb-3 text-left"
            style="max-width: 640px;"
            align="center">
            <div class="text-uppercase card-header"><h5>Leave a comment</h5></div>
            <b-card-body>
              <b-form>
                <b-form-group>
                  <b-textarea class="form-control"
                              rows={3}
                              placeholder="Enter something..."
                              v-model="commentText"
                              required>
                  </b-textarea>
                </b-form-group>
                <b-button type="submit"
                          class="btn btn-success align-content-end float-right"
                          v-on:click="submitButton">
                    Submit
                </b-button>
              </b-form>
            </b-card-body>
          </b-card>
        </b-card-group>
      </div>
    </b-row>
  </b-container>
</template>

<script>
  import {COMMENT_ADD, COMMENT_UPDATE} from "./index"

  export default {
    name: "commentForm",
    props: {
      blogPostId: String,
      commentId: String,
    },
    computed: {
      userId () {
        return this.$store.state.id
      },
    },
    data() {
      return {
        commentText: "",
      }
    },
    methods: {
      submitButton(){
        if (this.commentId)
          this.updateComment();
        else
          this.addComment();
      },
      addComment() {
        this.$apollo
          .mutate({
            mutation: COMMENT_ADD,
            variables: {
              text: this.commentText,
              blogPost: this.blogPostId,
              authorId: this.userId
            }
          })
          .then(response => {
            // add comment to list of comments
            debugger;
            let commentData = {
              id: response.data["id"],
              text: response.data["text"],
              createdAt: response.data["createdAt"],
              updatedAt: response.data["updatedAt"],
              author: {
                id: response.data["author"]["id"],
                firstName: response.data["author"]["firstName"],
                lastName: response.data["author"]["lastName"],
                photo: response.data["author"]["photo"],
              },
            };
            this.$emit('add-comment', commentData)
          })
      },
      updateComment() {
        this.$apollo
          .mutate({
            mutation: COMMENT_UPDATE,
            variables: {
              text: this.commentText,
              id: this.commentId,
            }
          })
          .then(response => {
            // update comment in list of comments
            let commentData = {
              id: response.data["id"],
              text: response.data["text"],
              createdAt: response.data["createdAt"],
              updatedAt: response.data["updatedAt"],
              author: {
                id: response.data["author"]["id"],
                firstName: response.data["author"]["firstName"],
                lastName: response.data["author"]["lastName"],
                photo: response.data["author"]["photo"],
              },
            };
            this.$emit('update-comment', commentData)
          })
      },
    },
    apollo: {

    },
  }
</script>

<style scoped lang="scss">
  .card-header {
    background-color: inherit;
  }
</style>
