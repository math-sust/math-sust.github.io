<template>
  <div class="home">
    <img alt="Sustainable Studies Logo" src="../assets/iqp_logo.png">
    <h1> WPI Sustainability Resources Platform </h1>
    <h3> Sustainable Studies IQP Team</h3>
    <div class="links">
      <md-button to="/about" class="md-raised md-primary">About the project</md-button>
      <md-button to="/sustainable" class="md-raised md-primary">Sustainability Themed Courses</md-button>
      <md-button to="/faculty" class="md-raised md-primary">Faculty Resources</md-button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>

<style lang="scss" scoped>
.home {
  margin: 5%;
}

.links {
  margin-top: 10%;
}
</style>
