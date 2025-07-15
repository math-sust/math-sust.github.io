<template>
  <div class="about">
    <div class="container">
      <img class="container__imageL" src="../assets/wpibuild.jpg" />
      <div class="container__text">
        <h1>About the Project</h1>
        <p>
          This site was developed by a student project team interested in promoting the SDGs, and sustainability in education for WPI faculty and students. The students interviewed faculty who teach
          sustainability themed curriculum and surveyed their students to find
          out what sustainability topics are currently being covered at WPI and
          what topics students want to learn about. The used this information to
          help them and provide a website that serves both students and
          faculty. It allows for students to filter through sustainable courses
          by subject or sustainability topic. It allows faculty to have easy
          access to ways sustainability can be integrated in curriculum,
          some resources to help with this process, and info on student interest in
          sustainability topics and delivery methods. 
	</p>
        <p>
      </div>
    </div>
    <div class="container">
      <img class="container__imageR" src="../assets/sdglogo.png" />
      <div class="container__text">
        <h1>About the Sustainable Development Goals</h1>
        <p>
          For this site, sustainability themed courses are organized according to the United Nations’ Sustainable Development Goals (SDGs). The SDGs are 17 goals that were announced as part
          of the United Nations 2030 Agenda for Sustainable Development. The goals help to map sustainability because these goals because they encompass a wide array of topics. WPI's Office of Sustainability and an SDG working group has also expressed interest in promoting the Sustainable Development Goals in curricula.
        </p>
        <p>
          To read more about the Sustainable Development Goals, visit the
          <a href="https://sustainabledevelopment.un.org/"
            >Sustainable Development Goals Knowledge Platform.</a
          >
        </p>
      </div>
    </div>
    <div class="container">
      <img class="container__imageL" src="../assets/team.png" />

      <div class="container__text">
        <h1>About Us</h1>

        <p>
          Thanks to the team of three WPI undergraduate students who developed teh foundation for this site: Emily Baker, Rui Huang and Akash Shaji. They completed this project in order to fulfill our Interactive Qualifying Project Requirement (IQP). The team was scheduled to complete our IQP at the University of Worcester in Worcester, UK, but due to COVID-19 they were required to do our project remotely instead. This still ended up being a 
          rewarding experience as they spent their term focused on addressing an important issue much closer to home. 
          
        </p>
<p>

</p>

	
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.container {
  padding: 20px 40px 40px;
  /*max-width: 600px;*/
  &__imageL {
    width: 350px;
    margin: 15px 15px 15px 0;
    float: left;
    border-radius: 25px;
  }
  &__imageR {
    width: 350px;
    margin: 15px 15px 15px 0;
    float: right;
  }
  &__text {
    display: inline;
  }
}

h1 {
  line-height: 120%;
}

p {
  font-size: 18px;
  text-align: left;
  //  text-indent : 5em;
}
</style>
