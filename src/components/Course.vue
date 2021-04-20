

<template>
  <div class="courseRow">
    <tr>
	<td>{{ title }}</td>
	<td>{{ subject }}{{ course }}</td>
	<td>{{ CRN }}</td>
	<td>{{ description }}</td>
    </tr>
  </div>
</template>

<script>
export default {
  name: "Course",
  props: {
    title: String,
    subject: String,
    course: String,
    CRN: Number,
    section: String,
    description: String,
    instructor: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.course {
    margin: 50px;
}
</style>
