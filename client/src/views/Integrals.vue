<template>
  <div class="integrals">
    <div id="variables">
      <h2>Number of Variables: </h2>
      <input type="number" v-model="varAmount" class="small">
    </div>
    <div id="integrand">
      <h2>Integrand:</h2>
      <input type="text" v-model="integrand" class="large">
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Integrals',
  data() {
    return {
      varAmount: 1,
      integrand: '',
      bounds: {},
    }
  }
}
</script>

<style scoped>
* {
  text-align: start;
}
h2 {
  color: black;
  font-size: 1.3rem;
  font-weight: 400;
}

input {
  border: none;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  border-radius: 7px;
  height: 45px;
  font-size: 1.2rem;
}

input.small {
  width: 70px;
  text-align: center;
}

input.large {
  width: 100%;
  height: 55px;
  padding-left: 13px;
  padding-right: 13px;
  border-radius: 12px;
  box-sizing: border-box;
  font-size: 1.1rem;
  color: #333333
}

.integrals {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.integrals > div > h2 {
  margin-bottom: 5px;
}

.integrals div {
  margin-top: 20px;
}

#variables {
  width: 100%;
  display: flex;
  align-items: center;
  margin-top: 0px;
}

#variables h2{
  margin-right: 20px
}

#integrand {
  display: flex;
  flex-direction: column;
}
</style>