<template>
  <div id="app">
    <nav :class="{ nav_expanded: expanded }">
      <div id="nav_head">
        <svg
          width="40"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
          @click="toggleNav"
        >
          <path
            id="icon/navigation/close_24px"
            d="M18.3 5.70999C18.1131 5.52273 17.8595 5.4175 17.595 5.4175C17.3305 5.4175 17.0768 5.52273 16.89 5.70999L12 10.59L7.10997 5.69999C6.92314 5.51273 6.66949 5.4075 6.40497 5.4075C6.14045 5.4075 5.8868 5.51273 5.69997 5.69999C5.30997 6.08999 5.30997 6.71999 5.69997 7.10999L10.59 12L5.69997 16.89C5.30997 17.28 5.30997 17.91 5.69997 18.3C6.08997 18.69 6.71997 18.69 7.10997 18.3L12 13.41L16.89 18.3C17.28 18.69 17.91 18.69 18.3 18.3C18.69 17.91 18.69 17.28 18.3 16.89L13.41 12L18.3 7.10999C18.68 6.72999 18.68 6.08999 18.3 5.70999Z"
          />
        </svg>
        <div id="logo">
          <!-- <h1 id="integral">\(\int\)</h1> -->
          <svg
            width="24"
            viewBox="0 0 25 51"
            xmlns="http://www.w3.org/2000/svg"
            fill="#002F6C"
          >
            <path d="M25 3.75226C25 5.1085 24.0054 5.69621 23.1013 5.69621C22.2423 5.69621 21.2477 5.1085 21.2477 3.79747C21.2477 3.16456 21.6094 2.12477 22.9204 1.94394C21.9259 1.08499 20.5244 0.994576 20.0723 0.994576C18.038 0.994576 16.5009 2.12477 15.868 10.443L15.009 21.6998C14.6474 26.7179 13.0199 39.8734 12.4322 42.2242C11.4376 46.293 9.26763 50.226 4.97288 50.226C2.2604 50.226 0 48.6438 0 46.4738C0 45.1175 0.994575 44.5298 1.89873 44.5298C2.75769 44.5298 3.75226 45.1175 3.75226 46.4286C3.75226 47.0615 3.3906 48.1013 2.07957 48.2821C3.02893 49.0958 4.38517 49.2315 4.97288 49.2315C7.54973 49.2315 9.17721 47.1971 9.76492 39.783L10.6239 28.5262C11.0307 23.0561 12.6582 10.3074 13.2007 7.82098C13.9693 4.38517 15.7324 0 20.0271 0C22.7396 0 25 1.58228 25 3.75226Z" />
          </svg>
          <h1>Symsolver<sup>bèta</sup></h1>
        </div>
      </div>
      <hr class="divider">
      <div id="itemsWrapper">
        <router-link
          to="/"
          class="menu_item"
          @click.native="toggleNav"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="home_24px">
              <path
                id="icon/action/home_24px"
                d="M9.99778 19.3275V14.3275H13.9978V19.3275C13.9978 19.8775 14.4478 20.3275 14.9978 20.3275H17.9978C18.5478 20.3275 18.9978 19.8775 18.9978 19.3275V12.3275H20.6978C21.1578 12.3275 21.3778 11.7575 21.0278 11.4575L12.6678 3.9275C12.2878 3.5875 11.7078 3.5875 11.3278 3.9275L2.96778 11.4575C2.62778 11.7575 2.83778 12.3275 3.29778 12.3275H4.99778V19.3275C4.99778 19.8775 5.44778 20.3275 5.99778 20.3275H8.99778C9.54778 20.3275 9.99778 19.8775 9.99778 19.3275Z"
              />
            </g>
          </svg>
          <h2>Home</h2>
        </router-link>
        <router-link
          to="/integrals"
          class="menu_item"
          @click.native="toggleNav"
        >
          <svg
            id="Layer_1"
            data-name="Layer 1"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 21.93 27.74"
          ><title>integral</title><path
            d="M23.63,12.46a1,1,0,0,1-1.05,1.07,1,1,0,0,1-1-1,1,1,0,0,1,.93-1,2.59,2.59,0,0,0-1.58-.52c-1.12,0-2,.62-2.32,5.22l-.47,6.21c-.2,2.77-1.1,10-1.43,11.34-.55,2.25-1.74,4.42-4.12,4.42-1.49,0-2.74-.87-2.74-2.07a1,1,0,0,1,1-1.08,1,1,0,0,1,1,1.05,1,1,0,0,1-.92,1,2.63,2.63,0,0,0,1.59.52c1.43,0,2.33-1.12,2.65-5.22l.47-6.22c.23-3,1.13-10.06,1.43-11.43.42-1.9,1.4-4.32,3.77-4.32C22.38,10.39,23.63,11.26,23.63,12.46Z"
            transform="translate(-1.69 -10.39)"
          /><path
            d="M15.5,12.46a1,1,0,0,1-1.05,1.07,1,1,0,0,1-1-1,1,1,0,0,1,.92-1,2.56,2.56,0,0,0-1.57-.52c-1.13,0-2,.62-2.32,5.22L10,22.37c-.2,2.77-1.1,10-1.42,11.34C8,36,6.81,38.13,4.44,38.13c-1.5,0-2.75-.87-2.75-2.07A1,1,0,0,1,2.74,35a1,1,0,0,1,1,1.05,1,1,0,0,1-.92,1,2.64,2.64,0,0,0,1.6.52c1.42,0,2.32-1.12,2.65-5.22l.47-6.22c.22-3,1.12-10.06,1.42-11.43.43-1.9,1.4-4.32,3.77-4.32C14.25,10.39,15.5,11.26,15.5,12.46Z"
            transform="translate(-1.69 -10.39)"
          /></svg>
          <h2>Integral Calculator</h2>
        </router-link>
      </div>
    </nav>

    <div
      v-if="expanded"
      id="grey"
      @click="toggleNav"
    />

    <header>
      <div class="filler">
        <img
          id="menu_ico"
          src="./assets/menu_24px_rounded.svg"
          alt="menu"
          @click="toggleNav"
        >
      </div>
      <div id="logo">
        <!-- <h1 id="integral">\(\int\)</h1> -->
        <svg
          width="24"
          viewBox="0 0 25 51"
          xmlns="http://www.w3.org/2000/svg"
          fill="#002F6C"
        >
          <path d="M25 3.75226C25 5.1085 24.0054 5.69621 23.1013 5.69621C22.2423 5.69621 21.2477 5.1085 21.2477 3.79747C21.2477 3.16456 21.6094 2.12477 22.9204 1.94394C21.9259 1.08499 20.5244 0.994576 20.0723 0.994576C18.038 0.994576 16.5009 2.12477 15.868 10.443L15.009 21.6998C14.6474 26.7179 13.0199 39.8734 12.4322 42.2242C11.4376 46.293 9.26763 50.226 4.97288 50.226C2.2604 50.226 0 48.6438 0 46.4738C0 45.1175 0.994575 44.5298 1.89873 44.5298C2.75769 44.5298 3.75226 45.1175 3.75226 46.4286C3.75226 47.0615 3.3906 48.1013 2.07957 48.2821C3.02893 49.0958 4.38517 49.2315 4.97288 49.2315C7.54973 49.2315 9.17721 47.1971 9.76492 39.783L10.6239 28.5262C11.0307 23.0561 12.6582 10.3074 13.2007 7.82098C13.9693 4.38517 15.7324 0 20.0271 0C22.7396 0 25 1.58228 25 3.75226Z" />
        </svg>
        <h1>Symsolver<sup>bèta</sup></h1>
      </div>
      <div class="filler" />
    </header>
    
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      expanded: false // controleert of menu zichtbaar is
    }
  },
  mounted() {
    // laad mathjax
    let MathJax = document.createElement('script')
    MathJax.setAttribute('src', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
    document.head.appendChild(MathJax)
  },
  methods: {
    toggleNav() {
      this.expanded = !this.expanded
    },
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: roboto;
  width: auto;
  height: auto;
}

h1 {
  font-size: 1.5rem;
  font-weight: 300;
  color: #002F6C;
  justify-self: center;
}
sup {
  font-weight: 200;
  font-size: 1rem;
}

h2 {
  font-size: 1.3rem;
  font-weight: 500;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

header {
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  width: 100%;
  height: 70px;
}
.filler {
  justify-self: stretch;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

#menu_ico {
  margin-left: 30px;
  width: 40px;
  display: inline-block;
}

#logo {
  display: inline-block;
  width: fit-content;
  margin: auto;
  display: flex;
  align-items: center;
  width: 100%;
  white-space: nowrap;
}

#grey {
  position: absolute;
  background-color: rgba(35, 35, 35, 0.3);
  height: 100vh;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1;
}

nav {
  height: 100vh;
  width: 80vw;
  position: fixed ;
  background-color: white;
  left: -80vw;
  transition: 0.5s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2
}

#logo svg {
  display: none;
}

.nav_expanded {
  left: 0vw !important;
}

#itemsWrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.menu_item {
  display: flex;
  align-items: center;
  text-decoration: none;
  height: 55px;
  width: 92%;
  border-radius: 7px;
  margin-top: 10px;
}

nav img, #itemsWrapper svg {
  width: 33px;
  margin-left: 10px;
  margin-right: 15px;
  fill: rgba(0, 0, 0, 0.54);
}

#nav_head {
  display: flex;
  height: 65px;
  align-items: center;
  width: 90%;
}

#nav_head h2 {
  color: black;
}

#nav_head svg {
  fill: black;
  width: 40px;
}

nav a.router-link-exact-active {
  background-color: rgba(1, 87, 155, 0.2);
}

nav a.router-link-exact-active h2 {
  color: rgba(0, 47, 108, 0.9);
}

nav a.router-link-exact-active svg {
  fill: rgba(0, 47, 108, 0.9);
}

#integral_sym {
  height: 50px;
  width: auto;
}

.menu_item h2 {
  color: rgba(0, 0, 0, 0.6);
  text-decoration: none;
}

hr {
  border: none;
  border-top: 1px solid rgba(0, 0, 0, 0.3);
  color: transparent;
  background-color: transparent;
  width: 85%;
  align-self: center;
}
@media screen and (min-width: 800px){
  header {
    display: none;
  } 
  nav {
    flex-direction: row;
    justify-content: space-between;
    position: fixed;
    left: 0 !important;
    top: 0;
    width: 100%;
    height: 65px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    justify-items: center;
  }

  #nav_head {
    margin-left: 20px;
    widows: auto;
  }

  nav .divider, nav svg {
    display: none;
  }

  #logo svg {
    display: block;
    height: 45px;
    fill: #002F6C;
  }

  #logo h1 {
    font-style: normal;
    font-weight: bold;
    font-size: 1.2rem;
    color: #002F6C;
  }

  #itemsWrapper {
    flex-direction: row-reverse;
    align-items: center;
    width: auto
  }

  .menu_item {
    background-color: white;
    width: fit-content;
    margin-right: 50px;
    margin-top: 0px;
    white-space: nowrap;
  }

  nav a.router-link-exact-active {
    background-color: white;
  }

  nav a h2:hover {
    color: #002F6C;
  }

  nav h2 {
    font-style: normal;
    font-weight: 500;
    font-size: 1.2rem;
    line-height: 26px;
  }

  #grey {
    display: none;
  }
}
</style>
