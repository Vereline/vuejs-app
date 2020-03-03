<template>
  <b-container>
    <b-row>
      <div class="col-lg-8">
        <b-card class="my-4 text-left">
          <h5 class="card-header">Comment header</h5>
          <b-card-body>
            <b-form>
              <b-form-group>
                <b-textarea class="form-control"
                          rows={3}
                          value={{commentText}}
                          required>
                </b-textarea>
              </b-form-group>
              <b-button type="submit"
                      class="btn btn-success align-content-end">
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
    export default {
      name: "commentForm",
      data() {
        return {
          commentText: "",
          newsId: "",
        }
      },
      methods: {
      },
    }
</script>

<style scoped lang="scss">

</style>
