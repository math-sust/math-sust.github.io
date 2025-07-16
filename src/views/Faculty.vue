<template>
  <div class="faculty">
    <h1>Faculty Resources Page</h1>
    <p>
      If you would like to incorporate sustainability in the classroom, you may
      find the following resources helpful:
    </p>

    <div>
      <md-button
        href="https://www.wpi.edu/offices/sustainability"
        class="md-raised md-primary"
        >WPI Office of sustainablity</md-button
      >
      <md-button
        href="https://web.wpi.edu/Images/CMS/Facilities/WPI_Sustainability_Plan.pdf"
        class="md-raised md-primary"
        >WPI Sustainability Plan
      </md-button>
    </div>
    <div id="faculty-content" class="md-elevation-2">
      <h2>Faculty Resources</h2>
      <md-tabs
        class="md-transparent"
        md-alignment="fixed"
        style="min-height: 80vh;"
      >
        <md-tab id="tab-findings" md-label="Student Interests"
          >For their IQP, a student project team surveyed 101 students across 11 sustainability themed courses to
          learn about their interests in specific Sustainable Development Goals
          and their desired delivery methods. They  received the following results.
          To read more about their findings and methodology, see our paper (in
          'About this site').<br />
          <img src="../assets/studentinterestsdg.png" />
          <br /><br />
          <img src="../assets/studentinterestdelivery.jpg" />
          <p></p>
        </md-tab>
        <md-tab id="tab-resources" md-label="Sustainability Resources">
          Here are some of the resources other faculty provided which may help
          incorporate sustainability in the classroom.
          <md-table>
            <md-table-row>
              <md-table-head>Title</md-table-head>
              <md-table-head>Description</md-table-head>
            </md-table-row>
            <md-table-row>
              <md-table-cell
                ><a
                  href="https://hub.aashe.org/browse/publication/15675/A-Guide-for-Applied-Sustainability-Learning-Projects-Advancing-sustainability-outcomes-on-campus-and-in-the-community"
                >
                  A Guide for Applied Sustainability Learning Projects
                </a></md-table-cell
              >
              <md-table-cell
                >This guide provides a step-by-step framework for how a new or
                existing applied learning for sustainability program can be
                systematically designed, built and scaled
              </md-table-cell>
            </md-table-row>
            <md-table-row>
              <md-table-cell
                ><a
                  href="https://www.iise.org/iemagazine/2019-11/html/erdil/erdil.html"
                >
                  A focus on sustainability as a core value
                </a></md-table-cell
              >
              <md-table-cell>
                An article that describe links between IE approaches to
                problem-solving and facility layout
              </md-table-cell>
            </md-table-row>
            <md-table-row>
              <md-table-cell>
                <a href="https://engineeringunleashed.com/">
                  Engineering Unleashed
                </a>
              </md-table-cell>
              <md-table-cell
                >Engineering Unleashed is a network of thousands of engineering
                faculty just like you, working to unleash undergraduate
                engineers so that they can create personal, economic, and
                societal value through the entrepreneurial mindset.
              </md-table-cell>
            </md-table-row>

            <md-table-row>
              <md-table-cell
                >Development Economics: Theory, Empirical Research, and Policy
                Analysis
              </md-table-cell>
              <md-table-cell
                >Theory Empirical Research and Policy Analysis by Julie
                Schaffner offers a means to think about development and policy
                in a way that is disciplined by economic theory and informed by
                empirical research. The main goal of this text is to get readers
                to think rigorously using tools of economic analysis. This text
                will help to define development objectives, understand the
                development process, identify potential barriers to development,
                design candidate development interventions, and analyze the
                multidimensional impact of theory, empirical research and policy
                analysis within the study of economic development.
              </md-table-cell>
            </md-table-row>
          </md-table>
        </md-tab>
      </md-tabs>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped>
.faculty {
  max-width: 1000px;
}
#faculty-content {
  margin-top: 20px;
  background-color: white;
  padding: 20px;
}

#tab-resources {
  text-align: left;
}

.md-tab {
  min-height: 800px;
}
</style>
