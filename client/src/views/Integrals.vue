<template>
  <div class="integrals">
    <div id="variables">
      <h2>Number of Variables: </h2>
      <input
        v-model.number="varAmount"
        type="number"
        class="small"
      >
    </div>
    <div id="integrand">
      <h2>Integrand:</h2>
      <input
        v-model="integrand"
        type="text"
        class="large"
      >
    </div>
    <div id="bounds">
      <h2>Variables and bounds</h2>
      <div id="bounds-table">
        <h3>Variable</h3>
        <h3>Lower bound</h3>
        <h3>Upper bound</h3>
        <input
          v-for="n in 3*varAmount"
          :key="n"
          type="text"
            
          @input="setBounds(n - 1, $event.target.value)"
        >
      </div>
      <p>
        Bounds can be left empty for indefinite integrals. Use inf for infinity. 
        <br>
        Symbols in the integrand not entered as variables will be treated as parameters.
      </p>
    </div>
    <div id="preview">
      <p :key="latex">
        $${{ latex }}$$
      </p>
    </div>
    <p
      v-if="notAllVars && showErrors"
      class="error"
    >
      Please enter all variables.
    </p>
    <p
      v-if="invalidSymbolsIntegrand"
      class="error"
    >
      The integrand contains invalid symbols.
    </p>
    <p
      v-if="invalidSymbolsBounds"
      class="error"
    >
      One of the bounds contains invalid symbols.
    </p>
    <p
      v-if="notLowerAndUpper && showErrors"
      class="error"
    >
      All bounds should have both lower and upper bounds, or no bounds
    </p>
    <p
      v-if="impossibleBounds"
      class="error"
    >
      No valid order of integrals is possible.
    </p>
    <button
      id="Integrate"
      @click="integrate"
    >
      Integrate!
    </button>
    <div
      v-if="loading"
      class="lds-ring"
    >
      <div /><div /><div /><div />
    </div>
  </div>
</template>

<script>
import getCorrectOrder from '@/functions/IntegralOrder.js'
import latexGenerator from '@/functions/latexGenerator.js'

export default {
  name: 'Integrals',
  data() {
    return {
      url: process.env.VUE_APP_IP + 'v1/integral', // environment variable, wijst naar localhost in development en server IP in productie
      varAmount: 1,
      integrand: '',
      bounds: [['', '', '']],
      showErrors: false,
      loading: false
    }
  },
  computed: {
    latex() {
      let latex_string = ''
      const bounds = (this.boundsOrdered) ? this.boundsOrdered : this.bounds
      for (let bound of bounds) {
        latex_string += `\\int_{${bound[1]}}^{${bound[2]}}`
      }
      latex_string += latexGenerator(this.integrand) // moet Latex code worden
      const boundsReversed = bounds.slice().reverse()
      for (let bound of boundsReversed) {
        if (bound[0]) {
          latex_string += ' \\: d' + bound[0]
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
    },
    invalidSymbolsIntegrand() {
      // true wanneer de integrand verkeerde symbolen bevat
      return false
    },
    invalidSymbolsBounds() {
      // true wanneer één van de grenzen verkeerde symbolen bevat
      return false
    },
    notAllVars() {
      // true wanneer niet alle vakjes voor variabelen correct zijn ingevuld
      return !this.bounds.every(bound => bound[0] && bound[0].match(/[a-z]/i)) || this.bounds.length != this.varAmount
    },
    impossibleBounds() {
      // true wanneer geen geldige volgorde integralen kan worden gevonden
      return (!this.notAllVars && !this.boundsOrdered)
    },
    notLowerAndUpper() {
      // true wanneer sommige grenzen enkel ondergrens of bovengrens hebben
      return !this.bounds.every(bound => (bound[1] && bound[2]) || !(bound[1] || bound[2]))
    }
  },
  watch: {
    latex() {
      // wacht tot volgende cycle event loop zodat nieuwe code gerenderd wordt
      this.$nextTick().then(() => { this.reRender() })
    }
  },
  created() {
    const MathJax = document.createElement('script')
    MathJax.setAttribute('src', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
    document.head.appendChild(MathJax)
    this.reRender()
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
      if (window.MathJax) {
        window.MathJax.typeset()
      }
    },
    integrate() {
      this.showErrors = true
      if (!this.notAllVars && !this.impossibleBounds && !this.invalidSymbolsIntegrand && !this.invalidSymbolsBounds && !this.notLowerAndUpper) {
        this.loading = true
        const body = JSON.stringify({
          integrand: this.integrand,
          bounds: this.boundsOrdered
        })
        console.log(this.url)
        fetch(this.url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          redirect: 'follow',
          body
        })
          .then(res => res.json())
          .then(data => {
            this.loading = false
            console.log(data)
            this.$router.push({path: `/result/${data}`})
          })
          .catch(err => console.error(err))
      }
    }
  }
}
</script>

<style scoped>
* {
  text-align: start;
}
h2 {
  color: #002F6C;
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

.integrals {
  padding-bottom: 5vh;
}

button {
  grid-area: Button;
  margin-top: 40px;
  width: 50vw;
  height: 50px;
  background-color: #01579B;
  border: none;
  border-radius: 15px;
  color: white;
  align-self: center;
  text-align: center;
  font-size: 1.4rem;
  font-weight: 400;
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
  margin-top: 70px;
  grid-area: Number;
  width: 100%;
  display: flex;
  align-items: center;
}

#variables h2{
  margin-right: 20px
}

#integrand {
  grid-area: Integrand;
  display: flex;
  flex-direction: column;
}

#bounds {
  grid-area: Bounds;
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
  grid-area: Integral;
  margin-top: 40px;
  padding: 5px;
  width: 90%;
  height: fit-content;
  align-self: center;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  justify-content: center;
  align-items: center;
  
}

#preview p {
  text-align: center;
  color: black;
  font-size: 1.3rem;
  overflow: auto;
  width: 100%;
}

.error {
  margin-top: 30px;
  color: red;
  font-size: 1rem;
}

.lds-ring {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
  align-self: center;
}
.lds-ring div {
  box-sizing: border-box;
  display: block;
  position: absolute;
  width: 64px;
  height: 64px;
  margin: 8px;
  border: 6px solid #01579B;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: #01579B transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
/* Desktop versie */
@media screen and (min-width: 900px){
  .integrals {
    justify-content: center;
    display: grid;
    margin-top: 80px;
    grid-template-columns: 400px 400px;
    grid-template-rows: auto;
    grid-gap: 3vh 8vw;
    grid-template-areas: 
    "Number Integral"
    "Integrand Integral"
    "Bounds Button";
    }
  #preview {
    margin-top: 0px;
  }
  #Integrate {
    grid-area: Button;
    width: 60%;
    justify-self: center;
  }
}


</style>
