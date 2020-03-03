<template>
  <b-container>
    <b-row>
      <div class="col-lg-8">
        <h1>Title</h1>
        <p class="lead">
          By <router-link :to="{ name: 'PersonProfile', params: {id: author.id }}">{{ author.name }}</router-link>
        </p>
        <hr/>
          <p>Posted on {{convertDateFormat(news.createdAt)}}</p>
          <hr/>
          <p>Updated on {{convertDateFormat(news.updatedAt)}}</p>
          <div>
            <div>
              <img class="img-fluid rounded" :src="news.titleImage" alt="Title Image" />
              <hr/>
            </div>
          </div>
          <p class="lead main-text">{{ news.description }}</p>
      </div>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: "blogDetail",
    data() {
      return {
        commentText: "",
        news: {
          id: "",
          titleImage: "",
          createdAt: "",
          updatedAt: "",
          description: "jfjhdefrgk suejrygfkjrhg seruyg hsgrjs hyerguiysergsleruyg sher,jg ",
        },
        author: {
          id: "",
          name: "",
        },
      }
    },
    methods: {
      convertDateFormat(date) {
        return date.toString().split('T')[0];
      },
    },
  }
</script>

<style scoped lang="scss">
  .row {
    justify-content: center;
  }

  .news-detail {
    text-align: left;
  }

  .main-text {
    text-indent: 30px;
    text-align: justify;
  }
</style>
