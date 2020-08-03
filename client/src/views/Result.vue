<template>
  <div id="result">
    <div>
      <p>$${{ $route.params.result }}$$</p>
    </div>
    <router-link to="/integrals" class="button">
    <h2>New integral</h2>
    </router-link>
  </div>
</template>
<script>
export default {
  name: 'result',
  mounted() {
    // laad mathjax
    let MathJax = document.createElement('script')
    MathJax.setAttribute('src', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
    document.head.appendChild(MathJax)
    window.MathJax.typeset()
  }
}
</script>
<style scoped>
#result {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#result div{
  margin-top: 100px;
  padding: 5px;
  width: 90%;
  height: fit-content;
  align-self: center;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  justify-content: center;
  align-items: center;
  
}

#result div p {
  text-align: center;
  color: black;
  font-size: 1.3rem;
  overflow: scroll;
}
.button {
  margin-top: 40px;
  width: 50vw;
  height: 50px;
  background-color: #01579B;
  border: none;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}

.button h2 {
  color: white;
  text-decoration: none;
  text-align: center;
  font-size: 1.4rem;
  font-weight: 400;
}
</style>