<template>
  <b-container >
    <b-row>
      <div class="col-lg-8">
        <b-card class="mb-3 text-left">
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
                        class="btn btn-success align-content-end float-right">
                  Submit
              </b-button>
            </b-form>
          </b-card-body>
        </b-card>
      </div>
    </b-row>
  </b-container>
</template>

<script>
  import {COMMENT_ADD, COMMENT_UPDATE} from './index'

  export default {
    name: "commentForm",
    props: {
      blogPostId: String,
    },
    computed: {

    },
    data() {
      return {
        commentText: "",
      }
    },
    methods: {
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
