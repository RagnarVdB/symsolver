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
    <div id="bounds">
      <h2>Variables and bounds</h2>
      <div id=bounds-table>
        <h3>Variable</h3>
        <h3>Lower bound</h3>
        <h3>Upper bound</h3>
          <input type="text" v-for="n in 3*varAmount" v-bind:key="n" v-on:input="setBounds(n - 1, $event.target.value)">
      </div>
      <p>Bounds can be left empty for indefinite integrals. Use inf for infinity. 
        <br>
        Symbols in the integrand not entered as variables will be treated as parameters.</p>
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
      bounds: [[null, null, null]],
    }
  },
  methods: {
    setBounds(n, value) {
      const row = Math.floor(n/3)
      const column = n % 3
      if (!this.bounds[row]) {
        this.bounds[row] = [null, null, null] //voeg lege rij toe aan matrix voor nieuwe variabele
      }
      this.bounds[row][column] = value
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
  font-size: 1.15rem;
  font-weight: 400;
}

h3 {
  font-weight: 300;
  font-size: 1rem;
}

p {
  font-size: 0.9rem;
  font-weight: 300;
  color: rgba(0, 0, 0, 0.6);
}

input {
  border: none;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  border-radius: 7px;
  height: 40px;
  font-size: 1.2rem;
}

input.small {
  width: 60px;
  text-align: center;
}

input.large {
  width: 100%;
  height: 50px;
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

#bounds {
  display: flex;
  flex-direction: column;
  width: 100%;
}

#bounds-table {
  display: grid;
  width: 100%;
  grid-template-columns: 1fr 2fr 2fr;
  justify-items: center;
  gap: 20px 10px;
  margin-bottom: 20px;
}

#bounds p {
  margin-left: 8px;
}

#bounds-table input{
  width: 80%;
  text-align: center;
}

</style>