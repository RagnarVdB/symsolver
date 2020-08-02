<template>
  <div class="integrals">
    <div id="variables">
      <h2>Number of Variables: </h2>
      <input
        type="number"
        v-model.number="varAmount"
        class="small">
    </div>
    <div id="integrand">
      <h2>Integrand:</h2>
      <input
        type="text"
        v-model="integrand"
        class="large">
    </div>
    <div id="bounds">
      <h2>Variables and bounds</h2>
      <div id=bounds-table>
        <h3>Variable</h3>
        <h3>Lower bound</h3>
        <h3>Upper bound</h3>
          <input
            type="text"
            v-for="n in 3*varAmount"
            v-bind:key="n"
            
            v-on:input="setBounds(n - 1, $event.target.value)"
            >
            
      </div>
      <p>Bounds can be left empty for indefinite integrals. Use inf for infinity. 
        <br>
        Symbols in the integrand not entered as variables will be treated as parameters.</p>
    </div>
    <div id="preview">
      <p :key="latex">$${{ latex }}$$</p>
    </div>
  </div>
</template>

<script>
import getCorrectOrder from '../functions/IntegralOrder.js'

export default {
  name: 'Integrals',
  created() {
    const MathJax = document.createElement('script')
    MathJax.setAttribute('src', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
    document.head.appendChild(MathJax)
  },
  data() {
    return {
      varAmount: 1,
      integrand: '',
      bounds: [['', '', '']],
    }
  },
  mounted() {
    // laad mathjax
    let MathJax = document.createElement('script')
    MathJax.setAttribute('src', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
    document.head.appendChild(MathJax)
  },
  methods: {
    setBounds(n, value) {
      const row = Math.floor(n/3)
      const column = n % 3
      if (!this.bounds[row]) {
        this.bounds[row] = ['', '', ''] //voeg lege rij toe aan matrix voor nieuwe variabele
      }
      let new_row = this.bounds[row]
      new_row[column] = value
      this.$set(this.bounds, row, new_row) // gebruik $set voor reactiviteit
    },
    reRender() {
      console.log('rerendering')
      if (window.MathJax) {
        window.MathJax.typeset()
      }
    },
  },
  computed: {
    latex() {
      let latex_string = ''
      const bounds = (this.boundsOrdered) ? this.boundsOrdered : this.bounds
      for (let bound of bounds) {
        latex_string += `\\int_{${bound[1]}}^{${bound[2]}}`
      }
      latex_string += this.integrand // moet Latex code worden
      const boundsReversed = bounds.slice().reverse()
      for (let bound of boundsReversed) {
        if (bound[0]) {
          latex_string += ' d' + bound[0]
        }
        
      }
      return latex_string
    },
    boundsOrdered() {
      const vars = this.bounds.map(bound => bound[0])
      if (!vars.every(el => Boolean(el))) {
        return false
      } else {
        const usedVars = {}
        for (const variable of vars) {
          usedVars[variable] = []
        }
        for (const bound of this.bounds) {
          for (const variable of vars) {
            if (bound[1].includes(variable) || bound[2].includes(variable)) {
              usedVars[bound[0]].push(variable)
            }
          }
        }
        return getCorrectOrder(this.bounds, usedVars)
        
      }
    }
  },
  watch: {
    latex() {
      // wacht tot volgende cycle event loop zodat nieuwe code gerenderd wordt
      this.$nextTick().then(() => { this.reRender() })
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

#preview {
  margin-top: 40px;
  width: 90%;
  height: fit-content;
  align-self: center;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  justify-content: center;
  align-items: center
}

#preview p {
  text-align: center;
  color: black;
  font-size: 1.3rem;
}

</style>