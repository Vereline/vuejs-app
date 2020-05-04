<template>
  <b-container>
    <div class="about-us">
      <section class="about-intro">
        <h2>{{ $t("aboutMessages.header") }}</h2>
        <img  class="img-fluid table-img" src="https://via.placeholder.com/960x300" alt="">
        <p class="text-justify">In sed neque id libero pretium luctus. Vivamus faucibus. Ut vitae elit. In hac habitasse platea dictumst. Proin et nisl ac orci tempus luctus. Aenean lacinia justo at nisi. Vestibulum sed eros sit amet nisl lobortis commodo. Suspendisse nulla. Vivamus ac lorem. Aliquam pulvinar purus at felis. Quisque convallis nulla id ipsum. Praesent vitae urna. Fusce blandit nunc nec mi. Praesent vestibulum hendrerit ante.</p>
        <p class="text-justify">Vivamus accumsan. Donec molestie pede vel urna. Curabitur eget sem ornare felis gravida vestibulum.Sed pulvinar, tellus in venenatis vehicula, lorem magna dignissim erat, in accumsan ante lorem sit amet lorem.</p>
      </section>
    </div>

    <section id="team">
      <h2 class="m-auto our-team">{{ $t("aboutMessages.teamHeader") }}</h2>
      <b-row>
        <b-col v-for="(user, i) in users"
               :key="`User${i}`"
               :value="user">
          <b-card class="card mt-2">
            <img src="https://via.placeholder.com/300" alt="John" style="width:100%">
            <h1>{{fullName(user.firstName, user.lastName)}}</h1>
            <p class="title">{{user.job}}</p>
            <p>{{user.position}}</p>
            <p><b-button class="btn-success">{{ $t("aboutMessages.contactButton") }}</b-button></p>
          </b-card>
        </b-col>
      </b-row>
    </section>
  </b-container>
</template>

<script>
    export default {
      name: "About",
      data() {
        return {
          users: [
            {
              firstName: "Johnatan",
              lastName: "Doe",
              id: "1",
              job: "Software Developer",
              position: "Frontend",
            },
            {
              firstName: "Viktoryia",
              lastName: "Stanko",
              id: "2",
              job: "Software Developer",
              position: "Full-stack",
            },
          ],
        }
      },
      methods: {
        fullName(firstName, lastName) {
          return firstName + ' ' + lastName
        },
      },
    }
</script>

<style scoped lang="scss">
  .about-us {
    h2 {
      margin-bottom: 50px;
      padding-bottom: 40px;
      font-size: 80px;
      text-align: center;
      text-transform: uppercase;
      border-bottom: 1px solid #CCCCCC;
    }

    .about-intro {
      margin-bottom: 50px;

      p {
        margin: 20px 0 0 0;
        padding: 0;
      }

      img {
        margin: 0 auto;
        width: 100%;
      }
    }
  }

  .card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    max-width: 300px;
    margin: auto;
    text-align: center;
  }

  .our-team {
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 50px;
  }

  .title {
    color: grey;
    font-size: 18px;
  }

  button {
    border: none;
    outline: 0;
    display: inline-block;
    padding: 8px;
    /*color: white;*/
    /*background-color: #000;*/
    text-align: center;
    cursor: pointer;
    width: 100%;
    font-size: 18px;

    /*&:hover{*/
    /*   opacity: 0.7;*/
    /*}*/
  }

  a {
    text-decoration: none;
    font-size: 22px;
    color: black;

    &:hover {
      opacity: 0.7;
    }
  }
</style>
