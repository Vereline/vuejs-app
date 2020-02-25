<template>
  <b-container>
    <div class="about-us">
      <section class="about-intro">
        <h2>About Us</h2>
        <img  class="img-fluid table-img" src="https://via.placeholder.com/960x300" alt="">
        <p class="text-justify">In sed neque id libero pretium luctus. Vivamus faucibus. Ut vitae elit. In hac habitasse platea dictumst. Proin et nisl ac orci tempus luctus. Aenean lacinia justo at nisi. Vestibulum sed eros sit amet nisl lobortis commodo. Suspendisse nulla. Vivamus ac lorem. Aliquam pulvinar purus at felis. Quisque convallis nulla id ipsum. Praesent vitae urna. Fusce blandit nunc nec mi. Praesent vestibulum hendrerit ante.</p>
        <p class="text-justify">Vivamus accumsan. Donec molestie pede vel urna. Curabitur eget sem ornare felis gravida vestibulum.Sed pulvinar, tellus in venenatis vehicula, lorem magna dignissim erat, in accumsan ante lorem sit amet lorem.</p>
      </section>
    </div>

    <section id="team">
      <h2>Our Team</h2>
    </section>
  </b-container>
</template>

<script>
    export default {
      name: "About",
      data() {
        return {
        }
      }
    }
</script>

<style scoped lang="scss">
.about-us{
  h2 {
    margin-bottom:50px;
    padding-bottom:40px;
    font-size:80px;
    text-align:center;
    text-transform:uppercase;
    border-bottom:1px solid #CCCCCC;
  }

  .about-intro {
    margin-bottom:50px;

    p {
      margin:20px 0 0 0;
      padding:0;
    }

    img {
      margin: 0 auto;
      width: 100%;
    }
  }

}

</style>
