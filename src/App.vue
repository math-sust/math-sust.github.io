<template>
  <div id="app">
    <div id="nav">
      <md-tabs md-sync-route class="md-primary" md-alignment="centered">
        <md-tab id="tab-home" md-label="Home Page" to="/" exact></md-tab>
        <md-tab
          id="tab-about"
          md-label="About The Project"
          to="/about"
        ></md-tab>
        <md-tab
          id="tab-sustainable"
          md-label="Sustainablility Themed Courses"
          to="/sustainable"
        ></md-tab>
        <md-tab
          id="tab-faculty"
          md-label="Faculty Resources Page"
          to="/faculty"
        ></md-tab>
      </md-tabs>
    </div>
    <div id="content" class="md-elevation-10">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  created() {
    document.title = "WPI Sustainablility Platform";
  },
};
</script>

<style lang="scss">
@import "~vue-material/dist/theme/engine"; // Import the theme engine

@include md-register-theme(
  "default",
  (
    primary: md-get-palette-color(green, 300),
    // The primary color of your application
      accent: md-get-palette-color(cyan, 200)
      // The accent or secondary color
  )
);

@import "~vue-material/dist/theme/all"; // Apply the theme
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
  padding-bottom: 10vh;
}
#content {
  display: flex;
  margin: 0 auto;
  margin-top: 4vh;
  justify-content: center;
  width: 80vw;
  min-height: 80vh;
  padding: 20px;
  background-color: #f6f8f4;
  opacity: 0.95;
  border-radius: 20px;
}
// #nav a {
//   font-weight: bold;
//   color: #2c3e50;
// }
#nav a.router-link-exact-active {
  font-weight: bold;
  color: white;
}
body {
  background-image: url("assets/bridge.jpg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
}
</style>
