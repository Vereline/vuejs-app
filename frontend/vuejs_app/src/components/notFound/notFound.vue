<template>
  <div class="page-wrap d-flex flex-row align-items-center">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-12 text-center">
          <span class="display-1 d-block">404</span>
          <div class="mb-4 lead">{{ $t("notFound.mainDiv") }}</div>
          <router-link to="/" class="btn btn-link">{{ $t("notFound.mainLink") }}</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "notFound"
    }
</script>

<style scoped lang="scss">
  .page-wrap {
    min-height: 100vh;
  }
</style>
