<template>
  <div class="home">
    <h1>Welcome to Sympy-GUI</h1>
    <p id="subtext">
      Sympy-GUI is an online symbolic calculator based on sympy. 
      Solve integrals, derivatives and differential equations with ease!
    </p>
    <div
      v-for="link in navigation"
      :key="link.title"
      class="nav_element"
      @click="goTo(link.to)"
    >
      <img
        :src="require(`../assets/${link.img}`)"
        alt=""
      >
      <div>
        <h2>{{ link.title }}</h2>
        <p>{{ link.info }}</p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data() {
    return {
      navigation: [
        {
          title: 'Integral Calculator',
          info: 'Calculate single and multiple integrals with parameters.',
          img: 'integraal_functie.jpg',
          to: '/integrals'
        },
        {
          title: 'Derivative Calculator',
          info: 'Calculate regular and partial derivatives.',
          img: 'afgeleide_functie.jpg',
          to: '/derivatives'
        }
      ]
    }
  },
  methods: {
    goTo(to) {
      this.$router.push({path: to})
    }
  }
}
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center
}

h1 {
  font-weight: 600;
  margin-top: 3vh;
}

h2 {
  color: rgba(0, 47, 108, 0.9);
}

p {
  color:rgba(0, 0, 0, 0.60);
  font-weight: 300;
  font-size: 0.9rem;
}

#subtext {
  width: 85%;
  margin-top: 2vh;
  margin-bottom: 1vh;
}

.nav_element {
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  width: 93%;
  display: flex;
  height: 110px;
  margin-top: 30px;
  border-radius: 15px;
}

.nav_element div {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  align-items: baseline;
  margin-left: 20px;
}

.nav_element h2 {
  margin-top: 10%;
  margin-bottom: 8px;
}

.nav_element p {
  text-align: left;
}

.nav_element img {
  height: 100%;
  border-radius: 15px 0px 0px 15px;
}
</style>