<template>
  <div class="home">
    <div class="header">
      <div class="Title">
        <h1>Symbolic calculations made easy</h1>
        <p>Sympy-GUI is an online symbolic calculator based on sympy. Solve integrals, derivatives and differential equations with ease!</p>
      </div>
      <img
        src="@/assets/Graph.png"
        alt="Graph"
        class="desktop"
      >
    </div>
    <div class="features">
      <div
        v-for="link in navigation"
        :key="link.title"
        class="feature"
      >
        <div>
          <h2>{{ link.title }}</h2>
          <img 
            :src="require(`@/assets/${link.img}`)"
            alt=""
            class="mobile"
          >
          <p>{{ link.info }}</p>
          <button @click="goTo(link.to)">
            Get Started
          </button>
        </div>
        <img
          :src="require(`@/assets/${link.img}`)"
          alt=""
          class="desktop"
        >
      </div>
    </div>
    <footer>
      <div>
        <h2>How it works</h2>
        <p>All calculations on Sympy-GUI are made by the open-source python library sympy. Learn more about sympy at www.sympy.org</p>
      </div>
      <div>
        <h2>About us</h2>
        <p>Sympy-GUI is built and maintained by three Belgian university students committed to making maths easier for everyone.</p>
      </div>
      <div>
        <h2>Contact</h2>
        <p>Contact us about bugs and improvements at Bjarne.Vergouwen@gmail.com</p>
      </div>
      <div>
        <h2>Privacy Policy</h2>
        <p>Sympy-GUI makes use of third party cookies by Google. By using this site you agree to the terms of service.</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      navigation: [
        {
          title: 'Integral Calculator',
          info: 'Calculate single and multiple integrals. Fast and easy',
          img: 'Double_integral.svg',
          to: '/integrals'
        },
        {
          title: 'Derivative Calculator',
          info: 'Calculate regular and partial derivatives.',
          img: 'partial_derivative.svg',
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
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

@font-face {
  font-family: Whyte Inktrap;
  src: url("../assets/WhyteInktrap-Regular.woff2");
  font-weight: 400;
  font-display: swap;
}

@font-face {
  font-family: Whyte;
  src: url("../assets/Whyte-Regular.woff2");
  font-weight: 400;
  font-display: swap;
}

@font-face {
  font-family: Whyte;
  src: url("../assets/Whyte-Bold.woff2");
  font-weight: 700;
  font-display: swap;
}

.desktop {
  display: none;
}

h1 {
  font-family: Whyte Inktrap, sans-serif;
  font-size: 3.5rem;
  color: white;
  line-height: 1.05;
  justify-content: space-between;
}

h2 {
  font-size: 2.8rem;
  font-family: Poppins, sans-serif;
  font-weight: 500;
  line-height: 1.3;
}

p {
  font-family: roboto, sans-serif;
  font-weight: 300;
  font-size: 1.1rem;
}

 button {
  background-color: white;
  border: solid 1px black;
  width: 180px;
  height: 50px;
  border-radius: 30px;
  font-family: Poppins, sans-serif;
  font-size: 1.2rem;
  font-weight: 500;
}

button:hover {
  background-color: #4D4D4D;
  color: white;
  border: None;
  transition: 0.5s ease;
}

.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url("../assets/grid.png");
  background-size: 80%;
}

.header {
  margin-top: 70px;
  display: flex;
  width: 100%;
  background-image: url("../assets/vector_mobile.svg");
  background-position: center bottom;
}

.header h1 {
  text-align: left;
}

.header p {
  color: rgba(255, 255, 255, 80);
  text-align: right;
  margin-top: 45px;
  align-self: flex-end;
  margin-right: 20px;
  width: 95%;
}

.Title {
  flex-grow: 1;
  margin: 30px;
  margin-bottom: 120px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}

.features {
  margin: 60px 40px 70px 40px;
  display: flex;
  flex-direction: column;
}

.feature {
  margin-bottom: 50px;
}

.feature > div {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.feature > div > div {
  width: 100%;
}

.feature > div > * {
  margin-top: 20px;
}

.feature h2 {
  color: #4D4D4D;
  width: 60%;
  text-align: left; 
}

.feature p {
  text-align: left;
}

.feature img{
  width: 90%;
}

footer {
  background-color: #444444;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 20px 40px 20px;
}

footer > div {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 85%;
}

footer h2 {
  font-size: 1.4rem;
  margin-top: 25px;
  margin-bottom: 10px;
}

footer p {
  width: 100%;
  font-size: 1rem;
  font-weight: 200;
}
</style>