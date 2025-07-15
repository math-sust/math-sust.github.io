<template>
  <div class="md-layout md-gutter md-alignment-top-center">
    <div class="md-layout-item md-size-33">
      <span>12121</span>
    </div>
    <div class="md-layout-item md-size-66">
      <span>12121</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "TestPage",
};
</script>

<style lang="scss" scoped>
@import "~vue-material/dist/theme/engine";
.md-layout {
  width: 100%;
}

.md-layout-item {
  min-height: 40px;
  // transition: .3s $md-transition-stand-timing;

  span {
    width: 100%;
    height: 100%;
    padding: 8px;
    display: block;
    background: lightgreen;
  }
}
</style>
